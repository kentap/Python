import string, random, itertools
import zipfile

file_path = "file path here"
size = 4
chars = "password here"
count = 0

with zipfile.ZipFile(file_path, 'r') as zf:
    for i in range(100000):
        # パスワードはバイト型で有る必要がある
        pwd = bytes(''.join(random.choices(chars, k=size)), 'UTF-8')
        try:
            zf.extractall(path='.', pwd=pwd)
            print('success : password  : {}'.format(pwd))
            break
        except Exception as e:
            count += 1

print('tried passwords : ', count)
