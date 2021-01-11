def to_jaden_case(text):
    from string import punctuation
    
   
        
    text = str(text) 
    
    text_list = text.split()
    for item in text_list:
        for c in punctuation:
            if c in item:
                pw_index = text_list.index(item)
                punc_word = text_list.pop(text_list.index(item))                
                punc_word = punc_word[0].upper() + punc_word[1:]
        
    print(punc_word)
    print(pw_index)
    
    text_list = [item.title() for item in text_list]
    text_list.insert(pw_index, punc_word)
    
        
    text = ' '.join(text_list)
    print(text_list)
    
    return text

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))











#Complete the method/function so that it converts dash/underscore delimited words into camel casing.
#The first word within the output should be capitalized only if the original word was capitalized
#(known as Upper Camel Case, also often referred to as Pascal case).

def to_camel_case(text):
    if text == '':
        return text
    d = {'hyphen':'-', 'underscore':'_'}
    if d['hyphen'] in text:
        n_list = text.split(d['hyphen'])
    elif d['underscore'] in text:
        n_list = text.split(d['underscore'])
    first = n_list[0]
    if not first[0].isupper():
        for i in range(1,len(n_list)):
            n_list[i] = n_list[i].title()
        alltext = ''.join(n_list)
        text = alltext
        return text
        
    else:
        for item in n_list:
            item = item.title()
        text = ''.join(n_list)
        return text
        
print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))




"""

def to_camel_case(text):
    if text == '':
        return text
    if '_' in text:
        n_list = text.split('_')
    
    elif '-' in text:
        n_list = text.split('-')
    first = n_list[0]
    if not first[0].isupper():
        for i in range(1,len(n_list)):
            n_list[i] = n_list[i].title()
        alltext = ''.join(n_list)
        text = alltext
        return text
        
    else:
        for item in n_list:
            item = item.title()
        text = ''.join(n_list)
        return text
        
        
    
    

print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))






k = 0
x = 0
def dig_pow(n, p):
    from math import pow
    if p == 0:
        print('Invalid value of p')
    
    x = str(n)
    L = list(x)
    L = [int(t) for t in x ]
    i = 0
    total = 0
    while i < len(L) and L[i] in L and p != 0:
        if p == 0:
            print('Invalid value of p')
            break
        else:
            total = total + pow(L[i],p)
            p = p + 1
        i = i + 1
    if total % n == 0:
        k = total/n 
        return k
    else:   
        return -1
print(dig_pow(89, 1))
print()"""




