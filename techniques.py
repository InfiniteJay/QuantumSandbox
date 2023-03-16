import sys
from numpy import sin

(walrus := True)  # returns True, assigns and evaluates

# useful for extracting and monitoring values from a function

# 3 sin (4x^2), p = 4x^2
x = 0.1
y = 3 * sin(p := 4 * x ** 2)

print("x: %s, y: %s" % (x, y))
print(f"x: {x}, y: {y}")

# f strings will use __str__ instead of __repr__
# use f"...!r" to force it to use __repr__

# iter creates a datastream iter(object, sentinel)
# sentinel is terminating value

nums = [1, 2, 3, 4, 5]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


class DataStore:
    def __init__(self, data):
        self.index = -1
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if (self.index == len(self.data) - 1):
            raise StopIteration
        self.index += 1
        return self.data[self.index]

    __call__ = __next__


ds = DataStore([1, 2, 3])
itr = iter(ds, 3)  # sentinel is 3, so it will stop when encounter 3

for i in itr:
    print(i)

# Generators are more efficient than iterators as they are dynamically generated

squres = (x * x for x in range(5))
print(next(squres))
print(next(squres))


def get_seq_upto(x):
    for i in range(x):
        yield i  # yield pauses execution and sends the value to the stream


evens = [x for x in range(100) if x % 2 == 0]
print(evens)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

nums = [(x,y) for x in nums1 for y in nums2]

