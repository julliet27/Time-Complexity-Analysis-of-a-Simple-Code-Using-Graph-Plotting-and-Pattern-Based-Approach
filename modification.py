from filteration import filteration
class modification(object):
    def __init__(self,lst):
        self.lst=lst
    def separation(self,string):
        keyword=['int','longlongint','unsignedlonglongint','signedlonglongint'
                 'string','float','double','longdouble','char']
        lst=[]
        string00=''
        for i in string:
            string00+=i
            if(string00 in keyword):
                lst.append(string00)
                string00=''
        if(string00 =='while_loop' or string00=='for_loop'):
            string00='loop'
        # if (string00 == 'assignE' or string00 == 'assignBy_1'):
        #     string00 = 'assign'
        if(len(string00)>0): lst.append(string00)
        return lst

    def method(self):
        lst = []
        for lst00 in self.lst:

            output = []
            output_dict={}

            filteration([]).reemovNestings(lst00,output,output_dict)
            if (lst00[0] == "assignE" or lst00[0] == "assignBY_1"):
                for key in output_dict:
                    tmp_lst=output_dict[key][0]
                    output[0]='assign'
                    for ii in tmp_lst:
                        output.append(ii)
                output_dict.clear()
            #print("OUTPUT :",output)
            #print("OUTPUT_dict:",output_dict)
            lst01=[]
            dict01={}
            for ii in range(len(output)):
                return_lst=filteration([]).filt(output[ii])
                for il in return_lst:
                    tmp=self.separation(il)
                    lst01+=tmp

            for ii in output_dict:
                for pp in output_dict[ii]:
                    lst02 = []
                    if(type(pp)==list):
                        tmp01=[]
                        for yy in pp:
                            return_lst=filteration([]).filt(yy)
                            tmp00=[]
                            for il in return_lst:
                                tmp=self.separation(il)
                                tmp00+=tmp
                            tmp01+=tmp00

                        lst02+=tmp01
                    else:
                        lst02 += filteration([]).filt(pp)
                    if(ii not in dict01): dict01[ii]=[]
                    dict01[ii].append(lst02)
            #print("check",lst01,dict01)
            if(len(output_dict)>0): lst01.append(dict01)
            lst.append(lst01)
        return lst
