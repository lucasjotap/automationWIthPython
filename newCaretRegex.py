import re 

regex = re.compile(r'^Hello')
regex_two = re.compile(r'\d$')
match_object = regex.search("Hello World")
match_object_two = regex.search("She said hello.")
match_object_three = regex_two.search("Your number is 7")

print(match_object.group())
print(match_object_two == True)
print(match_object_three.group())
