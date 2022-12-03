import re

heroRegex = re.compile(r'Batman|Tina Fey')
matchObject = heroRegex.search("Batman and Tina Fey.")
matchObject2 = heroRegex.search('Tina Fey and Batman.')
print(matchObject.group())
print(matchObject2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
matchObject3 = batRegex.search('Batmobile lost a wheel')
matchObject4 = batRegex.search('Batman is a character of the DC universe.')
print(matchObject3.group())
print(matchObject4.group())
print(matchObject3.group(1))
print(matchObject3.group(0))
print(matchObject4.groups())