
"""
switch功能
"""


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

def asdf(value):
    for case in Switch(value):
        if case('one'):
            print("1")
            break
        if case('two'):
            print("2")
            break
        if case('ten'):
            print('10')
            return '10'
        if case('eleven'):
            print("11")
            break
        if case():  # default, could also just omit condition or 'if True'
            print("something else!")
        # No need to break here, it'll stop anyway


a = asdf('ten')
print("a:", a)
