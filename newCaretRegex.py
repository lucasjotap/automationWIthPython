import re 

regex = re.compile(r'^Hello')
match_object = regex.search("Hello World")

print(match_object.group())