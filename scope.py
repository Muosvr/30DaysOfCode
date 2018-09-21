class Difference:
    def __init__(self, a):
        self.a = a
        self.maximumDifference = 0

    def computeDifference(self):
        self.a.sort()
        self.maximumDifference = a[len(a)-1] - a[0]


_ = input()
a = [int(e) for e in input().split(" ")]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
