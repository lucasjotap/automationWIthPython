import re

batRegex = re.compile(r'Bat(wo)?man')
matchObject = batRegex.search('The Adventures of Batman')
print(matchObject.group())

matchObjectTwo = batRegex.search('The Adventures of Batwoman')
print(matchObjectTwo.group())