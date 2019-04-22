# 在各个数字之间插入运算符组成算式,然后计算算式结果(某些数位之间可以没有运算符,但最少要插入1个运算符).
# 问题:求位于1000-9999,满足上述条件的数.

# 一旦用了*号以外的任意运算符,最终结果就凑不到四位了.如果使用+号,最大结果为999+9=1008.
op = ["*", ""]

# 过滤*01之类的情况
def filterZero(op, num):
    if (op != '' and num == '0'):
        return ""
    else:
        return op + num


for num in range(1000, 10000):
    if num % 10 == 0:
        continue

    reversedNum = str(num)[::-1]
    
    for op1 in op:
        for op2 in op:
            for op3 in op:
                result = reversedNum[3] + filterZero(op1, reversedNum[2]) + filterZero(
                    op2, reversedNum[1]) + op3 + reversedNum[0]
                # 保证至少插入一位运算符
                if eval(result) == int(reversedNum) and len(result) > 4:
                    print(result + "=" + reversedNum)

# eval() 逆波兰记法,也可以叫后缀表示法.如1+6+6*5+3,后缀表示法则为 16+65*3+
