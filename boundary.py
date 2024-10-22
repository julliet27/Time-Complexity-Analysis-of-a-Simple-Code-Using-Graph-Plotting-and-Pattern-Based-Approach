class boundary(object):
    def __init__(self,lst):
        self.lst=lst
    def method(self):
        stack = []
        tmp_lst=[]
        cnt = 0
        mn = 10000000
        mx = 0
        for i in self.lst:

            if ("{" in i):

                if (len(i) == 1 and i[0] == '{'):
                    stack.append(cnt-1)
                else:
                    stack.append(cnt)

            if ("}" in i):

                if (len(stack) > 0):
                    mn = min(mn, stack[-1])
                    stack.pop()
                mx = max(mx, cnt)

            cnt += 1

        # If only consider only scoping line , we have to find min boundary and max boundary.
        # In c++ or java code , most of the thing are done in scoping
        # otherthings are include , define , const which will delete by below for loop

        boundaries=[]
        stk=[]
        cnt_idx=0

        for i in range(mn, mx+1):

            if ("cout" not in self.lst[i] and "cin" not in self.lst[i]):

                tmp_lst.append(self.lst[i])
            else: cnt_idx-=1
            if ("{" in self.lst[i]):
                if(len(self.lst[i])==1 and self.lst[i][0]=='{'):
                    stk.append(cnt_idx-1)
                else:
                    stk.append(cnt_idx)
            if ("}" in self.lst[i]):

                if (len(stk) > 0):

                    boundaries.append([stk[-1],cnt_idx])
                    stk.pop()
            cnt_idx+=1
        return tmp_lst,boundaries