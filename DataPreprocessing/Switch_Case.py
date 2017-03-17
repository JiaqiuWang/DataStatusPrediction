"""
最近在使用Python单元测试框架构思自动化测试，在不段的重构与修改中，发现了大量的if...
else之类的语法，有没有什么好的方式使Python具有C/C#/JAVA等的switch功能呢？
在不断的查找和试验中，发现了这个：http://c
ode.activestate.com/recipes/410692/，并在自己的代码中大量的应用，
哈哈，下面来看下吧：
"""
# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.


class Switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for
            self.fall = True
            return True
        else:
            return False


# The following example is pretty much the exact use-case of a dictionary,
# but is included for its simplicity. Note that you can include statements
# in each suite.

v = 'ten3'
for case in Switch(v):
    if case('one'):
        print("1")
        break
    if case('two'):
        print("2")
        break
    if case('ten'):
        print('10')
        break
    if case('eleven'):
        print("11")
        break
    if case():  # default, could also just omit condition or 'if True'
        print("something else!")
        # No need to break here, it'll stop anyway


















