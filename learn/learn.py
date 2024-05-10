import copy


def helloworld():
    print("hello world")


def listLearn():
    arr = [1, 2, 3, 4, 'list']
    for x in arr:
        print(x)
    print(len(arr))
    # 设置步长跳跃，负数的话就是倒着开始
    print(arr[::-2])
    return arr


def listOperation():
    arr = [1, 2, 3, 4, 'list']
    # 追加元素
    arr.append(5)
    # 插入元素
    arr.insert(1, 199)
    # 删除元素
    arr.remove('list')
    # 删除指定元素
    arr.pop(len(arr) - 1)
    # 添加一整个队列
    arr.extend(['蜘蛛侠', 'zk'])
    # 替换
    arr[0] = 'zk'
    arr[1:4] = ['zk1', 'zk2', 'zk3']
    # 排序
    inlist = [3, 1, 2, 3, 1, 2]
    inlist.sort(reverse=True)
    inlist.reverse()
    for x in inlist:
        print(x)
    # 获取元素数量
    inlist.count(3)
    # 获取元素索引值
    inlist.index(3)
    # 范围获取索引值
    inlist.index(1, 0, 3)
    # 复制列表
    nums = inlist.copy()

    # 列表加减乘除
    a = [1, 2, 3]
    b = [2, 3, 4]
    c = a + b
    d = a * 3
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in matrix:
        for e in i:
            print(e, end=" ")
        print()
    # 清空列表
    # arr.clear()
    # for x in arr:
    #    print(x)

    # 判断类型是否相同
    str1 = 'finsh1'
    str2 = 'finsh1'
    boo = str1 is str2
    print(boo)

    # 浅拷贝
    x = [1, 2, 3]
    y = x.copy()
    x[0] = 111

    # 深拷贝
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrixOne = copy.deepcopy(matrix)
    matrix[0][0] = 666
    print(matrix)
    print(matrixOne)

    # 列表推导式
    two = [i * 2 for i in a]
    for i in two:
        print(i)
    even = [i*2 for i in range(10) if i % 2 == 0]
    for i in even:
        print(i)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # 外层循环放前面，内层在外面，其实就是两层for循环
    flatten = [col for row in matrix for col in row]
    for i in even:
        print(i)


if __name__ == '__main__':
    listOperation()
