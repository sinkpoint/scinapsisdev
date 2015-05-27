import csv
import functools
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from search import settings

file = 'closed_beta_accounts.csv'

def remove_space(input):
    return input.replace(' ','')
res = []
users = []
with open(file, 'rU') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        row = map(str.lower, row)
        my_password = User.objects.make_random_password()
        row.append(my_password)
        print ', '.join(row),
        res.append(row)

        user_name = '.'.join(map(remove_space,row[:2]))
        #hash_pw = make_password(my_password)

        #print user_name,hash_pw
        user = User(first_name=row[0],
                    last_name=row[1],
                    username=user_name,
                    email=row[2],
                    is_active=True)
        user.set_password(my_password)
        users.append(user)

User.objects.bulk_create(users)

with open('account_passwords.csv', 'wb') as fp:
    writer = csv.writer(fp, delimiter=',', quoting=csv.QUOTE_NONE)
    writer.writerow(['first','last','email','password'])
    writer.writerows(res)