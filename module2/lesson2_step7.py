import os

# получаем полный путь до текущего исполняемого файла
path_to_file = os.path.abspath(__file__)
print(path_to_file)


# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)

# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'file.txt')
