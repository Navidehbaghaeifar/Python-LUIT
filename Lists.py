var = []

print(type(var)) # ====>we need validate list by this cmd==>output is:<class 'list'>

var2 = [151,251,386,493,649,'009'] #mixed data type list
print(var2)
var2.append(721)  # inplace add element
print(var2)
var2=var2 + [445]#non inplace add element
print(var2)


numbers=[1,2,3,4,5]
for number in numbers:
    print(number)
    
numbers2 = list(range(0,50))
print(numbers2)

for number in numbers2:
    print(numbers)
    
    
list_of_lists = [[0,1,2],[2,3,4],[4,5,6]]
print(list_of_lists)

for list_of_list in list_of_lists:
	     for element in list_of_list:
              print(element)