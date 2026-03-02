a = 5
b = 15
s = 'cs111' 
s = s[:3]   # this is slicing the string to get the first 3 characters. The : is required to slice the string.
a = b // a
a = b / a   # this is a float division, which will give us a float result.
b = b % 4
s = s[::-1] # reverse the string. THE :: is required to reverse the string by slicing. 
            # The first : is for the start and the second : is for the step. the blanks assume 0
            # The -1 is for the step, which means to go backwards.
print(a, b, a + b, s)   