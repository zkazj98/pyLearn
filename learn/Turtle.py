import turtle


class Turtle:
    head = 1
    shenti = 2
    tui = 3
    # self其实就是当前对象实例,为什么用self呢，因为所有实例对象共享方法，要通过实例对象来建立一个绑定关系
    def sleep(self):
        print("我睡了两秒哈哈哈哈哈哈哈")

# 可以进行多重继承，访问顺序从左至右
class TurtleSon(Turtle):
    head = 10000
    def sleep(self):
        print("我是子类睡觉了")

class Dog:
    def say(self):
        print("汪汪汪")
class Cat:
    def say(self):
        print("喵喵喵")

class Garden:
    d=Dog()
    c=Cat()
    def say(self):
        self.d.say()
        self.c.say()

if __name__ == '__main__':
    t = TurtleSon()
    t.sleep()
    # 判断是否是这个类型
    print(isinstance(t,TurtleSon))
    # 判断是否是子类
    print(issubclass(Turtle,TurtleSon))
    print(issubclass(TurtleSon,Turtle))
    g = Garden()
    a = TurtleSon()
    print(g.say())
    g.x=10002
    print(g.__dict__)
    print(a.__dict__)
