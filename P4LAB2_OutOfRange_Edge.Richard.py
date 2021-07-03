#start and end integers should be -15, and 10
start = int(input())
end = int(input())
if start > end:
    print("Second integer can't be less than the first.")
else:
    while start <= end:
        print(start, end=' ')
#increase the number count by 5
        start += 5 
    print()