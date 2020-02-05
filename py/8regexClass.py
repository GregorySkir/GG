import re

## exracting phone numbers

phoneNumRegex = re.compile(r'(\d{3})-(\d{7})')
# phoneNumRegex = re.compile(r'(\+972)?-?(\d{2,3})-?(\d{7})')
# phoneNumRegex = re.compile(r'(?:(?:\+|00)972)?-?(\d{2,3})(?:-| - )?(\d{7})')

my_number = '054-1234567'
phone = phoneNumRegex.search(f'My number is {my_number}.')
print('Phone number found: ' + phone.group())

print('Using search :', phoneNumRegex.search(f'My number is {my_number}.').group())
print('Using match: ', phoneNumRegex.match(f'My number is {my_number}.'))
print('Using findall :', phoneNumRegex.findall(f'My number is {my_number}.'))

earnest = """Lady Bracknell.  In the carriage, Gwendolen!  [Gwendolen goes to the door.  She and Jack blow kisses to each other behind Lady Bracknell's back.  Lady Bracknell looks vaguely about as if she could not understand what the noise was.  Finally turns round.]  Gwendolen, the carriage!
Gwendolen.  Yes, mamma.  [Goes out, looking back at Jack.]
Lady Bracknell.  [Sitting down.]  You can take a seat, Mr. Worthing.
[Looks in her pocket for note-book and pencil.]
Jack.  Thank you, Lady Bracknell, I prefer standing."""

result = re.sub('Gwendolen', '', earnest)  # Delete pattern abc.
result = re.sub('Gwendolen', 'Honey', earnest)  # Replace pattern Gwendolen -> Honey.
result = re.sub(r'\s+', ' ', earnest)  # Eliminate duplicate whitespaces.
re.sub(r'\[[\w\.\-!,\s\']+?\]', '', earnest) # Delete play notes.