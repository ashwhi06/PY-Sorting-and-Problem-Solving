# Write your solution for algorithm 5 below
# 5. Write an algorithm that takes in an unsorted integer array and finds a pair with a given sum.

# For example, for input: [5, 10, 4, 7, 6, 2] and target = 9, the output would be 7, 2.
# If there are no pairs with sum equal to the target number, then the output should be 'no pairs sum to the target'.
# If stuck, here are helpful steps for algorithm 5:

# Sort the list in ascending order.
# Set a variable called left equal to 0 and another variable called right equal to one less than the length of the list. These variables should be initially set to the indices for the first and last element in the list.
# Write a while loop that runs the following code when left is less than right.
# If the value of the element at index or left plus the value of the element at index or right equals the target number, then print the pair and return.
# If the sum of the two elements is less than the target number, then increment left by 1.
# Otherwise, increment right by 1.
# Print 'no pairs sum to the target' if no two numbers sum to the target number.

def find_pair(lst, target):
    sorted_lst = sorted(lst) # sort list in ascending order
    left = 0 # set left index to 0
    right = len(lst) - 1 # set right index to one less than the length of the list
    
    while left < right: # while left index is less than right index
        if sorted_lst[left] + sorted_lst[right] == target: # if the sum of the two elements at the left and right indices is equal to the target number
            return (sorted_lst[left], sorted_lst[right]) # print the pair and return
        
        if sorted_lst[left] + sorted_lst[right] < target: # if the sum of the two elements at the left and right indices is less than the target number
            left += 1 # increment left index by 1
        else:
            right -= 1 # increment right index by 1
        return("no pairs sum to the target")
    
sample_lst = [53, 100, 40, 75]
print(find_pair(sample_lst, 9))