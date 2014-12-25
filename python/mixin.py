# -*-  coding:utf-8  -*-

# 由于Python允许使用多重继承，因此，Mixin就是一种 常见的设计 。

# 只允许单一继承的语言（如Java）不能使用Mixin的设计。

class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def do(self):
        print('Running...')

class Flyable(object):
    def do(self):
        print('Flying...')

# 放在前面的覆盖后面的
class Dog(Mammal,Flyable, Runnable):
    pass

class Bat(Mammal, Flyable,Runnable):
    pass

d = Dog()
d.do()


