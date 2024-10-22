import calculation
class Postfix_Expression:
    def __init__(self):
        self.stack = []
        self.top = -1

    def pop(self):
        if self.top == -1:
            return
        else:
            self.top -= 1
            return self.stack.pop()

    def push(self, i):
        self.top += 1
        self.stack.append(i)

    def centralfunc(self, ab,key):
        lst=[]

        for i in ab:

            if (i not in calculation.arithmetic):
                self.push(i)
            else:
                val1 = self.pop()
                val2 = self.pop()

                if i == '/':
                    self.push('n')
                    lst.append(val2+'/' + val1)
                elif i == '^':
                    self.push('n')
                    lst.append(val1+'**'+val1)

                elif i == '-':
                    self.push('n')
                    lst.append(val2+'-' + val1)
                elif i == '*':
                    self.push('n')
                    lst.append(val2+'*' + val1)

                elif i == '+':
                    self.push('n')
                    lst.append(val2+'+' + val1)

        return lst


# #Driver code
# if __name__ == '__main__':
#     str = '100 200 100 - 2 / + 1 -'
#
#     # Splitting the given string to obtain
#     # integers and operators into a list
#     strconv = str.split(' ')
#     obj = evalpostfix()
#     print(obj.centralfunc(strconv))

