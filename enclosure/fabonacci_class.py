class Fabonacci():
        def __init__(self):
                self.a=0
                self.b=1

        def __call__(self):
                self.b,self.a=self.a+self.b,self.b
                return self.a

f=Fabonacci()
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())