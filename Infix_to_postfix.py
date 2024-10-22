def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def associativity(c):
    if c == '^':
        return 'R'
    return 'L'

def infix_to_postfix(s):
    result = []
    stack = []
    string=''
    tmp_str=''
    i=0

    while(i<len(s)):
        c = s[i]
        if(('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')):
            while (('a' <= s[i]<= 'z') or ('A' <= s[i] <= 'Z') or ('0' <= s[i] <= '9')):
                tmp_str+=s[i]
                i=i+1
                if(i==len(s)): break
            result.append(tmp_str)
            tmp_str=''
            i=i-1
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Pop '('
        else:
            while stack and (prec(s[i]) < prec(stack[-1]) or
                (prec(s[i]) == prec(stack[-1]) and associativity(s[i]) == 'L')):
                result.append(stack.pop())
            stack.append(c)
        i=i+1


    while stack: result.append(stack.pop())
    for i in result: string+=i+' '
    return string[:-1]


