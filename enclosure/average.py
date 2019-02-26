def make_average():
        series=[]

        def averager(new_value):
                series.append(new_value)
                total=sum(series)
                return total/len(series)

        return averager

average=make_average()
print(average(10))
print(average(11))
print(average(12))
