import string
from tqdm import tqdm
from os import system
system('cls')
password = "5?de"
hor = string.ascii_letters+string.digits+string.punctuation
print(hor)
found = False

for i in tqdm(hor):
    for j in hor:
        for d in hor:
            for k in hor:

                gh = i+j+d+k
                if gh == password:
                    found = True
                    print(f'password == {gh}')
                    input('')
                    break
            if found: break
        if found: break
    if found: break
