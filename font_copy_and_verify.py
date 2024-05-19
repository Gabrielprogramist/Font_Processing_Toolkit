'''Копирование и проверка валидности файлов шрифтов'''
import os
import shutil
from fontTools.ttLib import TTFont

def find_and_copy_fonts(src_directory, dst_directory):
    font_extensions = ('.ttf', '.otf', '.woff')
    font_files = {}

    # Рекурсивно обходим директорию и собираем файлы шрифтов
    for root, dirs, files in os.walk(src_directory):
        for file in files:
            if file.lower().endswith(font_extensions):
                file_path = os.path.join(root, file)
                file_name = os.path.basename(file)  # Получаем полное имя файла с расширением
                file_size = os.path.getsize(file_path)

                if file_name not in font_files:
                    font_files[file_name] = (file_path, file_size)
                else:
                    # Сравниваем размеры и выбираем файл с наибольшим размером
                    if file_size > font_files[file_name][1]:
                        font_files[file_name] = (file_path, file_size)

    # Создаем целевые папки для каждого типа шрифтов
    for ext in font_extensions:
        os.makedirs(os.path.join(dst_directory, ext[1:]), exist_ok=True)

    copied_files = []

    # Копируем файлы в соответствующие папки и проверяем их валидность
    for file_name, (file_path, _) in font_files.items():
        file_ext = os.path.splitext(file_name)[1]
        dst_path = os.path.join(dst_directory, file_ext[1:], file_name)
        shutil.copy2(file_path, dst_path)

        # Проверяем валидность файла шрифта
        try:
            font = TTFont(dst_path)
            copied_files.append(dst_path)
            print(f'Copied and verified: {file_path} -> {dst_path}')
        except Exception as e:
            print(f'Invalid font file: {dst_path}, error: {e}')
            os.remove(dst_path)
    
    return copied_files

# Пример использования
src_directory = r'path/to/source/directory'
dst_directory = r'path/to/destination/directory'
copied_files = find_and_copy_fonts(src_directory, dst_directory)
print('Список скопированных файлов шрифтов:')
for file in copied_files:
    print(file)
