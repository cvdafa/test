#break可以提前退出循环
'''n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')
'''
'''
n = 1
while n <= 100:
    if n > 10: #当 n=11时，满足条件，执行break语句
        break #break语句会提前结束当前循环
    print(n)
    n= n+1
print('END')
'''
#continue跳过当次循环，直接开始下一次循环
'''
打印出1-100的所有奇数
'''
i =0
while i <= 100:
    i= i+1
    if i%2 == 0:
        continue
    print(i)