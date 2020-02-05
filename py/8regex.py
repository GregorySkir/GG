#Q1
"""Write a an expression that would replace the string of all occurrences of the string cat with dog.
Use regular expressions.
- Your answer should receive an argument named text that would be the text to replace.
- No need to use import re (we are already doing it during testing). If you do, the test would fail.
- The test would print out the result, you don't need to."""
re.sub('cat', 'dog', text)
text = 'cats'#dogs
#Q2
"""Write a an expression that would extract numbers from a text and return a list of all the numbers.
Use regular expressions.
- Your answer should receive an argument named text.
- No need to use import re (we are already doing it during testing). If you do, the test would fail.
- The test would print out the result, you don't need to."""
re.compile(r'(\d+)').findall(text)
text = 'B3st'#['3']
text = '3.14 < 7/22'#['3', '14', '7', '22']
#Q3
"""Write a an expression that would extract all words from text without punctuation to a list.
Use regular expressions with \w
- Your answer should receive an argument named text.
- No need to use import re (we are already doing it during testing). If you do, the test would fail.
- The test would print out the result, you don't need to."""
re.compile(r'(\w+)').findall(text)
	
text = 'This is still 2019!'#['This', 'is', 'still', '2019']
#Q4
"""Write a an expression that extracts urls from a text.
Use regular expressions. 
- To fully answer the question, you need to use lookaheads:
https://stackoverflow.com/questions/12169327/positive-lookahead-to-match-or-end-of-string
- Your answer should receive an argument named text.
- No need to use import re (we are already doing it during testing). If you do, the test would fail.
- The test would print out the result, you don't need to.

What is a valid url:
- Strings starting with http:// or https://
- Characters include digits (0-9), letters(A-Z, a-z), and these special characters:
*'();:-.~_@&=+$,\/?#[]"""
re.findall(r'http[s]?:\/\/(?:[\w[.\/=,-?]+(?=\s|$))', text)
text = """Here are some urls: https://moodle2.cs.huji.ac.il/nu19/course/view.php?id=55793
Also there are some urls: http://www.google.com http://www.google.com.au https://facebook.com https://www.ynet.co.il/home/0,7340,L-8,00.html"""
#['https://moodle2.cs.huji.ac.il/nu19/course/view.php?id=55793', 'http://www.google.com', 'http://www.google.com.au', 'https://facebook.com', 'https://www.ynet.co.il/home/0,7340,L-8,00.html']
#Q5
"""Write a an expression that checks if a text is an email address.
Use regular expressions, the functions search or match and \b
- Your answer should receive an argument named text.
- No need to use import re (we are already doing it during testing). If you do, the test would fail.
- The test would print out the result, you don't need to.

What is a valid email address:
For the local-part of the email:
uppercase and lowercase Latin letters A to Z and a to z;
digits 0 to 9;
printable characters !#$%&'*+-/=?^_`{|}~;
dot ., provided that it is not the first or last character unless quoted, and provided also that it does not appear consecutively unless quoted (e.g. John..Doe@example.com is not allowed but "John..Doe"@example.com is allowed); 
You can ignore the restriction on dots and the need to quote.
For the domain:
uppercase and lowercase Latin letters A to Z and a to z;
digits 0 to 9, provided that top-level domain names are not all-numeric;
a domain name has to include a name and its suffix, separated by a dot.
hyphen -, provided that it is not the first or last character."""
re.search('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', text)
text = r'ThisIs123@AnotherValid.mail'#True
text = r'This.IsNot.Valid'#False