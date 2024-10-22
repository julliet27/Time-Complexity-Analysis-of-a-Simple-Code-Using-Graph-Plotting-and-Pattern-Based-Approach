import calculation
from filteration import filteration
def final_calculation_loop(par_lst):
    if(type(par_lst) == str): return par_lst

    comp='constant'
    for inner in par_lst:
        l1,l2=inner[0],inner[1]
        if(l2 == 'logn'):
            return l2
        if(l2=='n'):
            comp='n'
    return comp
def final_calculation_recursion(par_lst,key):
    if(type(par_lst) == str): return par_lst
    dict={}
    one_par=0
    for inner in par_lst:
        if(len(inner)<=1):
            one_par=one_par+1
            continue
        l1,l2=inner[0],inner[1]
        if(l2 not in dict): dict[l2]=0
        if(l2!='c'): dict[l2]=dict[l2]+1
    if (len(par_lst)==one_par): return 'not recursive'
    if('logn' in dict):
        if(dict['logn']>=2 and calculation.Function[key]>=2):
            return "master theorm"
    return 'not master theorm'

def is_nested(par_dict):
    tmp_lst=[]
    prev1,prev2=0,0
    prev_tuple=0
    for key in par_dict: tmp_lst.append(key)
    for ii in range(len(tmp_lst)):
        if(ii==0):
            prev1,prev2=tmp_lst[ii][0],tmp_lst[ii][1]
            prev_tuple=tmp_lst[ii]
        else:
            new1, new2 = tmp_lst[ii][0], tmp_lst[ii][1]
            if(new1<prev1 and prev2<new2):
                comp=par_dict[prev_tuple]
                par_dict[tmp_lst[ii]]=par_dict[tmp_lst[ii]]+'*'+comp
                par_dict.pop(prev_tuple)
            prev1, prev2 = tmp_lst[ii][0], tmp_lst[ii][1]
            prev_tuple = tmp_lst[ii]
def choose_linear_or_logarithmic(par_lst):
    print(par_lst)
    if('logn' in par_lst):
        return 'logn'
    elif ( 'n' in par_lst):
        return 'n'
    else:
        return 'constant'
def linear_or_logarithmic(val2,sign,val1,check,par_dict,call):
    ans='n'
    if(call=='loop'):
        if (val2 not in calculation.ScopeMemory
                and val1 not in calculation.ScopeMemory
                and val2 not in par_dict
                and val1 not in par_dict
        ):
                ans='c'
                check=True
        else: ans='n'
    if(sign=='+' or sign=='-'): return ans
    else: return 'log'+ans

def loop(par_dict):

    for key in par_dict:
        value_of_n = ''
        check = False
        for ii in range(len(par_dict[key])):
            tt = filteration([]).filt(par_dict[key][ii])
            val2,sign,val1=tt[0],tt[1],tt[2]

            if(ii==0):

               tm=linear_or_logarithmic(val1,sign,val2,check,par_dict,'loop')
               par_dict[key][ii]=tm
               if (check): value_of_n='const'
               else: value_of_n = key
            else:
               if(val2=='n'): val2=value_of_n
               if (val1 == 'n'): val1 = value_of_n
               tm = linear_or_logarithmic(val2, sign, val1, check,par_dict,'loop')
               par_dict[key][ii] = tm
        print(par_dict[key])
        par_dict[key]=choose_linear_or_logarithmic(par_dict[key])
    lst=[]
    for key in par_dict:
        lst.append([key,par_dict[key]])
    return lst


def recursion(par_lst):

    for inner in par_lst:
        if(len(inner)<=1): continue
        lst=inner[1]
        if(type(lst)==str):
            inner[1]='c'
        else:

            for ii in range(len(lst)):
                tt = filteration([]).filt(lst[ii])

                val2,sign,val1=tt[0],tt[1],tt[2]
                tm = linear_or_logarithmic(val1, sign, val2, False, [], 'recusion')
                lst[ii] = tm
            print(lst)
            inner[1]=choose_linear_or_logarithmic(lst)

            #par_dict[key]=choose_linear_or_logarithmic(par_dict[key])


