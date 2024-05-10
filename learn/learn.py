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
    even = [i * 2 for i in range(10) if i % 2 == 0]
    for i in even:
        print(i)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # 外层循环放前面，内层在外面，其实就是两层for循环
    flatten = [col for row in matrix for col in row]


def yuanLearn():
    rhyme = (1, 2, 3, 4, 5)
    print(rhyme[0:])
    yuan = (1,)
    type(yuan)
    a, b, c, d, e = rhyme


def slide():
    a = [1, 2, 3, 4]
    e = [1, 2, 3]
    b = (1, 2, 3, 4)
    c = list(a)
    d = tuple(a)
    min(d, default="没有最小")
    max(d, default="没有最大")
    sum(a)
    sum(a, start=0)
    e = ['a', 'das', 'dqwdqwd']
    sorted(e, key=len)  # 不改变原序列
    list(reversed(a))
    # 变成带序号的列表 可设置编号开始时间
    list(enumerate(a))
    # 拼接两个 变成[(1,1),(2,2)]这种,假设出现个数有区别的这里会变成取最小的
    # itertools可以不丢失
    import itertools
    list(zip(a, e))
    zipped = itertools.zip_longest(a, e)
    print(list(zipped))
    # map将后续参数使用前面函数处理,第一个每一位一次和后面对应的进行处理
    mapped = map(pow, [2, 3, 4], [3, 2, 3])
    print(list(mapped))
    # filter过滤器
    print(list(filter(str.islower, "FashjkFF")))
    # 迭代器和可迭代对象
    y = iter(a)
    next(y, "没了")


def ziDian():
    a = {"吕布": "扣扣布", "关羽": "关习习"}
    b = dict(吕布="扣扣布", 关羽="关习习")
    c = dict([("吕布", "扣扣布"), ("关羽", "关习习")])
    # fromkeys创建新字典，使用输入值做参数
    d = dict.fromkeys("Fish", 250)
    d['F'] = 666
    d.pop('F')
    # 移除最后一个元素
    d.popitem()
    del d['i']
    d.clear()
    d.update(a=100, b=30)
    d.update({"dasd": "dasd"})
    d.get("dad", "meiyou")
    d.setdefault('dasaa', "dasdasdaasdassda")
    print(d)
    print(d.get("dad", "meiyou"))
    keys = d.keys()
    values = d.values()
    items = d.items()
    print(keys)
    print(values)
    print(items)
    list(d)
    list(d.values())
    e = iter(d)
    next(e)
    # 字典推导式
    b = {v: k for k, v in d.items}


def jiHe():
    # 集合不重复但是无序，会去重
    a = set("Fish")
    a.update(set("666Java"))
    print(a)
    s = list([1, 1, 2, 2, 3, 4])
    print(len(s) == len(set(s)))
    # 判断两个set是否不相关
    print(a.isdisjoint(set("java")))
    # 判断是否是另一个集合子集
    print(a.issubset("Fish.com"))
    # 判断是否是另一个超集
    print(a.issubset("Fish"))
    # 并集,可多参数
    print(a.union("Fisheqweqw"))
    # 交集,可多参数
    print(a.intersection("Fisheqweqw"))
    # 差集,可多参数
    print(a.difference("Fisheqweqw"))
    # 对称差集
    print(a.symmetric_difference("Fisheqweqw"))
    # 判断子集
    print(a <= set("Fish"))
    # 判断超集
    print(a >= set("Fish"))
    # 并集
    print(a | {1, 2, 3})
    # 交集
    print(a & {1, 2, 3})
    # 差集
    print(a - set("Fs"))
    # 对称差集
    print(a ^ set("Fs"))

    # 不可变集合
    t = frozenset("Finc")
    # 移除 remove和discard  remove抛出异常 另一个静默处理
    t.remove("F")
    print(t)


if __name__ == '__main__':
    jiHe()
