#while循环：条件满足一直循环，不满足条件退出循环
'''
打印出1-100所有的奇数之和
'''
sum = 0
n = 99
while n >0 :
    sum =sum + n
    n = n - 2
print(sum)

'''
利用循环依次对list中的每个名字打印出hello，xxx!:
'''
L = ['bart', 'lisa', 'adam']
for x in L:
    print('hello,', x, '!')