Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
# Car speed, Hours traveled, and Distance
# 19 June 2021
# CTI-110 P2HW1 - DistanceTraveled
# Richard Edge
#
>>> 


#input use float
speed = float(input("Enter car's speed: \n"))

#input use float
time = float(input("Enter time traveled: \n"))

# distance = time * speed   
dist = speed * time;

#print speed convert to string
print("Speed entered: " + str(speed))
  
#print time convert to string
print("Time entered: " + str(time))

#print distance traveled after converting to string

print("\nDistance traveled " + str(dist) + " miles")


# user should enter cars speed and time using float and input.
# distance should be calculated accordingly
# speed and time should be converted into a string
# lastly distance traveled should equal distance + miles for the total
