协程
gen.py: 简单的yield from，可以直接从一个迭代对象，比如列表，返回单个迭代对象里的元素
yield_from_example.py: 主调用方将数据直接一个个通过委托生成器传入子生成器，子生成器计算结果后，再返回给yield from
yield_from_example2.py: 这里没有使用yield from语句，按照常规的方法去使用生成器，那么当send结束的时候，要写try except语句，虽然能达到效果，但是代码比较麻烦
不美观，所以yield from帮我们干了这些事，实现了这些逻辑，使我们不再需要写try语句去判断StopIteration异常。
gen1.py: 委托生成器和子生成器，实现返回值和主调用方传入值到子生成器
inspect_gen.py: 在send时，生成器的不同阶段检查状态
inspect_gen2.py: 在仅yield时，生成器的不同阶段的状态检查

sample2.py: 即send进生成器，又从生成器yield出来，这么个写法。即传入又返回就叫协程。即是生产者也是消费者。