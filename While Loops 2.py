
numor = 0
denom = 1
while numor < denom:
    d = eval(input('Enter digit position by number - (e.g. 4 for 4th digit): '))
    numor = eval(input('Enter numerator of the fraction: '))
    denom = eval(input('Enter denominator of the fraction: '))
    if d == 1 and numor < denom:
        res = (numor*10)//denom
        x = str(res)
        print(x[0])
    elif d == 2 and numor < denom:
        res = (numor*100)//denom
        x = str(res)
        print(x[1])
    elif d == 3 and numor < denom:
        res = (numor*1000)//denom
        x = str(res)
        print(x[2])
    elif d == 4 and numor < denom:
        res = (numor*10000)//denom
        x = str(res)
        print(x[3])
    elif d == 5 and numor < denom:
        res = (numor*100000)//denom
        x = str(res)
        print(x[4])
    else:
        print('Get lost! This is not a fraction')
        




L = ['fan','electric bulb','television','socket','decoder','wire','remote control','meter']
N=[]
print(L)
from random import choice, shuffle
for item in L:
    for c in item:
        if item.count(c)>1:
            N.append(item)
            break
print(N)


norepeat = []
for i in range(len(L)):
    if L[i] not in N:
       norepeat.append(L[i])

print(norepeat)
t = choice(norepeat)
while t in L:
    shuffle(norepeat)
    if t:
        print(t)
        break
















    
   
        
    

"""

s = input('Enter text or word here: ')
t = input('Enter character: ')
for i in range(len(s)):
    if t in s:
        print(s.index(t))
        break
else:
    print(t, 'is not contained in',s)
        
    


num1 = eval(input('Enter first number: '))
num2 = eval(input('Enter second number: '))
    
while num2 < num1 and num2 != 0:
      r = num1 % num2
      num1 = num2
      num2 = r
      i = i + 1
print('Greatest common divisor of both numbers are: ', num1) 	



s = input('Enter text or word here: ')
while True:
    t = input('Enter character: ')
    if t not in s:
        print(t, 'is not contained in',s)
        break 
    print(s.index(t))   
           
    


#user-defined input: number of scores(num) to enter
#define count as 0
#define and initialize score to 1
#define total as 0
#define and initialize i to 0
#while i is less than number of scores(num) and score is greater than or equal 0, enter scores
#Inside loop: total score = total score + score
#Inside loop: if score is greater than or equal to 90, increment count
#Outside loop: print count
#Outside loop: print average as total score divided by num

num = eval(input('Enter number of scores you\'d like to input: '))
scorecount = 0
count = 0
score = 1
total = 0
i = 0
while i < num and score >= 0:
    score = eval(input('Enter a score - (negative score to quit): '))
    scorecount = scorecount + 1
    if scorecount == num:
        print('You have entered ',num,' scores already - add negative score below to quit')
    total = total + score
    if score >= 90:
        count = count + 1
print('There are ',count,'scores which are \'A\'s')
print(total/num)"""


