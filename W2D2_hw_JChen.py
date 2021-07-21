''' Exercise 1 '''
# Given list, write a function that returns a list of numbers that are less than ten
def less_ten_list(input_list):
    new_list = []
    for current_num in input_list:
        if current_num < 10:
            new_list.append(current_num)
    return new_list

l_1 = [1,11,14,5,8,9]
print(f'the numbers that are less than ten are {less_ten_list(l_1)}')




''' Excercise 2 '''
# Write a function that takes in two lists and returns the two lists merged together and sorted
def merge_sort(list1, list2):
    merged_sorted_list = list1 + list2
    merged_sorted_list.sort()
    return merged_sorted_list

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
print(f'the merged and sorted new list is {merge_sort(l_1, l_2)}')