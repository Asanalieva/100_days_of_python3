#Али-Баба №759

lst = []

# number of elements as input
n = int(input("Enter number of elements :")) #NUMBER of Element

# iterating till the range
for i in range(0, n):
    ele = int(input())   #Input Values

    lst.append(ele)  # adding the element
    lst.sort()      #sorting


print(max(lst) + lst[-2]) #Max number + sorted 2nd max number