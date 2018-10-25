


stp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print(tp1)
print(tp2)

li=list()
for i in tp:
		if tp[i]%2== 0:
			li.append(tp[i])

tp2=tuple(li)
print(tp2)
