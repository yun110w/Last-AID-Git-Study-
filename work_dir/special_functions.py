def pow(a, b):
    return a**b # a^b 기능을 구현함.

def abs(a):
    if(a<0):
        return -a # 음수일때 양수로 전환 후 리턴
    else:
        return a # 양수일때 그대로 리턴

def mod(a, b):
    return a%b # a를 b로 나눈 나머지를 리턴