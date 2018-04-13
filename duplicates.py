import os
import sys
import collections


def get_files_name_size_path(directory):
    files_info_dic = collections.defaultdict(list)
    for dirs_path, dirs, names in os.walk(directory):
        for file_name in names:
            file_path = os.path.join(dirs_path, file_name)
            file_size = os.path.getsize(file_path)
            file_name_and_size = (file_name, file_size)
            files_info_dic[file_name_and_size].append(dirs_path)
    return files_info_dic


def get_duplicates(file_info):
    duplicates = {}
    for info, path in file_info.items():
        if len(path) > 1:
            duplicates[info[0]] = path
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
    for file, path in duplicates.items():
        print(file, path)
