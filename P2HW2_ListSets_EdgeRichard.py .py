Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
# CTI-110 
# P2HW2 - List and Sets 
# Richard Edge
# 20 June 2021
#
>>> 
#ask user to
print('Enter a series of 10 numbers')
#put input into list
numbers_list = list(map(int,input().split()))
#split() returns list of space seperated values
# map() is used to convert the string to integer 
#list() is used to convert map object to list 
#lowest number 
low = min(numbers_list)
#min() returns minimum of the list 
high = max(numbers_list)
#max() returns maximum of the list 
total = sum(numbers_list)
#sum() returns sum of all values in the list 
avg = total/len(numbers_list)
#len() returns length of the list
#show all the values 
print("Lowest number:",low)
print('Largest number:',high)
print('Total:',total)
print('Average:',avg)
#converting the list to a set 
numbers_set = set(numbers_list)
print('set content:',end=' ')
#displaying the set content 
for i in numbers_set:
    print(i,end=' ')

# user should enter series of 10 number into a list from lowest to highest
# numbers should be totaled
# the total of the numbers to be averaged into a set list
