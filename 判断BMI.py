h = int(175)
t = int(80.5)
s =80.5*2/(175*175)
if s <=18.5:
    print('过轻')
elif 18.5<s<=25:
    print('正常')
elif 25<s<=28:
    print('过重')
elif 28<s<=32:
    print('肥胖')
else:
    print('严重肥胖')