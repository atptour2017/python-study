def deco(func):
    def wrapper():
        res = func()
        next(res)
        return res
    return wrapper

@deco
def foo():
    food_list = []
    while True:
        food = yield food_list  #返回添加food的列表
        food_list.append(food)
        print("elements in foodlist are:",food)

g = foo()
print(g.send('苹果'))
print(g.send('香蕉'))
print(g.send('菠萝'))