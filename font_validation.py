'''Проверка валидности файлов ttf и удаление неверных'''
import os
from fontTools.ttLib import TTFont

def validate_ttf(font_path):
    try:
        font = TTFont(font_path)
        font.save(font_path)  # Попытка сохранения для проверки
        print(f'Validated: {font_path}')
        return True
    except Exception as e:
        print(f'Invalid TTF file: {font_path}, error: {e}')
        return False

def process_ttf_directory(directory_path):
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith('.ttf'):
            if not validate_ttf(file_path):
                os.remove(file_path)
                print(f'Deleted: {file_path}')

# Пример использования
directory_path = r'path/to/ttf/directory'
process_ttf_directory(directory_path)
