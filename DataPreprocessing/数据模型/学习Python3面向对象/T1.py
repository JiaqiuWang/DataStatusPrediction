"""
类对象
类对象支持两种操作：属性引用和实例化。
属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。
类对象创建后，类命名空间中所有的命名都是有效属性名。所以如果类定义是这样:
"""


class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'

# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类属性i为：", x.i)
print("MyClass类的方法f输出为：", x.f())










