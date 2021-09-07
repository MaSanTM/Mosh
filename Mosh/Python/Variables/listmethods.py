numbers = [5, 2, 1, 7, 2,4]
#numbers2 = numbers.copy()
#print (numbers2)

#mylist = ['a', 'b', 'c', 'c', 'b']
#mylist = list(dict.fromkeys(mylist))
#print(mylist)

uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)