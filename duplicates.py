import os
import sys
import collections


def get_files_name_size_path(directory):
    files_name_size_path = collections.defaultdict(list)
    for dirs_path, dirs, files_name in os.walk(directory):
        for file_name in files_name:
            file_path = os.path.join(dirs_path, file_name)
            file_size = os.path.getsize(file_path)
            file_name_and_size = (file_name, file_size)
            files_name_size_path[file_name_and_size].append(dirs_path)
    return files_name_size_path


def get_duplicates(files_name_size_path):
    duplicates = {}
    for (file_name, file_size), file_path in files_name_size_path.items():
        if len(file_path) > 1:
            duplicates[(file_name, file_size)] = file_path
    return duplicates


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit('you did not enter the path to the directory as parameter')
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        exit('wrong path to the directory / directory not exist')
    file_size_path = get_files_name_size_path(directory)
    duplicates = get_duplicates(file_size_path)
    if not duplicates:
        exit('no duplicates in such directory')
    print('duplicate files found:')
    for (file_name, file_size), file_paths in duplicates.items():
        print('file: {} , size: {} Bytes in folders:'.format(
            file_name,
            file_size
        ))
        for file_path in file_paths:
            print(file_path)
        print()
