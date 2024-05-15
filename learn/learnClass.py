class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def mul(self):
        return self.x * self.y


class Cson(C):
    def __init__(self, x, y, z):
        C.__init__(self, x, y)
        self.z = z

    # 方法重写
    def add(self):
        return C.add(self) + self.z


class Cat:
    def __init__(self, name):
        self.name = name

    def say(self):
        print(f"我是猫，我叫{self.name}")


class Dog:
    def __init__(self, name):
        self.name = name

    def say(self):
        print(f"我是狗，我叫{self.name}")


# 多态体现
# 鸭子模型鸭子模型（Duck Typing）是 Python 等动态类型语言中的一个概念。它强调的是对象的行为（方法和属性），而不是对象的实际类型。
# 鸭子模型的核心思想是："如果它像鸭子一样走路，像鸭子一样叫，那么它就是一只鸭子。"
#
# 在鸭子模型中，你不需要检查对象的类型，只需要确保对象具有你所期望的方法和属性即可。这种方法使代码更加灵活和可扩展，因为你可以传递任何具有所需行为的对象，而不必关心它们的具体类型。
def animal(x):
    x.say()


# 私有变量 单个下划线开头变量表示内部使用变量 单个下划线结尾的是Py自己的类
class Private:
    def __init__(self, x):
        self.__x = x

    def set__x(self, x):
        self.__x = x

    def get__x(self):
        return self.__x


# __slots__标识只能创建标明的属性，继承的类不会遵循父类slots
class Slot:
    __slots__ = ['__x']

    def __init__(self, x):
        self.__x = x

    def set__x(self, x):
        self.__x = x

    def get__x(self):
        return self.__x

    def __getattribute__(self, item):
        print("拿来")
        return super().__getattribute__(item)


class Xunhuan:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, item):
        return self.x[item], self.y[item]


# 重写iter方法标明这是一个可迭代对象，next来获取下一个参数
class Double:
    def __init__(self, start, end):
        self.value = start - 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.end:
            raise StopIteration
        self.value += 1
        return self.value * 2

    # 标识不使用这个方法
    __lt__ = None


class Cc:

    def __init__(self):
        self._x = 250

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    # 其实就是通过另一种方式管理私有变量
    x = property(getx, setx, delx)


# 这样就和上述类的property作用一样了
class Ccone:

    def __init__(self):
        self._x = 250

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

    @x.setter
    def x(self, value):
        self._x = value


# 类方法
class ClassMethod:
    count = 0

    def __init__(self):
        ClassMethod.count += 1

    @classmethod
    def funcB(cls):
        print(f"一共实例化了 {cls.count}个")


class StaticMethod:
    count = 0

    def __init__(self):
        StaticMethod.count += 1

    @staticmethod
    def funcB():
        print(f"一共实例化了 {StaticMethod.count}个")


# 描述符
class Miao:
    def __get__(self, instance, owner):
        return instance._x

    def __set__(self, instance, value):
        instance._x = value

    def __delete__(self, instance):
        del instance._x


class MiaoSon:
    x = Miao()

    def __init__(self, x=250):
        self._x = x


# 手动实现Property，描述符只能应用在类属性上，不能应用在对象属性上
class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)

    def getter(self, func):
        self.fget = func
        return self

    def setter(self, func):
        self.fset = func
        return self

    def deleter(self, func):
        self.fdel = func
        return self


class MyPropertySonOne:

    def __init__(self):
        self._x = 1000

    @MyProperty
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


class MyPropertySon:

    def __init__(self):
        self._x = 1000

    # 重写了这个方法之后，这个方法会在子类继承之后先行拦截类似类属性参数的赋值操作
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__()

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = MyProperty(getx, setx, delx)


# 钻石继承指的是一个类使得父类被初始化两次，使用super初始化上级可以解决super().init()

if __name__ == "__main__":
    c = C(2, 3)
    print(c.add())
    print(c.__dict__)

    d = Cson(2, 3, 4)
    print(d.add())
    print(d.__dict__)

    print(C.mro())
    print(C.__mro__)

    animal(Cat("咪咪"))

    e = Private(12)
    e.get__x()
    print(e.__dict__)

    # 判断是否有该属性
    print(hasattr(c, "x"))
    setattr(e, "_Private__x", 100)
    print(getattr(e, "_Private__x"))
    delattr(c, "x")

    z = Xunhuan([1, 2, 3], [6, 7, 8, 9])
    for x in z:
        print(x)

    dou = Double(1, 5)
    for i in dou:
        print(i)

    p = Ccone()
    p.x = 1000

    z = ClassMethod()
    p = ClassMethod()
    o = ClassMethod()
    print(ClassMethod.funcB())

    z1 = StaticMethod()
    p1 = StaticMethod()
    o1 = StaticMethod()
    print(StaticMethod.funcB())

    c = MiaoSon()
    c.x = 1000
    print(c.x)

    myPropertySon = MyPropertySonOne()
    print(myPropertySon.x)


    def pp(self,name):
        print(name)


    C = type('C', (), {})
    print(C.__bases__)
    D = type('D', (C,), dict(a=120, b=130, say_hi=pp))
    d = D()
    d.say_hi("nihao")
