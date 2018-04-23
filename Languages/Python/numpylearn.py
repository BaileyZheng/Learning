import numpy as np
# a = np.array([1,2,3])
# print(a)

# 多于一个维度
# a = np.array([[1,2],[3,4]])
# print(a)

# 最小维度
# a = np.array([1,2,3,4,5],ndmin=2)
# print(a)

# dtype参数
# a = np.array([1,2,3],dtype=complex)
# print(a)

# 使用数组标量类型
# dt = np.dtype(np.int32)
# print(dt)

# int8,int16,int32,int64可替换为等价的字符串'i1','i2','i4'及'i8'
# dt = np.dtype('i8')
# print(dt)

# 使用端记号
# dt = np.dtype('>i4')
# print(dt)

# 创建结构化数据类型
# dt = np.dtype([('age',np.int8)])
# print(dt)

# 应用于ndarray对象
# a = np.array([(10,),(20,),(30,)],dtype=dt)
# print(a)

# 名字可用于访问age列的内容
# print(a['age'])

# 定义名为student的结构化数据类型，其中包含字符串字段name，整数字段age和浮点字段marks
# student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
# print(student)

# a = np.array([('abc',21,50),('xyz',18,75)],dtype=student)
# print(a)

# a = np.array([[1,2,3],[4,5,6]])
# print(a.shape)

# 调整数组大小
# a.shape=(3,2)
# print(a)
# b = a.reshape(3,2)
# print(b)

# 等间隔数字的数组
# a = np.arange(24)
# print(a)

# 一维数组
# a = np.arange(24)
# a.ndim
# 调整大小
# b = a.reshape(2,4,3)
# print(b)
# b现在拥有三个维度

# 数组的dtype为int8（一个字节）
# x = np.array([1,2,3,4,5],dtype=np.int8)
# print(x.itemsize)

#  数组的dtype为float32（四个字节）
# x = np.array([1,2,3,4,5],dtype=np.float32)
# print(x.itemsize)

# 展示当前的标志
# x = np.array([1,2,3,4,5])
# print(x.flags)

# 空数组
# x = np.empty([3,2],dtype=int)
# print(x)
#
# x = np.empty([3,2])
# print(x)

# 含有5个0的数组，默认类型是float
# x = np.zeros(5)
# print(x)

# x = np.zeros((5,),dtype=np.int)
# print(x)

# 自定义类型
# x = np.zeros((2,2),dtype=[('x','i4'),('y','i4')])
# print(x)

# x = np.zeros((2,3),dtype=[('x','i4'),('y','f4')])
# print(x)

# 含有5个1的数组，默认类型是float
# x = np.ones(5)
# print(x)

# x = np.ones([2,2],dtype=int)
# print(x)

# 将列表转换为ndarray
# x = [1,2,3]
# a = np.asarray(x)
# print(a) # [1 2 3]

# 设置了dtype
# x = [1,2,3]
# a = np.asarray(x,dtype=float)
# print(a) # [1. 2. 3.]

# 来自元组的ndarray
# x = (1,2,3)
# a = np.asarray(x)
# print(a) # [1 2 3]

# 来自元组列表的ndarray
# x = [(1,2,3),(4,5)]
# a = np.asarray(x)
# print(a) # [(1, 2, 3) (4, 5)]

# s = b'hello world'
# a = np.frombuffer(s,dtype='S1')
# print(a)

# 使用range函数创建列表对象
# list = range(5)
# print(list) # range(0, 5)

# 从列表中获得迭代器
# list = range(5)
# it = iter(list)
# # 使用迭代器创建ndarray
# x = np.fromiter(it,dtype=float)
# print(x) # [0. 1. 2. 3. 4.]

# x = np.arange(5)
# print(x) # [0 1 2 3 4]

# 设置dtype
# x = np.arange(5,dtype=float)
# print(x) # [0. 1. 2. 3. 4.]

# 设置了起始值和终止值参数
# x = np.arange(10,20,2)
# print(x) # [10 12 14 16 18]

# x = np.linspace(10,20,5)
# print(x) # [10.  12.5 15.  17.5 20. ]

# 将endpoint设为false
# x = np.linspace(10,20,5,endpoint=False)
# print(x) # [10. 12. 14. 16. 18.]

# # 输出retstep值
# x = np.linspace(1,2,5,retstep=True)
# print(x) # (array([1.  , 1.25, 1.5 , 1.75, 2.  ]), 0.25)

#  默认底数是10
# a = np.logspace(1.0,2.0,num=10)
# print(a)
# 输出：
# [ 10.          12.91549665  16.68100537  21.5443469   27.82559402
#   35.93813664  46.41588834  59.94842503  77.42636827 100.        ]

# 将对数空间底数设置为2
# a = np.logspace(1,10,num=10,base=2)
# print(a) # [   2.    4.    8.   16.   32.   64.  128.  256.  512. 1024.]

# a = np.arange(10)
# s = slice(2,7,2)
# print(a[s]) # [2 4 6]


# a = np.arange(10)
# b = a[2:7:2]
# print(b) # [2 4 6]
# 如果只输入一个参数，则返回与索引对应的单个项目。
# 如果使用a:,则从该索引向后的所有项目将被提取。
# 如果使用两个参数（以：分隔），则对两个索引（不包括停止索引）之间的元素以默认步骤进行切片。

# 对单个元素进行切片
# a = np.arange(10)
# b = a[5]
# print(b) # 5

# 对始于索引的元素进行切片
# a = np.arange(10)
# print(a[2:]) # [2 3 4 5 6 7 8 9]

# 对索引之间的元素进行切片
# a = np.arange(10)
# print(a[2:5]) # [2 3 4]

# 多维ndarray
# a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# print(a)
# 输出：
# [[1 2 3]
#  [3 4 5]
#  [4 5 6]]
# 对始于索引的元素进行切片
# print(a[1:])
# 输出：
# [[3 4 5]
#  [4 5 6]]
# 切片可以包括省略号（...),来使选择元组的长度与数组的维度相同。
# 如果在行位置使用省略号，将返回包含行中元素的ndarray
# 返回第二列元素的数组
# print(a[...,1]) # [2 4 5]
# 从第二行切片所有元素
# print(a[1,...]) # [3 4 5]
# 从第二列向后切片所有元素
# print(a[...,1:])
# 输出：
# [[2 3]
#  [4 5]
#  [5 6]]

# 获取ndarray对象中每一行指定列的一个元素，行索引包含所有行号，列索引指定要选择的元素
# x = np.array([[1,2],[3,4],[5,6]])
# y = x[[0,1,2],[0,1,0]]
# print(y) # [1 4 5]
# 结果包括数组中（0，0），（1，1）和（2，0）位置处的元素

# 获取4*3数组中每个角处的元素，行索引是[0,0]和[3,3]，而列索引是[0,2]和[0,2]
# x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
# rows = np.array([[0,0],[3,3]])
# cols = np.array([[0,2],[0,2]])
# y = x[rows,cols]
# print(y)
# 输出结果：
# [[ 0  2]
#  [ 9 11]]

# 高级和基本索引可以通过使用切片：或省略号...与索引数组组合
# 使用slice作为列索引和高级索引，当切片用于两者时，结果相同
# 但高级索引会导致复制，并且可能有不同的内存布局
# x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
# # 切片
# z = x[1:4,1:3]
# print(z)
# 输出结果：
# [[ 4  5]
#  [ 7  8]
#  [10 11]]
# 对列使用高级索引
# y = x[1:4,[1,2]]
# print(y)
# 输出结果：
# [[ 4  5]
#  [ 7  8]
#  [10 11]]

###############################################################
# 大于5的元素作为布尔索引的结果返回
# x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
# print(x[x>5]) # [ 6  7  8  9 10 11]

#  使用~（取补运算符）过滤NaN
# a = np.array([np.nan,1,2,np.nan,3,4,5])
# print(a[~np.isnan(a)]) # [1. 2. 3. 4. 5.]

# 从数组中过滤掉非复数元素
# a = np.array([1,2+6j,5,3.5+5j])
# print(a[np.iscomplex(a)]) # [2. +6.j 3.5+5.j]

#################################################################
# a = np.array([1,2,3,4])
# b = np.array([10,20,30,40])
# c = a * b
# print(c) # [ 10  40  90 160]

# a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])
# b = np.array([1.0,2.0,3.0])
# print(a+b)
# 输出结果：
# [[ 1.  2.  3.]
#  [11. 12. 13.]
#  [21. 22. 23.]
#  [31. 32. 33.]]

#############################################################################
# 使用arange函数创建一个3*4数组，并使用nditer对它进行迭代
# a = np.arange(0,60,5)
# a = a.reshape(3,4)
# print(a)
# 输出结果：
# [[ 0 5 10 15]
#  [20 25 30 35]
#  [40 45 50 55]]
# for x in np.nditer(a):
#     print(x)
# 输出结果：
# 0
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50
# 55

# 迭代的顺序匹配数组的内容布局，而不考虑特定的排序
# a = np.arange(0,60,5)
# a = a.reshape(3,4)
# b = a.T # 转置
# for x in np.nditer(b):
#     print(x)
# 输出结果：
# 0
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50
# 55

# 如果相同元素使用F风格顺序存储，则迭代器选择以更有效的方式对数组进行迭代。
# a = np.arange(0,60,5)
# a = a.reshape(3,4)
# b = a.T
# c = b.copy(order='C')
# for x in np.nditer(c):
#     print(x)
# 输出结果：
# 0
# 20
# 40
# 5
# 25
# 45
# 10
# 30
# 50
# 15
# 35
# 55
# c = b.copy(order='F')
# for x in np.nditer(c):
#     print(x)
# 输出结果：
# 0
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50
# 55

# 通过显式提醒强制nditer对象使用某种顺序
# a = np.arange(0,60,5)
# a = a.reshape(3,4)
# for x in np.nditer(a,order='F'):
#     print(x)
# 输出结果：
# 0
# 20
# 40
# 5
# 25
# 45
# 10
# 30
# 50
# 15
# 35
# 55

# 可选参数op_flags，其默认值为只读，但可以设置为读写或只写模式，可使用此迭代器修改数组元素
# a = np.arange(0,60,5)
# a = a.reshape(3,4)
# for x in np.nditer(a,op_flags=['readwrite']):
#     x[...]=2*x
# print(a)
# 输出结果：
# [[  0  10  20  30]
#  [ 40  50  60  70]
#  [ 80  90 100 110]]

# 外部循环
# nditer类的构造器拥有flags参数，它可以接受下列值：
# c_index 跟踪C顺序的索引
# f_index 跟踪Fortran顺序的索引
# multi-index 每次迭代可以跟踪一种索引类型
# external_loop 给出的值是具有多个值的一维数组，而不是零维数组
# 迭代器遍历对应于每列的一维数组
# a = np.arange(0,60,5)
# a = a.reshape(3,4)
# for x in np.nditer(a,flags = ['external_loop'],order='F'):
#     print(x)
# 输出结果：
# [ 0 20 40]
# [ 5 25 45]
# [10 30 50]
# [15 35 55]

# 广播迭代
# 如果两个数组是可广播的，nditer组合对象能够同时迭代它们
# 假设数组a具有维度3*4，并且存在维度为1*4的另一个数组b，则使用以下类型的迭代器（数组b被广播到a的大小）
# a = np.arange(0,60,5)
# a = a.reshape(3,4)
# b = np.array([1,2,3,4],dtype=int)
# for x,y in np.nditer([a,b]):
#     print("%d:%d"%(x,y))
# 输出结果：
# 0:1
# 5:2
# 10:3
# 15:4
# 20:1
# 25:2
# 30:3
# 35:4
# 40:1
# 45:2
# 50:3
# 55:4

#####################################数组操作###############################################
# 修改形状
# reshape 不改变数据的条件下修改形状
# flat 数组上的一维迭代器
# flatten 返回折叠为一维的数组副本
# ravel 返回连续的展开数组

##################numpy.reshape#######################
# numpy.reshape(arr,newshape,order)
#  arr:要修改形状的数组
#  newshape：整数或者整数数组，新的形状应当兼容原有形状
#  order：'C'为C风格顺序，'F'为F风格顺序，'A'为保留原顺序
# a = np.arange(8)
# b = a.reshape(4,2)
# print(b)
# 输出结果：
# [[0 1]
#  [2 3]
#  [4 5]
#  [6 7]]

##################numpy.ndarray.flat#######################
# 返回数组上的一维迭代器，行为类似Python内建的迭代器
# a = np.arange(8).reshape(2,4)
# 返回展开数组中下标的对应元素
# print(a.flat[5])  # 5

##################numpy.ndarray.flatten#######################
# 返回折叠为一维的数组副本
# ndarray.flatten(order)
# order: 'C'按行，'F'按列，'A'原顺序，'k'元素在内存中的出现顺序
a = np.arange(8).reshape(2,4)
# 默认按行
# print(a.flatten()) # [0 1 2 3 4 5 6 7]
# print(a.flatten(order='F')) # [0 4 1 5 2 6 3 7]

##################numpy.ravel#######################
# 返回展开的一维数组，并按需生产副本，返回的数组和输入数组拥有相同数据类型
# numpy.ravel(a,order)
# order: 'C'按行，'F'按列，'A'原顺序，'k'元素在内存中的出现顺序
# a = np.arange(8).reshape(2,4)
# print(a.ravel()) # [0 1 2 3 4 5 6 7]
# print(a.ravel(order='F')) # [0 4 1 5 2 6 3 7]

# 翻转操作
# transport 翻转数组的维度
# ndarray.T 和 self.transpose()相同
# rollaxis 向后滚动指定的轴
# swapaxes 互换数组的两个轴

##################numpy.transport#######################
# 翻转给定数组的维度，如果可能的话会返回一个视图
# numpy.transpose(arr,axes)
# arr：要转置的数组
# axes：整数的列表，对应维度，通常所有维度都会翻转
# a = np.arange(12).reshape(3,4)
# print(np.transpose(a))
# 输出结果：
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]

##################numpy.ndarray.T#######################
# 该函数属于ndarray类i，行为类似于numpy.transpose
# a = np.arange(12).reshape(3,4)
# print(a.T)
# 输出结果：
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]

##################numpy.rollaxis#######################
# 该函数向后滚动特定的轴，直到一个特定位置
# numpy.rollaxis(arr,axis,start)
# arr:输入数组
# axis：要向后滚动的轴，其他轴的相对位置不会改变
# start：默认为零，表示完整的滚动，会滚动到特定位置
# a = np.arange(8).reshape(2,2,2)
# print(a)
# 输出结果：
# [[[0 1]
#   [2 3]]
#
#  [[4 5]
#   [6 7]]]
# 将轴2滚动到轴0（宽度到深度）
# print(np.rollaxis(a,2))
# 输出结果：
# [[[0 2]
#   [4 6]]
#
#  [[1 3]
#   [5 7]]]
# 将轴2滚动到轴1（宽度到高度）
# print(np.rollaxis(a,2,1))
# 输出结果：
# [[[0 2]
#   [1 3]]
#
#  [[4 6]
#   [5 7]]]
# print(np.rollaxis(a,1))
# 输出结果：
# [[[0 1]
#   [4 5]]
#
#  [[2 3]
#   [6 7]]]
## 推测：
## 1. 只能从高维向低维转，从低维向高维转不变
## 2. 最高维是单个元素，标量组成的，将其一个一个放到低维中去
## 3. 次高维是数组，以数组为整体放到低维中去

##################numpy.swapaxis#######################
# 交换数组的两个轴，1.10之前版本的NumPy版本会返回交换后数组的视图。
# numpy.swapaxes(arr,axis1,axis2)
# arr:要交换其轴的输入数组
# axis1：对应第一个轴的整数
# axis2：对应第二个轴的整数
# a = np.arange(8).reshape(2,2,2)
# print(np.swapaxes(a,2,0))
# 输出结果：
# [[[0 4]
#   [2 6]]
#
#  [[1 5]
#   [3 7]]]
# print(np.swapaxes(a,0,1))
# 输出结果：
# [[[0 1]
#   [4 5]]
#
#  [[2 3]
#   [6 7]]]

# 修改维度
# broadcast：产生模仿广播的对象
# broadcast_to:将数组广播到新形状
# expand_dims：扩展数组的形状
# squeeze：从数组的形状中删除单维条目
##################broadcast#######################
# 返回一个对象，该对象封装了将一个数组广播到另一个数组的结果
# x = np.array([[1],[2],[3]])
# y = np.array([4,5,6])
# 对y广播x
# b = np.broadcast(x,y)
# 它拥有iterator属性，基于自身组件的迭代器元组
# r,c = b.iters
# print(r.next(),c.next()) # AttributeError: 'numpy.flatiter' object has no attribute 'next'
# print(r.next(),c.next())
# print(next(r),next(c)) # 1 4
# print(next(r),next(c)) # 1 5
# shape属性返回广播对象的形状
# print(b.shape) # (3, 3)
# 手动使用broadcast将x与y相加
# b = np.broadcast(x,y)
# c = np.empty(b.shape)
# print(c.shape) # (3, 3)
# c.flat = [u+v for (u,v) in b]
# print(c)
# 输出结果：
# [[5. 6. 7.]
#  [6. 7. 8.]
#  [7. 8. 9.]]
# print(x+y)
# 输出结果：
# [[5 6 7]
#  [6 7 8]
#  [7 8 9]]

##################numpy.broadcast_to#######################
# 将数组广播到新形状，在原始数组上返回只读视图，通常不连续
# 如果新形状不符合NumPy的广播规则，该函数可能会抛出ValueError
# numpy.broadcast_to(array,shape,subok)
# a = np.arange(4).reshape(1,4)
# print(a) # [[0 1 2 3]]
# print(np.broadcast_to(a,(4,4)))
# 输出：
# [[0 1 2 3]
#  [0 1 2 3]
#  [0 1 2 3]
#  [0 1 2 3]]

##################numpy.expand_dims#######################
# 通过在指定位置插入新的轴来扩展数组形状
# numpy.expand_dims(arr,axis)
# arr:输入数组
# axis：新轴插入的位置
# x = np.array(([1,2],[3,4]))
# print(x)
# 输出结果：
# [[1 2]
#  [3 4]]
# y = np.expand_dims(x,axis=0)
# print(y)
# 输出结果：
# [[[1 2]
#   [3 4]]]
# print(x.shape,y.shape) # (2, 2) (1, 2, 2)
# 在位置1插入轴
# y = np.expand_dims(x,axis=1)
# print(y)
# 输出结果:
# [[[1 2]]
#
#  [[3 4]]]
# print(x.ndim,y.ndim) # 2 3
# print(x.shape,y.shape) # (2, 2) (2, 1, 2)
# a = np.array([[1,2],[2,3],[4,5]])
# print(a.shape) # (3, 2)
# a = np.array([[[1,2],[2,3],[4,5]]])
# print(a.shape) # (1, 3, 2)
# a = np.array([[[1,2]],[[4,5]]])
# print(a.shape) # (2, 1, 2)

##################numpy.squeeze#######################
# 从给定数组的形状中删除一维条目
# numpy.squeeze(arr,axis)
# arr:输入数组
# axis：整数或整数元组，用于选择形状中单一维度条目的子集
# x = np.arange(9).reshape(1,3,3)
# print(x)
# 输出结果：
# [[[0 1 2]
#   [3 4 5]
#   [6 7 8]]]
# y = np.squeeze(x)
# print(y)
# 输出结果
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
# print(x.shape,y.shape) # (1, 3, 3) (3, 3)

# 数组的连接
# concatenate 沿着现存的轴连接数据序列
# stack 沿着新轴连接数组序列
# hstack 水平堆叠序列中的数组（列方向）
# vstack 竖直堆叠序列中的数组（行方向）

##################numpy.concatenate#######################
# 数组的连接，用于沿指定轴连接相同形状的两个或多个数组
# numpy.concatenate((a1,a2,...),axis)
# a1,a2,...：相同类型的数组序列
# axis：沿着它连接数组的轴，默认为0
# a = np.array([[1,2],[3,4]])
# print(a)
# 输出结果：
# [[1 2]
#  [3 4]]
# b = np.array([[5,6],[7,8]])
# print(b)
# 输出结果：
# [[5 6]
#  [7 8]]
# 两个数组的维度相同
# 沿轴0连接两个数组
# print(np.concatenate((a,b)))
# 输出结果：
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
# 沿着轴1连接两个数组
# print(np.concatenate((a,b),axis=1))
# 输出结果：
# [[1 2 5 6]
#  [3 4 7 8]]

##################numpy.stack#######################
# 沿着新轴连接数组序列
# numpy.stack(arrays,axis)
# arrays:相同形状的数组序列
# axis：返回数组中的轴，输入数组沿着它来堆叠
# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# 沿着轴0堆叠两个数组
# print(np.stack((a,b),0))
# 输出结果：
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]
# 沿着轴1堆叠两个数组
# print(np.stack((a,b),1))
# 输出：
# [[[1 2]
#   [5 6]]
#
#  [[3 4]
#   [7 8]]]

##################numpy.hstack#######################
# numpy.stack函数的变体，通过堆叠生成水平的单个数组
# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# 水平堆叠
# print(np.hstack((a,b)))
# 输出结果：
# [[1 2 5 6]
#  [3 4 7 8]]

##################numpy.vstack#######################
# numpy.stack函数的变体，通过堆叠生成竖直的单个数组
# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# print(np.vstack((a,b)))
# 输出结果：
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# 数组分割
# split 将一个数组分割为多个子数组
# hsplit 将一个数组水平分割为多个子数组（按列）
# vsplit 将一个数组竖直分割为多个子数组（按行）

##################numpy.split#######################
# 沿特定的轴将数组分割为子数组
# numpy.split(ary,indices_or_sections,axis)
# ary：被分割的输入数组
# indices_or_sections：可以是整数，表明要从输入数组创建的，等大小的子数组的数量，
# 如果此参数是一位数组，则其元素表明要创建新子数组的点
# axis：默认为0
# a = np.arange(9)
# 将数组分为三个大小相等的子数组
# b = np.split(a,3)
# print(b) # [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
# 将数组在一维数组中表明的位置分割
# print(np.split(a,[4,7])) # [array([0, 1, 2, 3]), array([4, 5, 6]), array([7, 8])]

##################numpy.hsplit#######################
# numpy.hsplit是split的特例，轴为1表示水平分割，无论输入数组的维度是什么
# a = np.arange(16).reshape(4,4)
# 水平分割
# print(np.hsplit(a,2))
# 输出结果：
# [array([[ 0,  1],
#        [ 4,  5],
#        [ 8,  9],
#        [12, 13]]), array([[ 2,  3],
#        [ 6,  7],
#        [10, 11],
#        [14, 15]])]

##################numpy.split#######################
# numpy.vsplit是split的特例，轴为0表示水平分割，无论输入数组的维度是什么
# a = np.arange(16).reshape(4,4)
# 竖直分割
# print(np.vsplit(a,2))
# 输出结果：
# [array([[0, 1, 2, 3],
#        [4, 5, 6, 7]]), array([[ 8,  9, 10, 11],
#        [12, 13, 14, 15]])]

# 添加/删除元素
# resize 返回指定形状的新数组
# append 将值添加到数组末尾
# insert 沿指定轴将值插入到指定下表之前
# delete 返回删掉某个轴的子数组的新数组
# unique 寻找数组内的唯一元素
##################numpy.resize#######################
# 返回指定大小的新数组，如果新大小大于原始大小，则包含原始数组中的元素的重复副本
# numpy.resize(arr,shape)
# arr:要修改大小的输入数组
# shape：返回数组的新形状
# a = np.array([[1,2,3],[4,5,6]])
# print(a.shape) # (2, 3)
# print(np.resize(a,(3,2)))
# 输出结果：
# [[1 2]
#  [3 4]
#  [5 6]]
# print(np.resize(a,(3,3)))
# 输出结果：
# [[1 2 3]
#  [4 5 6]
#  [1 2 3]]

##################numpy.append#######################
# 在输入数组的末尾添加值，附加操作不是原地的，而是分配新的数组
# 输入数组的维度必须匹配，否则ValueError
# numpy.append(arr,values,axis)
# arr:输入数组
# values：要向arr添加的值，比如和arr形状相同（除了要添加的轴）
# axis：沿着它完成操作的轴，如果没有提供，两个参数都会被展开
# a = np.array([[1,2,3],[4,5,6]])
# print(np.append(a,[7,8,9])) # [1 2 3 4 5 6 7 8 9]
# print(np.append(a,[[7,8,9]],axis=0))
# 输出结果：
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# print(np.append(a,[[5,5,5],[7,8,9]],axis=1))
# 输出结果：
# [[1 2 3 5 5 5]
#  [4 5 6 7 8 9]]

##################numpy.insert#######################
# 在给定索引之前，沿着给定轴在输入数组中插入值
# 如果值的类型转换为要插入，则它与输入数组不同
# 插入没有原地的，函数会返回一个新数组
# 如果未提供轴，输入数组会被展开
# numpy.insert(arr,obj,values,axis)
# arr:输入数组
# obj:在其之前插入值的索引
# values：要插入的值
# axis:沿着它插入的轴，如果未提供，则shrubs数组会被展开
# a = np.array([[1,2],[3,4],[5,6]])
# 未传递axis参数，在插入之前输入数组会被展开
# print(np.insert(a,3,[11,12])) # [ 1  2  3 11 12  4  5  6]
# 沿轴0广播
# print(np.insert(a,1,[11],axis=0))
# 输出结果：
# [[ 1  2]
#  [11 11]
#  [ 3  4]
#  [ 5  6]]
# 沿轴1广播
# print(np.insert(a,1,11,axis=1))
# 输出结果：
# [[ 1 11  2]
#  [ 3 11  4]
#  [ 5 11  6]]

##################numpy.delete#######################
# 返回从输入数组中删除指定子数组的新数组，
# 和insert一样，如果未提供轴参数，则输入数组将展开
# numpy.delete(arr,obj.axis)
# arr:输入数组
# obj:可以被切片，整数或整数数组，表明要从输入数组删除的子数组
# axis：沿着它删除给定子数组的轴，如果未提供，则输入数组会被展开
# a = np.arange(12).reshape(3,4)
# print(np.delete(a,5)) # [ 0  1  2  3  4  6  7  8  9 10 11]
# print(np.delete(a,1,axis=1))
# 输出结果：
# [[ 0  2  3]
#  [ 4  6  7]
#  [ 8 10 11]]
# a = np.array([1,2,3,4,5,6,7,8,9,10])
# print(np.delete(a,np.s_[::2])) # [ 2  4  6  8 10]

##################numpy.unique#######################
# 返回输入数组中的去重元素数组，
# 能够返回一个元组，包含去重数组和相关索引的数组
# 索引的性质取决于函数调用中返回参数的类型
# numpy.unique(arr,return_index,return_inverse,return_counts)
# arr：输入数组，如果不是一维数组则会展开
# return_index：如果为true，返回输入数组中的元素下标
# return_inverse:如果为true，返回去重数组的下标，它可以用于重构输入数组
# return_counts:如果为true，返回去重数组中的元素在原数组中的出现次数
# a = np.array([5,2,6,2,7,5,6,8,2,9])
# print(np.unique(a)) # [2 5 6 7 8 9]
# 去重数组的索引数组
# u,indices = np.unique(a,return_index=True)
# print(indices) # [1 0 2 4 7 9]
# 去重数组的下标
# u,indices = np.unique(a,return_inverse=True)
# print(indices)# [1 0 2 0 3 1 2 4 0 5]
# 使用下标重构原数组
# print(u[indices])#[5 2 6 2 7 5 6 8 2 9]
#返回去重元素的重复数量
# u,indices = np.unique(a,return_counts=True)
# print(u)#[2 5 6 7 8 9]
# print(indices)#[3 2 2 1 1 1]

###################################位操作#########################################
# NumPy包中可用的位操作函数
# bitwise_and 对数组元素执行位与操作
# bitwise_or 对数组元素执行或操作
# invert 计算位非
# left_shift 向左移动二进制表示的位
# right_shift 向右移动二进制表示的位

#################bitwise_and##################
# 对输入数组中的整数的二进制表示的相应位执行位与运算
# a,b = 13,17
# print(bin(a),bin(b)) #0b1101 0b10001
# print(np.bitwise_and(a,b)) # 1

#################bitwise_or###################
# 对输入数组中的整数的二进制表示的相应位执行位或运算
# a,b = 13,17
# print(np.bitwise_or(a,b)) # 29

#################invert###################
# 计算数组中整数的位非结果，对于有符号整数，返回补码
# print(np.invert(np.array([13],dtype=np.uint8))) # [242]
# print(np.binary_repr(13,width=8))# 00001101
# print(np.binary_repr(242,width=8))#11110010
# np.binary_repr函数返回给定宽度中十进制数的二进制表示

#################left_shift###################
# numpy.left_shift()函数将数组元素的二进制表示中的位向左移动到指定位置，右侧附加相等数量的0
# print(np.left_shift(10,2))# 40
# print(np.binary_repr(10,width=8)) #00001010
# print(np.binary_repr(40,width=8)) #00101000

#################right_shift###################
# numpy.right_shift()函数将数组元素的二进制表示中的位向右移动到指定位置，左侧附加相等数量的0
# print(np.right_shift(40,2)) # 10
# print(np.binary_repr(40,width=8))#00101000
# print(np.binary_repr(10,width=8))#00001010

####################################字符串函数##################################################
# 用于对dtype为numpy.string_或numpy.unicode_的数组执行向量化字符串操作
# 它们基于Python内置库中的标准字符串函数
# add 返回两个str或unicode数组的逐个字符串连接
# multiply 返回按元素多重连接后的字符串
# center 返回给定字符串的副本，其中元素位于特定字符串的中央
# capitalize 返回给定字符串的副本，其中只有第一个字符串大写
# title 返回字符串或unicode的按元素标题转换版本
# lower 返回一个数组，其元素转换为小写
# upper 返回一个数组，其元素转换为大写
# aplit 返回字符串中的单词列表，并使用分隔符来分割
# splitlines 返回元素中的行列表，以换行符分割
# strip 返回数组副本，其中元素移除了开头或者结尾处的特定字符
# join 返回一个字符串，它是序列中字符串的连接
# replace 返回字符串的副本，其中所有子字符串的出现位置都被新字符串取代
# decode 按元素调用str.decode
# encode 按元素调用str.encode
####这些函数在字符数组类(numpy.char)中定义
####numpy.char类中的上述函数在执行向量化字符串操作时非常有用

###########################numpy.char.add##############################
# 函数执行按元素的字符串连接
# print(np.char.add(['hello'],[' zbl'])) #['hello zbl']
# print(np.char.add(['hello','hi'],[' abc', ' xyz']))#['hello abc' 'hi xyz']

###########################numpy.char.multiply##############################
# 执行多重连接
# print(np.char.multiply('Hello ',3)) # Hello Hello Hello

###########################numpy.char.center##############################
# 返回所需宽度的数组，以便输入字符串位于中心，并使用fillchar在左侧和右侧进行填充
# print(np.char.center('hello',20,fillchar='*')) # *******hello********

###########################numpy.char.capitalize##############################
# 函数返回字符串的副本，其中第一个字母大写
# print(np.char.capitalize('hello world')) # Hello world

###########################numpy.char.title##############################
# 返回输入字符串的按元素标题转换版本，其中每个单词的首字母都大写
# print(np.char.title('hello how are you?')) #Hello How Are You?

###########################numpy.char.lower##############################
# 函数返回一个数组，其元素转换为小写，它对每个元素调用str.lower
# print(np.char.lower(['HELLO','WORLD'])) # ['hello' 'world']
# print(np.char.lower("HELLO")) # hello

###########################numpy.char.upper##############################
# 函数返回一个数组，其元素转换为大写，它对每个元素调用str.upper
# print(np.char.upper('hello')) # HELLO
# print(np.char.upper(['hello','world'])) # ['HELLO' 'WORLD']

###########################numpy.char.split##############################
# 此函数返回输入字符串中的单词列表，默认情况下，空格用作分隔符，否则，指定的分隔符用于分割字符串
# print(np.char.split('hello how are you?')) #['hello', 'how', 'are', 'you?']
# print(np.char.split('yiibaipoint,hyderabda,telangana',sep=',')) # ['yiibaipoint', 'hyderabda', 'telangana']

###########################numpy.char.splitlines##############################
# 函数返回数组中元素的单词列表，以换行符分割
# print(np.char.splitlines('hello\nhow are you?')) #['hello', 'how are you?']
# print(np.char.splitlines('hello\rhow are you?')) # ['hello', 'how are you?']
# '\n','\r','\r\n'都会用作换行符

###########################numpy.char.strip##############################
# 函数返回数组的副本，其中元素移除了开头或结尾处的特定字符
# print(np.char.strip('ashok arora','a')) # shok aror
# print(np.char.strip(['arora','admin','java'],'a')) # ['ror' 'dmin' 'jav']

###########################numpy.char.join##############################
# 返回一个字符串，其中单个字符由特定的分隔符连接
# print(np.char.join(':','dmy')) # d:m:y
# print(np.char.join([':','-'],['dmy','ymd'])) # ['d:m:y' 'y-m-d']

###########################numpy.char.replace##############################
# 返回字符串副本，其中所有字符序列的出现位置都被另一个给定的字符序列取代
# print(np.char.replace('He is a good boy','is','was')) #He was a good boy

###########################numpy.char.decode##############################
# 在给定的字符串中使用特定编码调用str.decode
# a = np.char.encode('hello','cp500')
# print(a) # b'\x88\x85\x93\x93\x96'
# print(np.char.decode(a,'cp500')) # hello

###########################numpy.char.encode##############################
# 对数组中的每个元素调用str.encode函数，默认编码是utf-8,可以使用标准Python库中的编解码器
# a = np.char.encode('hello','cp500')
# print(a) # b'\x88\x85\x93\x93\x96'

#######################################算数##########################################################
# NumPy包含大量的各种数学运算功能，
# NumPy提供标准的三角函数，算术运算的函数，复数处理函数等
# # 三角函数
# NumPy拥有标准的三角函数，它为弧度制单位的给定角度返回三角函数比值
# a = np.array([0,30,45,60,90])
# 通过乘pi/180转化为弧度
# print(np.sin(a*np.pi/180)) # [0.         0.5        0.70710678 0.8660254  1.        ]
# print(np.cos(a*np.pi/180)) # [1.00000000e+00 8.66025404e-01 7.07106781e-01 5.00000000e-01 6.12323400e-17]
# print(np.tan(a*np.pi/180)) # [0.00000000e+00 5.77350269e-01 1.00000000e+00 1.73205081e+00 1.63312394e+16]

# arcsin,arccos和arctan函数返回给定角度是sin，cos和tan的反三角函数，
# 这些函数的结果可以通过numpy.degrees函数通过将弧度制转换为角度制来验证
a = np.array([0,30,45,60,90])
inv = np.arcsin(np.sin(a*np.pi/180))
# print(inv) # [0.         0.52359878 0.78539816 1.04719755 1.57079633]
# print(np.degrees(inv)) # [ 0. 30. 45. 60. 90.]
# print(np.degrees(np.arccos(np.cos(a*np.pi/180)))) # [ 0. 30. 45. 60. 90.]
# print(np.degrees(np.arctan(np.tan(a*np.pi/180)))) # [ 0. 30. 45. 60. 90.]

## 舍入函数
# numpy.around
# 返回四舍五入到所需精度的值
# numpy.around(a,decimals)
# a:输入数组
# decimals：要舍入的小数位数，默认为0，如果为负，整数将四舍五入到小数点左侧的位置
# a = np.array([1.0,5.55,123,0.567,25.532])
# print(a) # [  1.      5.55  123.      0.567  25.532]
# print(np.around(a)) # [  1.   6. 123.   1.  26.]
# print(np.around(a,decimals=1)) # [  1.    5.6 123.    0.6  25.5]
# print(np.around(a,decimals=-1)) # [  0.  10. 120.   0.  30.]

# numpy.floor
# 返回不大于输入参数的最大整数，
# 即标量x的下限是最大的整数i，使得i<=x
# 在Python中，向下取整总是从0舍入
# a = np.array([-1.7,1.5,-0.2,0.6,10])
# print(np.floor(a)) #[-2.  1. -1.  0. 10.]

# numpy.ceil
# 返回输入值的上限，即，标量x的上限是最小的整数i，使得i>=x
# a = np.array([-1.7,1.5,-0.2,0.6,10])
# print(np.ceil(a)) # [-1.  2. -0.  1. 10.]

# 用于执行算术运算（如add，subtract，multiply和divide）的输入数组必须具有相同的形状或符合数组广播规则
# a = np.arange(9,dtype=np.float_).reshape(3,3)
# print(a)
# 输出结果：
# [[0. 1. 2.]
#  [3. 4. 5.]
#  [6. 7. 8.]]
# b = np.array([10,10,10])
# print(b)
# 输出结果：
# [10 10 10]
# print(np.add(a,b))
# 输出结果：
# [[10. 11. 12.]
#  [13. 14. 15.]
#  [16. 17. 18.]]
# print(np.subtract(a,b))
# 输出结果：
# [[-10.  -9.  -8.]
#  [ -7.  -6.  -5.]
#  [ -4.  -3.  -2.]]
# print(np.multiply(a,b))
# 输出结果：
# [[ 0. 10. 20.]
#  [30. 40. 50.]
#  [60. 70. 80.]]
# print(np.divide(a,b))
# 输出结果：
# [[0.  0.1 0.2]
#  [0.3 0.4 0.5]
#  [0.6 0.7 0.8]]

# numpy.reciprocal
# 返回参数逐元素的倒数，
# 由于python处理整数除法的时候，对于绝对值大于1的整数元素，结果时钟为0
# 对于整数0，则发出溢出警告
# a = np.array([0.25,1.33,1,0,100])
# print(np.reciprocal(a))
# 输出结果：
# RuntimeWarning: divide by zero encountered in reciprocal
#   print(np.reciprocal(a))
# [4.        0.7518797 1.              inf 0.01     ]
# b = np.array([100],dtype=int)
# print(b) # [100]
# print(np.reciprocal(b)) # 0

# numpy.power
# 将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂
# a = np.array([10,100,1000])
# print(np.power(a,2))# [    100   10000 1000000]
# b = np.array([1,2,3])
# print(np.power(a,b))#[        10      10000 1000000000]

# numpy.mod
# 返回输入数组中相应元素的除法余数，
# 函数numpy.remainder也产生相同的结果
# a = np.array([10,20,30])
# b = np.array([3,5,7])
# print(np.mod(a,b)) # [1 0 2]
# print(np.remainder(a,b)) # [1 0 2]

# 对含有复数的数组进行操作的函数
# numpy.real 返回复数类型参数的实部
# numpy.imag 返回复数类型参数的虚部
# numpy.conj 返回通过改变虚部的符号而获得的共轭复数
# numpy.angle 返回复数参数的角度，参数是degree，如果为true，返回角度制的角度，否则返回弧度制
# a = np.array([-5.6j,0.2j,11.,1+1j])
# print(np.real(a)) # [-0.  0. 11.  1.]
# print(np.imag(a)) # [-5.6  0.2  0.   1. ]
# print(np.conj(a)) # [-0.+5.6j  0.-0.2j 11.-0.j   1.-1.j ]
# print(np.angle(a)) # [-1.57079633  1.57079633  0.          0.78539816]
# print(np.angle(a,deg=True)) # [-90.  90.   0.  45.]

########################################统计函数##################################################
# NumPy的统计函数用于从数组中给定的元素中查找最小，最大，百分标准差和方差等
# numpy.amin和numpy.amax
# 从给定数组中的元素沿指定轴返回最小值和最大值
# a = np.array([[3,7,5],[8,4,3],[2,4,9]])
# print(np.amin(a,1)) # [3 3 2]
# print(np.amin(a,0)) # [2 4 3]
# print(np.amax(a)) # 9
# print(np.amax(a,axis=0)) # [8 7 9]

# numpy.ptp
# 返回沿轴的值的范围（最大值-最小值）
# a = np.array([[3,7,5],[8,4,3],[2,4,9]])
# print(np.ptp(a)) # 7
# print(np.ptp(a,axis=1)) # [4 5 7]
# print(np.ptp(a,axis=0)) # [6 3 6]

# numpy.percentile
# 百分位数是统计中使用的度量，表示小于这个值得观察值占某个百分比
# 计算分位数，50代表中位数
# numpy.percentile(a,q,axis)
# a:输入数组
# q：要计算的百分位数，在0~100之间
# axis：沿着它计算百分位数的轴
# a = np.array([[30,40,70],[80,20,10],[50,90,60]])
# print(np.percentile(a,50)) # 50.0
# print(np.percentile(a,50,axis=1)) # [40. 20. 60.]
# print(np.percentile(a,50,axis=0)) # [50. 40. 60.]

# numpy.median
# 中值，定义为将数据样本的上半部分与下半部分分开的值
# a = np.array([[30,65,70],[80,95,10],[50,90,60]])
# print(np.median(a)) # 65.0
# print(np.median(a,axis=0)) # [50. 90. 60.]
# print(np.median(a,axis=1)) # [65. 80. 60.]

# numpy.mean
# 算术平均值，沿轴的元素的总和除以元素的数量
# numpy.mean函数返回数组中元素的算术平均值
# 如果提供了轴，则沿轴计算
# a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# print(np.mean(a)) # 3.6666666666666665
# print(np.mean(a,axis=0)) # [2.66666667 3.66666667 4.66666667]
# print(np.mean(a,axis=1)) # [2. 4. 5.]

# numpy.average
# 加权平均值，由每个分量乘以反映其重要性的因子得到的平均值，
# 该函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值，
# 该函数可以接受一个轴参数，如果没有指定轴，则数组会被展开
# 例子：
#     数组[1,2,3,4]和相应的权重[4,3,2,1]
#     通过将相应元素的乘积相加，并将和除以权重的和，计算出加权平均值
# a = np.array([1,2,3,4])
# 不指定权重时相当于mean函数
# print(np.average(a)) # 2.5
# wts = np.array([4,3,2,1])
# print(np.average(a,weights=wts)) # 2.0
# # returned 为true则返回权重的和
# print(np.average([1,2,3,4],weights=[4,3,2,1],returned = True)) # (2.0, 10.0)

# a = np.arange(6).reshape(3,2)
# print(a)
# 输出结果：
# [[0 1]
#  [2 3]
#  [4 5]]
# wt = np.array([3,5])
# print(np.average(a,axis=1,weights=wt)) # [0.625 2.625 4.625]
# print(np.average(a,axis=1,weights=wt,returned=True)) # (array([0.625, 2.625, 4.625]), array([8., 8., 8.]))

# 标准差
# 标准差是与均值的偏差的平方的平均值的平方根
# 公式： std = sqrt(mean((x-x.mean())^2)
# print(np.std([1,2,3,4])) # 1.118033988749895

# 方差
# 偏差的平方的平均值，标准差是方差的平方根
# print(np.var([1,2,3,4])) #1.25

######################################排序、搜索和计数########################################
# quicksor 快速排序 速度最快 最坏情况O(n^2)  工作空间0 不稳定
# mergesort 归并排序 速度居中 最坏情况O(n*log(n)) 工作空间~n/2 稳定
# heapsort 堆排序  速度最慢 最坏情况O(n*log(n)) 工作空间0 不稳定
##################numpy.sort###################
# 返回输入数组的排序副本
# numpy.sort(a,axis,kind,order)
# a 要排序的数组
# axis 沿着它排序数组的轴，如果没有，数组会被展开，沿着最后的轴排序
# kind 默认为'quicksort'
# order 如果数组包含字段，则是要排序的字段
# a = np.array([[3,7],[9,1]])
# print(np.sort(a))
# 输出结果：
# [[3 7]
#  [1 9]]
# 沿轴0排序
# print(np.sort(a,axis=0))
# 输出结果：
# [[3 1]
#  [9 7]]
# 在sort函数中加入排序字段
# dt = np.dtype([('name','S10'),('age',int)])
# a = np.array([("raju",21),("anil",25),("ravi",17),("amar",27)],dtype=dt)
# 按name排序
# print(np.sort(a,order='name')) # [(b'amar', 27) (b'anil', 25) (b'raju', 21) (b'ravi', 17)]

#########################numpy.argsort#############################
# 对输入数组沿给定轴执行间接排序，并使用指定排序类型返回数据的索引数组
# 索引数组用于构造排序后的数组
# x = np.array([3,1,2])
# y = np.argsort(x)
# print(y) # [1 2 0]
# print(x[y]) # [1 2 3]

###########################numpy.lexsort###############################
# 使用键序列执行间接排序
# 键可以看作是电子表格中的一列
# 函数返回一个索引数组，使用它可以获得排序数据
# 最后一个键恰好是sort的主键
# nm = ('raju','anil','ravi','amar')
# dv = ('f.y.','s.y.','s.y.','f.y.')
# ind = np.lexsort((dv,nm))
# print(ind) # [3 1 0 2]
# 使用索引获取排序后的数据
# print([nm[i]+","+dv[i] for i in ind]) # ['amar,f.y.', 'anil,s.y.', 'raju,f.y.', 'ravi,s.y.']
# ind2 = np.lexsort((nm,dv))
# print(ind2) #[3 0 1 2]

##############################numpy.argmax和numpy.argmin############################
# 分别返回沿给定轴返回最大和最小元素的索引
# a = np.array([[30,40,70],[80,20,10],[50,90,60]])
# print(np.argmax(a)) #7
# 展开数组
# print(a.flatten()) # [30 40 70 80 20 10 50 90 60]
# maxindex = np.argmax(a,axis = 0)
# print(maxindex) # [1 2 0]
# maxindex1 = np.argmax(a,axis=1)
# print(maxindex1) # [2 0 1]
# minindex = np.argmin(a)
# print(minindex) # 5
# print(a.flatten()[minindex]) #10
# minindex0 = np.argmin(a,axis=0)
# print(minindex0) # [0 1 1]
# minindex1 = np.argmin(a,axis=1)
# print(minindex1) # [0 2 0]

###############################numpy.nonzero################################
# 返回输入数组中非零元素的索引
# a = np.array([[30,40,0],[0,20,10],[50,0,60]])
# print(np.nonzero(a)) # (array([0, 0, 1, 1, 2, 2], dtype=int32), array([0, 1, 1, 2, 0, 2], dtype=int32))

#################################numpy.where#################################
# 返回输入数组中满足给定条件的元素的索引
# x = np.arange(9.).reshape(3,3)
# y = np.where(x>3)
# print(y) # (array([1, 1, 2, 2, 2], dtype=int32), array([1, 2, 0, 1, 2], dtype=int32))
# print(x[y]) # [4. 5. 6. 7. 8.]

###################################numpy.extract#############################
# 返回满足任何条件的元素
# x = np.arange(9.).reshape(3,3)
# 定义条件
# condition = np.mod(x,2) == 0
# print(condition)
# 输出结果：
# [[ True False  True]
#  [False  True False]
#  [ True False  True]]
# print(np.extract(condition,x)) # [0. 2. 4. 6. 8.]

###############################################字节交换########################################
# 存储在计算机内存中的数据取决于CPU使用的架构
# 它可以是小端（最小有效位存储在最小地址中）或大端（最小有效位存储在最大地址中）
#####################numpy.ndarray.byteswap############################
# 在大端和小端之间切换
# a = np.array([1,256,8755],dtype = np.int16)
# print(a) #[   1  256 8755]
# 以十六进制表示内存中的数据
# print(map(hex,a)) # <map object at 0x00FABA50>
# print(["%x"%i for i in a]) #['1', '100', '2233']
# byteswap函数通过传入true来原地交换
# print(a.byteswap(True)) #[  256     1 13090]
# print(map(hex,a)) #<map object at 0x01295610>
# print(["%x"%i for i in a]) #['100', '1', '3322']

#############################################副本和视图################################################
# 执行函数时，其中一些返回输入数组的副本，另一些返回视图
# 当内容物理存储在另一个位置时，称为副本
# 如果提供了相同内存内容的不同视图，就是视图
#### 无复制
# 简单的赋值不会创建数组对象的副本，而是使用原始数组的相同id来访问
# id函数返回python对象的通用标识符，类似于c中的指针
# 一个数组的任何变化都反映在另一个数组上，
# 例如，一个数组的形状改变也会改变另一个数组的形状
# a = np.arange(6)
# print(a) #[0 1 2 3 4 5]
# print(id(a)) # 38005560
# b = a
# print(id(b)) # 38005560
# b.shape = 3,2
# print(b)
# 输出结果：
# [[0 1]
#  [2 3]
#  [4 5]]
# print(a)
# 输出结果：
# [[0 1]
#  [2 3]
#  [4 5]]

###### 视图或浅复制
# ndarray.view函数是一个新的数组对象，并可查看原始数组的相同数据
# 新数组的维数更改不会更改原始数组的维数
# a = np.arange(6).reshape(3,2)
# print(a)
# 输出结果：
# [[0 1]
#  [2 3]
#  [4 5]]
# b = a.view()
# print(b)
# 输出结果：
# [[0 1]
#  [2 3]
#  [4 5]]
# print(id(a)) # 44561776
# print(id(b)) # 44562216
# 修改b的形状，并不会修改a
# b.shape = 2,3
# print(b.shape) #(2, 3)
# print(a.shape) #(3, 2)

####数组的切片会创建视图
# a = np.array([[10,10],[2,3],[4,5]])
# print(a)
# 输出结果：
# [[10 10]
#  [ 2  3]
#  [ 4  5]]
# s = a[:,:2]
# print(s)
# 输出结果：
# [[10 10]
#  [ 2  3]
#  [ 4  5]]

#########深拷贝
# ndarray.copy函数创建一个深层副本，它是数组及其数据的完整副本，不与原始数组共享
# a = np.array([[10,10],[2,3],[4,5]])
# print(a)
# 输出结果：
# [[10 10]
#  [ 2  3]
#  [ 4  5]]
# b = a.copy()
# print(b)
# 输出结果：
# [[10 10]
#  [ 2  3]
#  [ 4  5]]
# b与a不共享任何内容
# print(b is a) #False
# b[0,0] = 100
# print(b)
# 输出结果：
# [[100 10]
#  [ 2  3]
#  [ 4  5]]
# print(a)
# 输出结果：
# [[10 10]
#  [ 2  3]
#  [ 4  5]]

##########################################矩阵库######################################
# Matrix库numply.matlib
# 函数返回矩阵
#####################matlib.empty###########################
# 返回一个新的矩阵，而不初始化元素
# numpy.matlib.empty(shape,dtype,order)
# shape 定义新矩阵形状的整数或整数元组
# dtype 可选，输出的数据类型
# order C或者F
import numpy.matlib
# 填充为随机数
# print(np.matlib.empty((2,2)))
# 输出结果：
# [[2.12199579e-314 6.36598737e-314]
#  [1.06099790e-313 1.48539705e-313]]

###################numpy.matlib.zeros#############################
# 返回以零填充的矩阵
# print(np.matlib.zeros((2,2)))
# 输出结果：
# [[0. 0.]
#  [0. 0.]]

###################numpy.matlib.ones#############################
# 返回以一填充的矩阵
# print(np.matlib.ones((2,2)))
# 输出结果：
# [[1. 1.]
#  [1. 1.]]

###################numpy.matlib.eye#############################
# 返回一个矩阵，对角线元素为1，其他位置为零
# numpy.matlib.eye(n,M.k,dtype)
# n 返回矩阵的行数
# M 返回矩阵的列数，默认为n
# k 对角线的索引
# dtype 输出的数据类型
# print(np.matlib.eye(n=3,M=4,k=0,dtype=float))
# 输出结果：
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]]
# print(np.matlib.eye(n=3,M=4,k=1,dtype=float))
# 输出结果：
# [[0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

###################numpy.matlib.identity#############################
# 返回给定大小的单位矩阵，单位矩阵是主对角线元素都为1的方阵
# numpy.matlib.identity(n,dtype)
# n 方阵的行数（或列数）
# dtype 输出的数据类型
# print(np.matlib.identity(5,dtype=float))
# 输出结果：
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

###################numpy.matlib.rand#############################
# 返回给定大小的填充随机值的矩阵
# print(np.matlib.rand(3,3))
# 输出结果：
# [[0.90796277 0.33481028 0.6857256 ]
#  [0.30574222 0.01042222 0.33451347]
#  [0.15845694 0.35361556 0.41205505]]
# 矩阵总是二维的，而ndarray是一个n维数组，两个对象可以互换
# i = np.matrix('1,2;3,4')
# print(i)
# 输出结果：
# [[1 2]
#  [3 4]]
# j = np.asarray(i)
# print(j)
# 输出结果：
# [[1 2]
#  [3 4]]
# k = np.asmatrix(j)
# print(k)
# 输出结果：
# [[1 2]
#  [3 4]]

###########################################线性代数############################################
# numpy包包含numpy.linalg模块，提供线性代数所需的所有功能
# dot 表示两个数组的点积
# vdot 两个向量的点积
# inner 两个数组的内积
# matul 两个数组的矩阵积
# determinant 数组的行列式
# solve 求解线性矩阵方程
# inv 寻找矩阵的乘法逆矩阵

########################numpy.dot#########################
# 返回两个数组的点积
# 对于二维向量，其等效于矩阵乘法
# 对于一维数组，它是向量的内积
# 对于N维数组，它是a的最后一个轴上的和与b的倒数第二个轴的乘积
# a = np.array([[1,2],[3,4]])
# b = np.array([[11,12],[13,14]])
# print(np.dot(a,b))
# 输出结果：
# [[37 40]
#  [85 92]]

########################numpy.vdot#############################
# 返回两个向量的点积
# 如果第一个参数是复数，那么用它的共轭复数计算
# 如果参数id是多维数组，它会被展开
# a = np.array([[1,2],[3,4]])
# b = np.array([[11,12],[13,14]])
# print(np.vdot(a,b))#130

############################numpy.inner#############################
# 返回一维数组的向量内积
# 对于更高的维度，返回最后一个轴上的和的乘积
# print(np.inner(np.array([1,2,3]),np.array([0,1,0]))) # 2
# 多维数组的情况
# a = np.array([[1,2],[3,4]])
# b = np.array([[11,12],[13,14]])
# print(np.inner(a,b))
# 输出结果：
# [[35 41]
#  [81 95]]

############################numpy.matmul##############################
# 返回两个数组的矩阵乘积
# 虽然它返回二维数组的正常乘积，但如果任一参数的维度大于2，
# 则将其视为存在于最后两个索引的矩阵的栈，并进行相应广播
# 如果任一参数是一维数组，则通过在其维度上附加1来将其提升为矩阵，并在乘法之后被去除
# 对于二维数组，就是矩阵乘法
# a = [[1,0],[0,1]]
# b = [[4,1],[2,2]]
# print(np.matmul(a,b))
# 输出结果：
# [[4 1]
#  [2 2]]
# 二维和一维运算
# a = [[3,0],[1,4]]
# b = [1,2]
# print(np.matmul(a,b)) # [3 9]
# 计算方法：
# a'= a.
# b'=[[1,2],[1,1]]
# a'与b'相乘，去除副对角线上的值即得
# print(np.matmul(b,a)) # [5 8]
# 维度大于二的数组
# a = np.arange(8).reshape(2,2,2)
# b = np.arange(4).reshape(2,2)
# print(np.matmul(a,b))
# 输出结果：
# [[[ 2  3]
#   [ 6 11]]
#
#  [[10 19]
#   [14 27]]]

################################numpy.linalg.det##########################
# 计算输入矩阵的行列式
# a = np.array([[1,2],[3,4]])
# print(np.linalg.det(a)) #-2.0000000000000004

##########################numpy.linalg.solve############################
# 给出矩阵形式的线性方程的解
# a = np.array([[1,1,1],[0,2,5],[2,5,-1]])
# b = np.array([6,-4,27])
# print(np.linalg.solve(a,b)) #[ 5.  3. -2.]

##########################numpy.linalg.inv###############################
# 计算矩阵的逆
# 矩阵的逆乘以原始矩阵，得到单位矩阵
# x = np.array([[1,2],[3,4]])
# y = np.linalg.inv(x)
# print(np.dot(x,y))
# 计算结果
# [[1.0000000e+00 0.0000000e+00]
#  [8.8817842e-16 1.0000000e+00]]

##########################################Matplotlib库###############################################
# matplotlib是python的绘图库，可与Numpy一起使用
# 也可以和图形工具包一起使用，如PyQt和wxPython
from matplotlib import pyplot as plt
# pyplot用于绘制2D数据
# 绘制y = 2*x+5
# x = np.arange(1,11)
# y = 2* x+5
# plt.title("demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x,y)
# plt.show()
# 可以向plot函数添加格式字符串显示离散值，
# 可以使用以下格式化字符
# '-' 实线
# '--' 短横线
# '-.' 点划线
# ':' 虚线
# '.' 点标记
# ',' 像素标记
# 'o' 圆标记
# 'v' 倒三角标记
# '^' 正三角标记
# '&lt;' 左三角标记
# '&rt;' 右三角标记
# '1' 下箭头标记
# '2' 上箭头标记
# '3' 左箭头标记
# '4' 右箭头标记
# 's' 正方形标记
# 'p' 五边形标记
# '*' 星形标记
# 'h' 六边形标记1
# 'H' 六边形标记2
# '+' 加号标记
# 'x' X标记
# 'D' 菱形标记
# 'd' 窄菱形标记
# '&#124;' 竖直线标记
# '_' 水平线标记

## 颜色
# 'r' 红色
# 'g' 绿色
# 'b' 蓝色
# 'c' 青色
# 'm' 品红色
# 'y' 黄色
# 'k' 黑色
# 'w' 白色

# plt.plot(x,y,'ob')
# plt.show()

# 正弦波图
# x = np.arange(0,3*np.pi,0.1)
# y = np.sin(x)
# plt.title('sine wave form')
# plt.plot(x,y)
# plt.show()

# ###########################subplot####################
# 可在同一图中绘制不同的东西
# 绘制正弦和余弦值
# x = np.arange(0,3*np.pi,0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
# plt.subplot(2,1,1)
# plt.plot(x,y_sin)
# plt.title('Sine')
# plt.subplot(2,1,2)
# plt.plot(x,y_cos)
# plt.title('Cosine')
# plt.show()

###################bar##########################
# 生成条形图
# x = [5,8,10]
# y = [12,16,6]
# x2 = [6,9,11]
# y2 = [6,15,7]
# plt.bar(x,y,align='center')
# plt.bar(x2,y2,color='g',align='center')
# plt.title('Bar graph')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.show()

###########################histogram################################
# 是数据的频率分布的图形表示
# 水平尺寸相等的矩形对应于类间隔，称为bin，变量height对应于频率
# histogram函数将输入数组和bin作为两个参数，bin数组中的连续元素用作每个bin的边界
# a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
# np.histogram(a,bins=[0,20,40,60,80,100])
# hist,bins = np.histogram(a,bins=[0,20,40,60,80,100])
# print(hist) #[3 4 5 2 1]
# print(bins) #[  0  20  40  60  80 100]
################################plt#################################
# matplotlib可以将直方图的数字表示转换为图形
# pyplot子模块的plt函数将包含数据和bin数组的数组作为参数，并转换为直方图
# plt.hist(a,bins=[0,20,40,60,80,100])
# plt.title("histogram")
# plt.show()

###########################################I/O文件操作############################################
# ndarray对象可以保存到磁盘文件并从磁盘文件加载
# load和save函数处理numpy二进制文件（带npy扩展名）
# loadtxt和savetxt函数处理正常的文本文件
# numpy为ndarray对象引入了一个简单的文件格式，
# 这个npy文件在磁盘文件中，存储重建ndarray所需的数据、图形、dtype和其他信息，
# 以便正确获取数组，即使该文件在具有不同架构的另一台机器上
#######################numpy.save######################
# 文件将输入数组存储在具有npy扩展名的磁盘文件中
# a = np.array([1,2,3,4,5])
# np.save('outfile',a)
# b = np.load('outfile.npy')
# print(b) #[1 2 3 4 5]

# save和load函数接受一个附加的布尔参数allow_pickles
# python中的pickle用于在保存到磁盘文件或从磁盘文件读取之前，对对象进行序列化和反序列化。
#########################savetxt###################
# 以简单文本文件格式存储和获取数组数据，通过savetxt和loadtxt完成
# a = np.array([1,2,3,4,5])
# np.savetxt('out.txt',a)
# b = np.loadtxt('out.txt')
# print(b) # [1. 2. 3. 4. 5.]
# savetxt和loadtxt函数接收附加的可选参数，如页首，页尾和分隔符