MainMemory = {}
Complexity={}
LoopVariable={}
ScopeMemory={}
FunctionVariable={}
Function={}

keyword=['int','longlongint','unsignedlonglongint','signedlonglongint','string','float','double','longdouble','char']
operator = ['<', '>', '=', '&', '!', '|']
brackets=[',','(',')','{','}']
arithmetic=['+','-','/','*','%','^']
from filteration import filteration
import Infix_to_postfix
from Postfix_Expression import Postfix_Expression
import measurment
class calculation(object):

    def __init__(self,lst,boundaries):
        self.lst=lst
        self.boundaries=boundaries

######################## Method ############################
    def clear_extra_plus_minus(self, par_string):
        string = ""
        for i in range(len(par_string)):
            if (i == len(par_string) - 1):
                if (par_string[i] != '-' or par_string[i] != '+'):
                    string += par_string[i]

                break
            if (par_string[i] == '+' and par_string[i + 1] == '+'): continue
            if (par_string[i] == '+' and par_string[i + 1] == '-'): continue

            string += par_string[i]

        if (len(string) > 0 and string[-1] == '+'): string = string[:-1]
        return string

######################## Method ############################
    def lst_to_string(self,par_lst):
        tmp_lst = ""
        for inner in par_lst:
            tmp_lst=tmp_lst+inner
        return tmp_lst

######################## Method ############################
    def nested_to_linear(self, par_lst):
        output = []
        output_dict = {}
        filteration([]).reemovNestings(par_lst, output, output_dict)
        return output

######################## Method ############################
# If I have time , I will consider this method
# def go_to_last_variable_in_ScopeMemory(self,key,par_lst,main,visited):
#
#     par_lst = self.nested_to_linear(par_lst)
#     visited.append(key)
#     #print("check", key, par_lst)
#     for kk in range(len(par_lst)):
#         if par_lst[kk] in ScopeMemory and par_lst[kk] not in visited:
#             #print("----",key,par_lst )
#             self.go_to_last_variable_in_ScopeMemory(par_lst[kk],ScopeMemory[par_lst[kk]],visited)
#             print("----",par_lst[kk], ScopeMemory[par_lst[kk]],par_lst)
#             par_lst[kk] = ScopeMemory[par_lst[kk]]
#     #print("check", key, par_lst)
#     return par_lst
######################## Method ############################
    def return_statment(self,par_lst):
        for inner in par_lst:
            for jj in range(len(inner)):
                if inner[jj] in Function:
                    Function[inner[jj]]=Function[inner[jj]]+1
                    a=inner[jj:].index('(')+jj+1
                    b=inner[jj:].index(')')+jj
                    tmp_str = ''
                    while (a < b):
                        tmp_str += inner[a]
                        a += 1
                    tmp_str = tmp_str.split(',')
                    function_name=inner[jj]
                    if (function_name not in MainMemory): MainMemory[function_name] = []
                    MainMemory[function_name].append(tmp_str)




######################## Method ############################
    def function_learning(self):
        for key in Function:
            if key in MainMemory and key in FunctionVariable:
                for outer in MainMemory[key]:
                    for inner in range(len(outer)):
                        FunctionVariable[key][inner].append(outer[inner])

        for key in FunctionVariable:
            for ii in range(len(FunctionVariable[key])):
                string = ''
                outer=FunctionVariable[key][ii]
                check=[]
                for inner in range(len(outer)):
                    if inner==0:
                        check.append(outer[inner])
                        continue
                    tmp_lst=filteration([]).filt(outer[inner])
                    for kk in range(len(tmp_lst)):
                        if(tmp_lst[kk] in MainMemory):
                            tmp_lst[kk]=MainMemory[tmp_lst[kk]]

                    tmp=self.nested_to_linear(tmp_lst)
                    tmp=self.lst_to_string(tmp)
                    tmp=self.clear_extra_plus_minus(tmp)
                    string+=tmp+'+'
                if(len(string)>0):
                    tt=Infix_to_postfix.infix_to_postfix(string[:-1]).split(' ')
                    tt = Postfix_Expression().centralfunc(tt, outer[0])
                    if(len(tt)>0):
                        FunctionVariable[key][ii]=[outer[0],tt]
                    else:
                        FunctionVariable[key][ii] = [outer[0],string[:-1] ]


######################## Method ############################
    def loop_learning(self):

        if (len(LoopVariable) != 0):
            for key in LoopVariable:
                if key in ScopeMemory:
                    LoopVariable[key] = ScopeMemory[key]

        for key in LoopVariable:
            tmp_lst = LoopVariable[key]
            output = self.nested_to_linear(tmp_lst)
            tmp_lst = output
            # exp=tmp_lst
            # a=self.go_to_last_variable_in_ScopeMemory(key,exp,exp,[])
            # print("exp",a)
            for kk in range(len(tmp_lst)):
                if tmp_lst[kk] in ScopeMemory:
                    tmp_lst[kk] = ScopeMemory[output[kk]]
            output=self.nested_to_linear(tmp_lst)
            tmp_str = self.lst_to_string(output)
            tmp_str=self.clear_extra_plus_minus(tmp_str)

            tt=Infix_to_postfix.infix_to_postfix(tmp_str).split(" ")

            tt=Postfix_Expression().centralfunc(tt,key)
            LoopVariable[key]=tt
            #print(tt)
            #print(key, LoopVariable[key])

######################## Method ############################
    def formation(self, par_lst):
        if (par_lst[0] == 'assign'):
            if (par_lst[1] not in ScopeMemory): ScopeMemory[par_lst[1]] = []
            if (par_lst[1] not in MainMemory): MainMemory[par_lst[1]] = []
            MainMemory[par_lst[1]] += [par_lst[3:]] + ['+']
            ScopeMemory[par_lst[1]] += [par_lst[3:]] + ['+']

        elif (par_lst[0] == 'return'):
            if ('return' not in ScopeMemory): ScopeMemory['return'] = []
            if (par_lst[1] not in MainMemory): MainMemory['return'] = []
            MainMemory['return'] += [par_lst[2:]]
            ScopeMemory['return'] += [par_lst[2:]]

        elif (par_lst[0] == 'loop'):
            par_lst_dict = par_lst[2]
            if ('compare' in par_lst_dict):
                for outer_lst in par_lst_dict['compare']:
                    for ii in outer_lst:
                        if (ii not in operator and ii.isdigit() == False):
                            LoopVariable[ii] = []
            if ('assign' in par_lst_dict):
                for inner_lst in par_lst_dict['assign']:
                    if (inner_lst[0] not in LoopVariable): LoopVariable[inner_lst[0]] = []
                    LoopVariable[inner_lst[0]] += [inner_lst[2:]] + ['+']

        elif (par_lst[0] == "function_with_curly_braces"):
            if (par_lst[1] not in Function): Function[par_lst[1]] = 0

            FunctionVariable[par_lst[1]] = []
            for ii in range(len(par_lst)):
                if ii == 0 or ii == 1: continue
                if (par_lst[ii] not in keyword
                        and par_lst[ii] not in operator
                        and par_lst[ii] not in brackets
                        and par_lst[ii] not in arithmetic
                ):
                    FunctionVariable[par_lst[1]].append([par_lst[ii]])

        elif (par_lst[0] == "funtion"):
            function_name = par_lst[1]
            a = par_lst.index('(') + 1
            b = par_lst.index(')')
            tmp_str = ''
            while (a < b):
                tmp_str += par_lst[a]
                a += 1
            tmp_str = tmp_str.split(',')
            if (function_name not in MainMemory): MainMemory[function_name] = []
            if (function_name not in Function):
                Function[function_name] = 0
            MainMemory[function_name].append(tmp_str)
            Function[function_name] = Function[function_name] + 1
######################## Method ############################
    def method(self):
        visited=[]

        for i in range(len(self.lst)):
            visited.append(0)
        for i in self.boundaries:
            first,last=i[0],i[1]
            check_if_forloopE=False
            check_if_loop = False

            ## each function will clear the memory
            if(self.lst[first][0]=="for_loopE"): check_if_forloopE=True
            if (self.lst[first][0] == "loop"):
                check_if_loop = True

            while(first<=last):
                if(visited[last]==0):
                    self.formation(self.lst[last])
                    #print(self.lst[last])
                visited[last]=1
                last=last-1

            # print("CodeMemory: ",ScopeMemory)
            # print("loopVariable: ",LoopVariable)
            # print("functionVariable: ", FunctionVariable)
            # print("Function: ", Function)
            #print()
            tmp=''

            if (check_if_loop):
                self.loop_learning()
                Complexity[(i[0],i[1])]=measurment.loop(LoopVariable)

                LoopVariable.clear()
                ScopeMemory.clear()

            ##for(int i:mp)
            if (check_if_forloopE):
                Complexity[i[0]]='n'


        if ("return" in MainMemory): self.return_statment(MainMemory["return"])
        self.function_learning()
        #print("functionVariable: ", FunctionVariable)
        for key in FunctionVariable:
            measurment.recursion(FunctionVariable[key])

        #print("functionVariable: ", FunctionVariable)
        # print("function: ", Function)
        #print("DDComplexity: ", Complexity)
        MainMemory.clear()
        for key in Complexity:
            Complexity[key]=measurment.final_calculation_loop(Complexity[key])
        measurment.is_nested(Complexity)
        for key in FunctionVariable:
            FunctionVariable[key] = measurment.final_calculation_recursion(FunctionVariable[key],key)
        #print("DDComplexity: ", Complexity)
        # print("functionVariable: ", FunctionVariable)
        return Complexity,FunctionVariable,Function