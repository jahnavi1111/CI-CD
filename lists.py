import os
List1 = [1,4,5,7,8,11]
List1.reverse()
print("The reversed list is", List1)

List2 = [10,99,34,76,27,101,23,67,35,35,79,210]
List2.sort()
print ("The sorted list is" , List2)

List3 = []
List3 = List1.copy()
print("List3 =", List3)

List4 = []
List4.append(7)
print("List4 =", List4)

List5 = [1, 2, 3]
List5.extend([4, 5])
print("List5 =", List5)

indexvalue = List2[2:6]
print("The index values are" , indexvalue)
