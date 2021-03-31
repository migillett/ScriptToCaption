import os


def check_for_directory(directory):
    if not os.path.exists(directory):
        try:
            os.mkdir(directory)
            print('Directory created at', directory)
        except PermissionError:
            print('PERMISSION ERROR: Unable to create directory at', directory)
    else:
        print(f'Path {directory} already exists.')
