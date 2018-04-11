import os
import sys


def get_files_size_path(directory):
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


def get_duplicates(file_info):
    duplicates = {}
    for info, path in file_info.items():
        if len(path) > 1:
            file_size = info.split('+')
            duplicates[file_size[0]] = path
    return duplicates


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit('you did not enter the path to the directory as parameter')
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        exit('wrong path to the directory / directory not exist')
    file_size_path = get_files_size_path(directory)
    duplicates = get_duplicates(file_size_path)
    if not duplicates:
        exit('no duplicates in such directory')
    for file, path in duplicates.items():
        print(file, path)
