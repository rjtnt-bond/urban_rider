""" import hashlib

pwd='password'
email='jkr@gmail.com'
pwd='ChairOnTableWith3Legs'


pwd_encode=pwd.encode()
pwd_hash=hashlib.md5(pwd_encode).hexdigest()

your_email='jkr@gmail.com'
your_password = 'ChairOnTableWith3Legs'

hacker_email='jkr@gmail.com'
hacker_password='2329e22c9a4de221abeabaf22b72c7fc'


print(pwd_hash)
 """

import hashlib

user_email='jkd@gmaiul.com'
pass_word='ilikeuifulovemeTakingIsareToSureData'

data_base_stor_encode=pass_word.encode()
data_base_stor=hashlib.md5(data_base_stor_encode).hexdigest()

hacker_email='jkd@gmaiul.com'
hacker_password='97c9e3aa78069d4cf24fdfcb0f41523d'

your_email='jkd@gmaiul.com'
your_pass_word='97c9e3aa78069d4cf24fdfcb0f41523d'

# hased_encode=your_pass_word.encode()
hashed_password=hashlib.md5(your_pass_word.encode()).hexdigest()

if your_email==user_email and data_base_stor==hashed_password:
    print('Right User')
else:
    print('Worng User')


# print(data_base_stor)














