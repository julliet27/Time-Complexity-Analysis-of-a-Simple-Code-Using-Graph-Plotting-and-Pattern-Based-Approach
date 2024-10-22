from filteration import filteration
from boundary import boundary
from pattern import pattern
from modification import modification
from calculation import calculation
import measurment
class file_control(object):
    def __init__(self,lst):
        self.lst=lst
    def method(self):

        filter_lst=filteration(self.lst).method()
        lst1,boundaries=boundary(filter_lst).method()
        pattern_lst = pattern(lst1).method()
        modify=modification(pattern_lst).method()
        Complexity, FunctionVariable, Function = calculation(modify,boundaries).method()
        # for i in modify:
        #     print(i)
        for key in Complexity:
            first,last=key[0],key[1]
            print("--------------Loop Analysis--------------")
            print('>>>> scope: ',key)
            print('>>>> The complexity is','O('+Complexity[key]+')')
            while(first<=last):
                print(lst1[first])
                first=first+1
            print()

        print("--------------Recursive Analysis--------------")
        for key in FunctionVariable:
            print(key,'is',FunctionVariable[key])
        print()

        print("--------------Numeber of function called--------------")
        for key in Function:
            if(Function[key]==0):
                if(key=='main'):print(key, 'is Main function')
                else: print(key, 'is built in')
            else:
                print(key, 'is called',Function[key],'time')
        print()
        ############## presentation a dekabo ###################
        # print(boundaries)
        # for i in boundaries:
        #     print(i)
        #     for j in range(i[0],i[1]+1):
        #         print(j,pattern_lst[j])
        #     print()
        ########################################################







