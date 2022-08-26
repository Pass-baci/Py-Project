import os


def search_file(path, file_name):
    files = os.listdir(path)
    for files_name in files:
        if os.path.isdir(files_name):
            files_name = search_file(path+files_name+'/', file_name)
            if files_name is not None:
                return files_name

        if os.path.isfile(path+files_name):
            if files_name == file_name:
                return os.path.abspath(files_name)


if __name__ == '__main__':
    print(search_file('./', 'a.txt'))
