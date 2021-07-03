#Program input= Listen, Mr. Jones, calm down.
user_text = input()
count = 0
#The count when the character is not an exclamation point, comma, period or space
for x in user_text:
    if not(x in " !,."):
# increase the number count by 1
        count += 1
#print the count       
print(count) 



