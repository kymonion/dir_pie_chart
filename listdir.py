import os

dirs = []
files = []

for item in os.listdir(os.getcwd()):
    if os.path.isdir(item):
        dirs.append(item)
    elif os.path.isfile(item):
        files.append(item)

print("\n-= 폴더 =-")
for item in dirs:
    print(item)

print("\n-= 파일 =-")
for item in files:
    print(item)

input("\n-= Enter로 종료 =-")
