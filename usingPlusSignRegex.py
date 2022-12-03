import re

batRegex = re.compile(r'Bat(wo)+man')
matchObject = batRegex.search('The Adventures of Batwoman')
print(matchObject.group())

matchObjectTwo = batRegex.search('The Adventures of Batwowowowowowoman')
print(matchObjectTwo.group())

matchObjectThree = batRegex.search('The Adventures of Batman')

if matchObjectThree == None:
    print('None')
