a = {"name": "lin", 2: "key"}
print(a)
for x in a:
    print(x, end="|")
else:
    print("end")


b = {"lin", '23', ("s", 'b', 'k')} #集合存储无序
for k in b:
    print(k,end='')
    for g in k:
        print(g,end='')


 
for x in range(0,10):
    x+=1
    print('x='+str(x),end=' ')
