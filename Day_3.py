#Complex String Transformation

text = "ArtificialIntelligence"
print(text)
print(text[:7:1],text[8:15:1],text[15::1])
print(text[:7:1],text[-8:-15:-1],text[15::1])
print(text[15::1]+text[-8:-15:-1]+text[:7:1])
print(text[3::3])
print(text[-3::-3])



#Advanced List Block Manipulation

num=[12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50]
print(num)
num_1=num[:5:1],num[5:10:1],num[10:15:1],num[15:20:1]
print(num_1)
num_2=num[:5:1],num[-11:-16:-1],num[10:15:1],num[-1:-6:-1]
print(num_2)
num_3=list(num_2)
print(num_3)
num_4=num_3[-1],num_3[-2],num_3[-3],num_3[-4]
num_4=list(num_4)
print(num_4)
print(num_4[-4::1]+num_4[:-4:1])
print(num_4[3::1]+num_4[:3:1])
num_5=[1,2,3,4,5,6,7,8,9,10]
print(num_5)
print(num_5[1::2])
num_6=[11,12,13,14,15,16,17,18,19,20]
print(num_6)
print(num_6[2::2])
num_7=num_5[1::2]+num_6[2::2]
print(num_7)




#Nested Sequence Logic

data = ["Python", "Java", "C++", "JavaScript", "GoLang"]
print(data[-5],data[-1])
print(data[0][-1::-1],data[1][-1::-1],data[2][-1::-1],data[3][-1::-1],data[4][-1::-1])
print(data[0][:2:1],data[1][:2:1],data[2][:2:1],data[3][:2:1],data[4][:2:1])
print([data[0][:2:1],data[1][:2:1],data[2][:2:1],data[3][:2:1],data[4][:2:1]])
print([data[0][:-3:-1],data[1][:-3:-1],data[2][:-3:-1],data[3][:-3:-1],data[4][:-3:-1]])
rev_data=(data[0][-1::-1]+"|"+data[1][-1::-1]+"|"+data[2][-1::-1]+"|"+data[3][-1::-1]+"|"+data[4][-1::-1])
print(rev_data)
print(type(rev_data))




#Pattern Engineering (Logic Test)

value = "Sequence"
print(value)
value_1=value[::2]
print("Even -",value_1)
value_2=value[1::2]
print("Odd -",value_2)
print(value_2[-1::-1])