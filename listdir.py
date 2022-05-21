import os

def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total

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
    print("size : %s" % get_dir_size(item))

print("\n-= 파일 =-")
for item in files:
    print(item)
    print("size : %s" % os.path.getsize(item))

input("\n-= Enter로 종료 =-")
