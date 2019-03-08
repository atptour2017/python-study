#yield from的使用

#从外部获取迭代对象，直接yield from
def g1(gen):
    yield from gen

#内部生成迭代对象，直接yield from
def g2():
	#a=range(5)
	a=[1,2,3,4,5]
	yield from a

if __name__=='__main__':
	g=g1(range(10))
	#g.send(None)
	for x in g:
		print(x)
	g.close()

	s=g2()
	#这里不能SEND NONE，否则第一个元素被忽略了
	#s.send(None)
	# for x in s:
	# 	print(x)