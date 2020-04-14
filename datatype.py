import time

# i am  yellow king  not effect your code
print("hi")
if 10 > 9:
    print(time.time())

# test array
test = "123456789"
print(test[0:3])  # 左闭右开
print(test[-1])
print(100 % 12)

print('1' in test)  # 数字不能放在字符串里面
print(test + test)
print(test * 3)
print(type(2 / 1))
print(bool("false"))
print("""huanghang
huanghang
""")
print('huanghang\nhuanghang')
print('huang\
huang')
print(r'c:\programfiles\lins')  # r代表普通字符串
print('lins'[-1])
print('lins'[0:-1])  # 左闭右开

a = 3
a = '50'
print(a)

list5 = [1, 2, 3, 4, 5, 'lin', 'one', 'plus']
list5[1] = 3
list5[-2] = 'ze'
print(len(list5))
for index in range(len(list5)):
    print(list5[index], end='')
# for ele in list:
#     print(ele)
list5 += [400, 600]
list5.append(200)
list5.insert(0, -1)  # 索引插入
if 400 in list5:  # 先判断是否存在
    list5.remove(400)
list5.pop(0)  # 索引删除列表元素
list5.pop(len(list5) - 1)
# list.clear()
print(list5)
list2 = list5
print(list2)
print(list2[0::])

listx = ['jin10', 'qianduan', 'adncxkcnxkc', 'python']
list3 = sorted(listx)  # 列表排序不能有int又有str
list4 = sorted(listx, key=len)
print(list3)
print(list4)

tup = (1, 2, 3, 'fu', 'kc', 'java')
print(tup[2:len(tup)])
print(tup[::-1])

str = 'abcde'
for man in str:
    print(man, end='')

list10 = list(tup)
list10.remove('fu')
print(list10)

listtup = [29, 299, 3999]
tupa = tuple(listtup)
print(tupa)

setest = {2, 3, 3, 4, 4}
setest.add(8)
setest.update([11, 22, 33, 23])
setest.discard(4)
setest.remove(2)
print(setest)
print(setest.pop())
setest2 = {3, 4, 5, 5, 6, 7, 8, 9}
print(3 in setest)
print(setest & setest2)
print(setest2 | setest)
print(setest2 - setest)
print(setest - setest2)  # 对称差运算 去除两个集合相同 并将另外一个指定集合中不同的元素插入到当前集合中

setest3 = {3, 4}
print(setest3 <= setest2)
print(setest2 >= setest3)

dict1 = {'name': 'lin', 'age': 19, 0: 'man'}
print(dict1['name'] + dict1[0])
del dict1['age']
print(dict1)
# dict1.clear()
# del dict1


arr = (11, 22, [1, 3, 2, [222, 2]], {2, 3, 4})
print(arr[2][3][1])


