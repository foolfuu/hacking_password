import string
from tqdm import tqdm
from os import system
system('cls')
password = "s4ax1"
hor = ''
for i in password:
    if i in string.ascii_uppercase and string.ascii_uppercase not in hor: hor += string.ascii_uppercase
    elif i in string.ascii_lowercase and string.ascii_lowercase not in hor: hor += string.ascii_lowercase
    elif i in string.digits and string.digits not in hor: hor += string.digits
    elif i in string.punctuation and string.punctuation not in hor: hor += string.punctuation
# hor = string.ascii_letters+string.digits+string.punctuation


found = False
for i in tqdm(hor):
    for j in hor:
        for d in hor:
            for k in hor:
                for f in hor:
                    gh = i+j+d+k+f
                    if gh == password:
                        found = True
                        print(f'password == {gh}')
                        break
                if found: break
            if found: break
        if found: break
    if found: break

for i in range(2): input('')