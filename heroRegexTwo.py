import re

batRegex = re.compile(r'Bat(wo)?man')
matchObject = batRegex.search('The Adventures of Batman.')
