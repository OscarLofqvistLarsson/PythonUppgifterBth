import os
def find_sub_dirs(directory):
    paths = os.listdir(directory)
    sub_dirs = []
    for path in paths:
        fullpath = directory + '/' + path
        if os.path.isdir(fullpath):
            sub_dirs.append(fullpath)
            sub_dirs += find_sub_dirs(fullpath)
    return sub_dirs

print(find_sub_dirs("C:/Test"))