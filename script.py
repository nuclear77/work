# task2
import os
import time
import hashlib

timestamp = int(time.time())

for filename in os.listdir('.'):
    if filename.endswith('.log'):
        new_filename = f'filename_{timestamp}.log'
        os.rename(filename, new_filename)
        print(f'Renamed {filename} to {new_filename}')
    elif filename.endswith('.py'):
        git_hash = hashlib.sha1()
        with open(filename, 'rb') as file:
            git_hash.update(file.read())
        git_hash = git_hash.hexdigest()[:7]

        new_filename = f'{filename[:-3]}_{git_hash}.py'
        os.rename(filename, new_filename)
        print(f'Renamed {filename} to {new_filename}')