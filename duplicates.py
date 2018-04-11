import os
import sys


def get_file_size_path(directory):
    file_info = {}
    for dirs_path, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(dirs_path, file)
            size = os.path.getsize(filepath)
            file_size = file + '+' + str(size)
            if file_size not in file_info:
                file_info[file_size] = [dirs_path]
            else:
                file_info[file_size].append(dirs_path)
    return file_info


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit('you did not enter the path to the directory as parameter')
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        exit('wrong path to the directory / directory not exist')
    file_size_path = get_file_size_path(directory)
    count_dup = 0
    for info, path in file_size_path.items():
        if len(path) > 1:
            file_size = info.split('+')
            print(
                'duplicates of file:',
                file_size[0],
                'of size:',
                file_size[1],
                'bites',
                'in directories:',
                path
            )
            count_dup += 1
    if not count_dup:
        exit('in this directory no duplicate files found')
