class Person(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print("{}在跑....".format(self.name))
        return self

    def sing(self):
        print("{}在唱：燃烧我的卡路里！".format(self.name))


p1 = Person("沈腾")
# p1.run()
# p1.sing()

# 链式操作，本质上就是方法返回当前的实例对象
p1.run().sing()
