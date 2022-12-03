import re 

phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
matchObject = phoneRegex.search('My number is 415-555-4242')
print(matchObject.group())

matchObjectTwo = phoneRegex.search('My number is 555-4242')
print(matchObjectTwo.group())