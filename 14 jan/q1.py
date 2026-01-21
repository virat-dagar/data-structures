
'''given an aray of integers, perform the following operations: reverse the array, find the max and minimum elememnts, calculate sum and average of the elements
implement function to perform each operation. ensure time complexity if optimal'''

a = [1, 2, 3, 4, 5]
a_rev = []
for i in range (len(a)):
    a_rev.append(a[len(a)-1-i])
print("Reversed array:", a_rev)


a_max = a[0]
for i in range (len(a)):
    if a[i]>a_max:
        a_max = a[i]
print("Maximum element:", a_max)


a_min = a[0]
for i in range (len(a)):
    if a[i]<a_min:
        a_min = a[i]
print("Minimum element:", a_min)


a_sum = 0
for i in range (len(a)):
    a_sum += a[i]
print("Sum of elements:", a_sum)


a_avg = a_sum/len(a)
print("Average of elements:", a_avg)
