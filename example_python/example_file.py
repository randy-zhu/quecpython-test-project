import uos
# 文件操作

# create a file
# 创建一个文件操作句柄
f=open('test.txt','w')

# 写入文件
f.write('hello quecpython!\n')
f.write('123456789abcdefg!\n')

# 关闭文件句柄
f.close()

# read a file
f=open('test.txt', 'r')
print(f.readline())
print(f.readline())
f.close()

# 也可使用with方法
with open('test.txt','w')as f:
    f.write("hello quecpython!\n")