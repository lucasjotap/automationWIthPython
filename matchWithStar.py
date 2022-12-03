import re

batRegex = re.compile(r'Bat(wo)*man')
matchObject = batRegex.search('The Adventures of Batman')
print(matchObject.group())

matchObjectTwo = batRegex.search('The adventures of Batwoman')
print(matchObjectTwo.group())

matchObjectThree = batRegex.search('The adventures of Batwowowowowowoman')
print(matchObjectThree.group())