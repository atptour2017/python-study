
def make_fabonacci():
        a=0
        b=1

        def fabonacci():
                nonlocal a,b
                b,a=a+b,b
                return a

        return fabonacci

fabonacci=make_fabonacci()
print(fabonacci())
print(fabonacci())
print(fabonacci())
print(fabonacci())
print(fabonacci())
print(fabonacci())
print(fabonacci())
print(fabonacci())
print(fabonacci())
print(fabonacci())