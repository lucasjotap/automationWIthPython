While there are several steps to using regular expressions in Python, each step is fairly simple.

1 - Import the regex module with `import re`.

2 - Create a Regex object with the `re.compile()`function. (Remember to use a raw string.)

3 - Pass the string you want to search into the Regex object’s `search()` method. This returns a Match object.

4 - Call the Match object’s group() method to return a string of the actual matched text.

While I encourage you to enter the example code into the interactive shell, you should also make use of web-based regular expression testers, which can show you exactly how a regex matches a piece of text that you enter. I recommend the tester at `http://regexpal.com/`.