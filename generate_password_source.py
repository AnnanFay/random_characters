import os
import random
import string

length = 64
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
row_count = 64

for row in range(row_count):
    random.seed = os.urandom(1024)

    print(''.join(random.choice(chars) for i in range(length)))
