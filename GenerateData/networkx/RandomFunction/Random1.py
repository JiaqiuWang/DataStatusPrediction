import random
import itertools
import bisect

# random.randint(a, b),返回[a,b]之间的整数
print(random.randint(1, 2))

# random.randrange(start, stop[, step)，从指定范围内，按指定基数递增的
print(random.randrange(10, 100, 2))

"""random.choice(sequence)。
参数sequence表示一个有序类型。这里要说明一下：sequence在python不是一种特定的类型，
而是泛指一系列的类型。list, tuple, 字符串都属于sequence。"""
print(random.choice(["JGood", "is", "a", "handsome", "boy"]))
print(random.choice(("Tuple", "List", "Dict")))
print(random.choice("学习Python"))

# random.shuffle(x[, random])，用于将一个列表中的元素打乱
p = ["Python", "is", "powerful", "simple", "and so on..."]
random.shuffle(p)
print(p)

# random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
list_var = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice_var = random.sample(list_var, 5)
print("slice:", slice_var)

weight_choices = [('Red', 3), ("Blue", 2), ('Yellow', 1), ('Green', 4)]
population = [val for val, cnt in weight_choices for i in range(cnt)]
print("population:", population)
print("choice_population:", random.choice(population))
print("Sample_population:", random.sample(population, 3))

"""
A more general approach is to arrange the weights in a cumulative distribution with
 itertools.accumulate(), and then locate the random value with bisect.bisect():
"""
choices, weights = zip(*weight_choices)
print("choices, weights:", choices, weights)
cumdist = list(itertools.accumulate(weights))
print("cumdist:", cumdist)
x = random.random() * cumdist[-1]
print("x:", x)
print("", choices[bisect.bisect(cumdist, x)])

