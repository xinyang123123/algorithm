# 如果把某个数的各个数字按相反的顺序排列,得到的数字和原来的数相同,则这个数字就是回文数.比如123454321.
# 问题:求用十进制,二进制,八进制表示都是回文数的所有数字中,大于十进制数10的最小值.

num = 11

while True:
    binNum = str(bin(num))[2:]
    octNum = str(oct(num))[2:]
    
    if (str(num) == str(num)[::-1] 
        and binNum == binNum[::-1] 
        and octNum == octNum[::-1]):
        print(num)
        break
    else:
        # 因为有二进制的回文数,最后一位为0的情况下首位也必须为0,所以优先排除全部偶数.故这里使用+2
        num += 2

# str() 可以把变量转换为字符串
# bin() 转换为二进制数 自带前缀0b
# oct() 转换为八进制 自带前缀0o
# int() 转换为十进制
# hex() 转换为十六进制 自带前缀0x
# "xx"[::-1] 字符串反转