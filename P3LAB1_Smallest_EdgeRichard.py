#input in descending order
#n1=7
#n2=15
#n3=3
n1 = int(input())
n2 = int(input())
n3 = int(input())

smallest=n1
if n2<smallest:
    smallest = n2
if n3 < smallest:
    smallest = n3

print(smallest)