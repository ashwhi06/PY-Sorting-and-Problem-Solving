# Write your solution for algorithm 3 below
#3. Write an algorithm that takes in an unsorted numerical list as an argument and creates a new sorted list in descending order (use the sorted() function).

#The sorted() function sorts in ascending order, but it can sort in descending order by adding a reverse parameter with a boolean value of True.
lst = [5, 10, 9, 7, 6, 12] #unsorted list
sorted_lst = sorted(lst, reverse = True) # sort in descending order
print(sorted_lst) #prints sorted list