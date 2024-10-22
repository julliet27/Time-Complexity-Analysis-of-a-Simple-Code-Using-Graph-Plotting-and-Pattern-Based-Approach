from filteration import filteration
import re
class pattern(object):
    def __init__(self,lst):
        self.lst=lst


###################### Method ######################
    def pattern(self,string):
        dic={
        "while_loop": "^(while)\((.+)*\){*",
        "for_loop": "^(for)\((.+)*\;(.+)*\;(.+)*\){*",
        "for_loopE": "^(for)\((.+)*\:(.+)*\){*",
        "condition": "^(if|elseif)\((.+)*\)",
        "compare": "(.*)(==|=>|<=|>|<|!=)(.*)",
        "assignE": "(.*)(\+=|\-=|\*=|\/=|\%=)(.+)*",
        "assignBY_1": "(.*)(\+\+|\-\-)",
        "define":"^(bool|int|string|char|float|double|void|longlongint|unsignedlonglongint|unsignedint)(.+)*",
        "assign":"(.*)(=)(.*)",
        "else":"^(else){*",
        "return":"^(return)(.+)",
        "funtion":"(.+)\((.+)*\){?",
        "break":"break"
        }

        for key,value in dic.items():
            tmp=re.findall(value, string)
            if tmp:
                if(key=='funtion'):
                    tmp[0]=list(tmp[0])
                    tmp[0][1]='('+tmp[0][1]+')'
                st=tmp[0][1]
                for pp in range(len(string)-1):
                    if(string[pp] in ['==','=>','<=','>','<','!='] and key=='compare'):
                        return 'compare',string
                    if (string[pp]+string[pp+1] in ['==', '=>', '<=', '>', '<', '!=']
                        and key=='compare'):
                        return 'compare', string
                if(key=='define'):
                    tm=st.split(',')
                    for ii in range(len(tm)):
                        a = list(re.findall(dic["assign"], tm[ii]))
                        b= list(re.findall(dic["funtion"], st))
                        c = list(re.findall(dic["assignE"], tm[ii]))
                        if a:
                            tm[ii]=list(a[0])
                            return "assign",tm
                        elif b:
                            return "function_with_curly_braces",b
                        elif c:
                            tm[ii] = list(c[0])
                            return "assignE",tm
                        else:return "initial",tmp
                return key,tmp
        return string

###################### Method ######################

    def pattern_match(self,string):
       tmp=list(self.pattern(string))
       output=[]
       output_dict={}
       if(len(tmp)>1):   ##to remove extra parenthesis
           filteration([]).reemovNestings(tmp[1], output,output_dict)
           tmp[1]=output
           pt = tmp[1]
       #print("I_want_to_see",tmp[0])
       if (tmp[0] == "assignBY_1" or tmp[0] == "assignE"):
           string = ''
           for i in pt: string += i
           if (string != ''): pt = [string]
           #print("pt",pt,'tmp',tmp)
       #### i+=1,j=j+1,i++;
       if(tmp[0]=="for_loop"
       or tmp[0]=="while_loop"
       or tmp[0]=="condition"
       or tmp[0]=="for_loopE"
       or tmp[0]=="assignBY_1"
       or tmp[0]=="assignE"):
           ##### this if-else making i+=1 = i=i+1 or i++ = i=i+1
           if(tmp[0]=="assignBY_1" or tmp[0]=="assignE"):
               string=''
               for i in pt: string+=i
               if(string!=''): pt=[string]
           #### this loop iteration is for i+=1,j=j+1,i++; -> assign i=i+1,....

           for i in range(len(pt)):
                dic = {}
                if(len(pt[i])>0 and type(pt[i])==str):
                    tp = pt[i].split(',')
                    #print("I_want_to_see",tmp,tp)

                    for ii in tp:
                        tm=self.pattern(ii)
                        if(tm!=ii):
                            # tm=('assign', [('lamka', 'l+m')]) ii=intlamka=l+m
                            tm=list(tm)

                            key,value=tm[0],list(tm[1][0])
                            if(key=="assignBY_1"):
                                tm[0] = 'assign'
                                if(value[-1]=='++'):
                                    value = [value[0], '=', value[0], '+', '1']
                                if (value[-1] == '--'):
                                    value = [value[0], '=', value[0], '-', '1']

                            if (key == "assignE"):
                                tm[0]='assign'
                                if('+' in value[1]):
                                    value=[value[0],'=', value[0],'+',value[2]]
                                if ('-' in value[1]):
                                    value = [value[0], '=', value[0] , '-' , value[2]]
                                if ('*' in value[1]):
                                    value = [value[0], '=', value[0] , '*' , value[2]]
                                if ('/' in value[1]):
                                    value = [value[0], '=', value[0] , '/' , value[2]]

                            if(key=='compare'): value=tm[1]

                            if(tm[0] not in dic): dic[tm[0]]=[]
                            dic[tm[0]].append(value)

                            #print(tm, ii)
                            #### tm=['assign', ['lamka', 'l+m']] ii=intlamka = l + m

                    if(len(dic)>0):pt[i]=dic



           tmp[1]=pt
       return tmp

###################### Method ######################

    def method(self):
        tmp_lst=[]
        for i in self.lst:
            string = ""
            output = []
            output_dict={}
            for j in i: string += j
            #print("check",string)
            lst00=self.pattern_match(string)
            #print("check after", lst00)
            #print("-----------------------------------")
            filteration([]).reemovNestings(lst00,output,output_dict)
            if(len(output_dict)>0): output.append(output_dict)

            tmp_lst+= [lst00]
        return tmp_lst

##################################################################