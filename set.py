# list1 = [10, 20, 30, 40, 50]
# list2 = [10, 20, 60, 70]

# num1 = set(list1)
# num2 = set(list2)

# print(num1 | num2)  # union
# print(num1 - num2)  # Difference
# print(num1 ^ num2)  # Symmetric Difference
# print(num1 & num2)  # And
# print(len(num1))

# list1 = [1, 2, 3, 4, 5, 6]
# s1 = {1, 2, 3, 4, 5, 6}

# s1.add(7)
# s1.update([8, 9, 10])
# s1.remove(10)
# s1.discard(9)

# print(s1)


set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2)
set5 = set1.difference(set3)
set6 = set1.intersection(set2)
set7 = set1.symmetric_difference(set3)

print(set4)
print(set5)
print(set6)
print(set7)
