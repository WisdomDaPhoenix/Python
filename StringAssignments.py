"""word = input('Enter any word: ')
word = word.lower()
if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word:
    print('Word contains vowels')

else:
    print('No vowels')



formular = input('Enter a formular: ')
opening_par_count = 0
closing_par_count = 0
for c in formular:
    if c == '(':
         opening_par_count = opening_par_count + 1
    elif c == ')':
        closing_par_count = closing_par_count + 1

if opening_par_count == closing_par_count:
    print('You have equal number of parentheses')
else:
    print('You have ',opening_par_count, 'opening parentheses and ',closing_par_count,' closing parentheses')

string_text = input('Enter any text: ')
s = string_text[1] #Get second character
if string_text.index(s)< 2: # if index of second character is 1
    new_string = string_text.replace(s,'*') + '!'*3
print(new_string)"""

string_text = input('Enter any text: ')
new_string = string_text[:1] + '*' + string_text[2: ] +  '!'*3
print(new_string)
    







"""userentry = input('Enter any text: ')
userentry = userentry.lower()
userentry = userentry.replace('a','e')
print(userentry)

for c in userentry:
    userentry = userentry.replace(c,'*')

print(userentry)"""

    
