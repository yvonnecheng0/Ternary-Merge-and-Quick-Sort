""""
Module will be able to divide lists into two or three sublists and sort them back together using merge or quick sort. 
Yvonne Cheng 
csci 112
Winter, 2023
""" 
import random 

#Taken from textbook
def mergeSortBinary(alist):
    #If length of list is > 1, not sorted. Split list in half 
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        #Recursively left and right hlaf of list
        mergeSortBinary(lefthalf)
        mergeSortBinary(righthalf)

        #Initialize i,j,k variables to track current index on left and right half of list.
        #K used to track current index in merged list
        i= j = k = 0

        #Compare values on left and right half of list and place in merged list in ascending order. Continue until all items in left or right half is added to merged list
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        #Copy remaining elements of left half in the merged list if any are left
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        #Copy remaining elements of right half in the merged list if any are left
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def mergeSortTernary(alist):
    #Base case, if only one or no element in list, return list 
    if len(alist) <= 1:
        return alist
    
    #Use insertion sort for small sublists
    if len(alist) < 50:
        for i in range(1, len(alist)):
            index = alist[i]
            j = i-1
            while j >=0 and index < alist[j] :
                    alist[j+1] = alist[j]
                    j -= 1
            alist[j+1] = index
        return alist
    
    #Split list into three parts
    m1 = len(alist) // 3
    m2 = 2 * len(alist) // 3
    
    left = mergeSortTernary(alist[:m1])
    middle = mergeSortTernary(alist[m1:m2])
    right = mergeSortTernary(alist[m2:])
    
    #Merge the three parts
    return left, middle, right

#Taken from textbook 
def quickSortBinary(alist):
    #Call quickSortHelper to sort unsorted list 
   quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist,first,last):
   #If sublist has more than one element, partitions sublist using partition function
     if first<last:
        splitpoint = partition(alist,first,last)
        #Recursively call quickSortHelper on two resulting sublists
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   #Set pivot value to first element in list 
   pivotvalue = alist[first]

   #Set left and right mark
   leftmark = first+1
   rightmark = last

   done = False
   while not done:
       #Move leftmark to the right until it finds an element > pivot value
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       #Move rightmark to the left until it find an element < pivot value 
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       
       #If rightmark < leftmark, loop terminates
       if rightmark < leftmark:
           done = True
       #Swap pivot value with the value at rightmark
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   #Return index of pivot value to split the list into two sub-lists
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark

def quickSortTernary(alist):
    #If only one or no element in list, return list 
    if len(alist) <= 1:
        return alist
    
    #Use insertion sort for small sublists
    if len(alist) < 50:
        for i in range(1, len(alist)):
            index = alist[i]
            j = i-1
            while j >=0 and index < alist[j] :
                    alist[j+1] = alist[j]
                    j -= 1
            alist[j+1] = index
        return alist
    
    #Choose random pivot
    pivot_index = random.randint(0, len(alist) - 1)
    pivot = alist[pivot_index]
    
    #Split array into three parts
    left = []
    middle = []
    right = []
    
    for n in alist:
        if n < pivot:
            left.append(n)
        elif n == pivot:
            middle.append(n)
        else:
            right.append(n)
    
    #Recursively sort three parts
    return quickSortTernary(left) + middle + quickSortTernary(right)


if __name__ == "__main__":
    alist = [54,26,93,17,77,31,44,55,20]
    blist = [54,26,93,17,77,31,44,55,20]
    clist = [54,26,93,17,77,31,44,55,20]
    dlist = [54,26,93,17,77,31,44,55,20]
    quickSortBinary(alist) 
    print(alist)
    quickSortTernary(blist)
    print(blist)
    mergeSortBinary(clist)
    print(clist)
    mergeSortTernary(dlist)
    print(dlist)
