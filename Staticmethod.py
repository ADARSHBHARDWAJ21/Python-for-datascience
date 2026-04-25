class math:
    @staticmethod # use to remove self
    def add(x,y):
        return x + y
    def multiply(x, y):
        return x * y
m = math()
print(m.add(3,4))

# code refactoring - it is a process of restructuring existing source code
# improving its internal structure , redablity, and maintainablity - without
#changing its external behaviour