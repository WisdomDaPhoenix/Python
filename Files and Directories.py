#List all files contained on the Desktop directory
import os
directory = 'c:/users/wisdom/desktop/'
entries = os.listdir(directory)
for t in entries:
    if os.path.isfile(directory+t):
        print(t)
#List all entries in Bone Foods directory
import os
f = 'Bone Foods'
entries = os.listdir('c:/users/wisdom/desktop/'+f)
print(entries)

#List all text files contained in the directory called Python programs
import os
entries = os.listdir('c:/users/wisdom/documents/hotwizzytron/Python programs')
for t in entries:
    if t[-4:] == '.txt':
        print(t)

#Getting files from the internet. Reading contents of a page into a string s
from urllib.request import urlopen
page = urlopen('http://www.google.com')
s = page.read().decode()


#Walk through the directory called Python programs and list all python program files (.py)
import os
for (path, dirs, files) in os.walk('c:/users/wisdom/documents/hotwizzytron/Python programs'):
    for filename in files:
        if filename[-3:]=='.py':
            print(filename)



#Run a program called Notepad++ by first locating using the path to its executable file or (.exe) file
import os
os.chdir('c:/Users/wisdom/Documents/Software Setups/Notepad++')
os.system('notepad++.exe')

#Remove or delete a file called Patients data from Bone Foods directory on the desktop
import os
os.remove('c:/users/wisdom/desktop/bone foods/Patients data.txt')
print('File deleted')


#Rename the Emails file from marketing file to Emails
import os
os.rename('c:/users/wisdom/desktop/bone foods/EMAILS FOR MARKETING.txt', 'c:/users/wisdom/desktop/bone foods/EMAILS.txt')
print('File updated')




import os
f = 'Skin Foods'
g = 'Liver Foods'
m = 'Bone Foods'
directory = 'c:/users/wisdom/desktop/'
newdir = os.mkdir(directory+f)
newdir = os.mkdir(directory+g)
newdir = os.mkdir(directory+m)
print('New directories created')


import os
newdir = os.rmdir('c:/users/wisdom/desktop/badlands')
print('Directory removed')

import os
#f = 'badlands'
#directory = 'c:/users/wisdom/desktop/'
newdir = os.mkdir('c:/users/wisdom/desktop/badlands')
print('New directory created')

