协程
gen.py: 简单的yield from，可以直接从一个迭代对象，比如列表，返回单个迭代对象里的元素
yield_from_example.py: 主调用方将数据直接一个个通过委托生成器传入子生成器，子生成器计算结果后，再返回给yield from
yield_from_example2.py: 这里没有使用yield from语句，按照常规的方法去使用生成器，那么当send结束的时候，要写try except语句，虽然能达到效果，但是代码比较麻烦
不美观，所以yield from帮我们干了这些事，实现了这些逻辑，使我们不再需要写try语句去判断StopIteration异常。