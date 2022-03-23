import os

def get_folder_size(folder_path):
    total_size = 0
    for dir_name, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(dir_name, file_name)
            file_size = os.path.getsize(file_path)
            total_size += file_size
    return total_size

if __name__ == '__main__':
    folder_size = get_folder_size('EXAMPLES')
    print("folder_size: {}".format(folder_size))

    folder_size = get_folder_size('DATA')
    print("folder_size: {}".format(folder_size))

    folder_size = get_folder_size('.')
    print("folder_size: {}".format(folder_size))
