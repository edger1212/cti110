#Use 5345 for input to get answer
def steps_to_miles(user_steps):
    return user_steps/2000

if __name__ == '__main__':
    steps = float(input())
    print('{:.2f}'.format(steps_to_miles(steps)))