class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
        
    # Add your code here
    def computeDifference(self):
        max_val = 1
        min_val = 100
        for i in self.__elements:
            if i > max_val:
                max_val = i
            elif i < min_val:
                min_val = i
        self.maximumDifference = abs(max_val - min_val)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
