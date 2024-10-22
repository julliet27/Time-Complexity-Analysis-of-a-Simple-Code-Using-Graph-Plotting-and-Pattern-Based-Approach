class filteration(object):
    def __init__(self,lst):
        self.lst=lst

    ###################### method ##################
    def reemovNestings(self,M_lst,output,output_dict):
        for ii in M_lst:
            if type(ii) == list:
                self.reemovNestings(ii,output,output_dict)
            elif type(ii) ==tuple:
                self.reemovNestings(ii, output,output_dict)
            elif type(ii) ==dict:
                for pp in ii:
                    if(pp not in output_dict and pp!='assignE' and pp!='assignBY_1'):
                        output_dict[pp]=[]
                    for qq in ii[pp]:
                        if(pp=='assignE' or pp=='assignBY_1'):
                            if ('assign' not in output_dict): output_dict['assign'] = []
                            output_dict['assign'].append(qq)
                        else: output_dict[pp].append(qq)
            elif type(ii) == str :
                output.append(ii)

    ###################### method ##################
    def filt(self,string):  # separating sign and word

        return_lst = []
        tmp_string = ""

        for i in range(len(string)):

            chr=string[i]
            if ("a" <= chr <= "z" or "A" <= chr <= "Z" or "0" <= chr <= "9" or chr == "[" or chr == "]" or chr=='_'):
                tmp_string += chr

            else:  # only char and word insert
                if (tmp_string != ""): return_lst.append(tmp_string)
                tmp_string = ""
                return_lst.append(chr)

        if (tmp_string != ""):
            return_lst.append(tmp_string)  # if in the last their not any sign char
        return return_lst

    ###################### method ##################
    def method(self):
        string = ""
        lst = []
        temporary_lst = []
        for x in self.lst:
            for i in x:
                if (i == "\n"):  # line
                    if (string != ""): lst.append(string)

                    if (len(lst) != 0 and lst[0][0] != "/"):  # deleting comment and empty lines
                        temporary_lst.append(lst)

                    lst = []  # remove previous line && string
                    string = ""
                else:
                    if (i == " "):  # string formatting
                        if (string != ""):

                            lst.append(string)
                        string = ""
                    elif (i == "\t"):
                        string += ""
                    else:
                        if('A'<=i<='Z' or 'a'<=i<='z' or '0'<=i<='9' or i=='_'):
                            string += i
                            #if (i == '_'): print(i,string)
                        else:
                            #if(i=='_'): print(i)
                            if(len(string)>0): lst.append(string)
                            string=""
                            lst.append(i)

        temporary01_lst = []
        for x in temporary_lst:

            return_lst = []
            for y in x:

                return_lst = return_lst + self.filt(y)

            if(return_lst[-1]==';'):temporary01_lst.append(return_lst[:-1])
            else: temporary01_lst.append(return_lst)

        return temporary01_lst
####################################################################