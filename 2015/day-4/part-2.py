from hashlib import md5

secret_key = 'iwrupvqb'
counter = 0
while not md5(f"{secret_key}{counter}".encode('utf-8')).hexdigest()[:6] == '000000':
    counter += 1
print(counter)
