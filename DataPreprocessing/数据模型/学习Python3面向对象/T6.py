
"""
类的属性与方法
"""


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
print(counter.count())
print(counter.count())
print(counter.publicCount)
# print(counter.__secretcount)
