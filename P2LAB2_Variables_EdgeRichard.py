user_int = int(input('Enter integer (32 - 126):\n'))

# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
user_float = float(input('Enter float:\n'))   
# FIXME (2): Output the four values in reverse
user_char = input('Enter character:\n')  
# FIXME (3): Convert the integer to a characer, and output that character
user_str = input('Enter string:\n')

print("%d %.2f %s %s" % (user_int, user_float, user_char, user_str))
print("%s %s %.2f %d" % (user_str, user_char, user_float, user_int))
print('%d converted to a character is %s' % (user_int, chr(user_int)))