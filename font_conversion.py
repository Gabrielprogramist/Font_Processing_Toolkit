'''Конвертация шрифтов из otf и woff в ttf'''
import os
import subprocess
from fontTools.ttLib import TTFont
from fontTools.subset import Subsetter
from fontTools.ttx import makeOutputFileName

def convert_otf_to_ttf(input_path, output_path):
    try:
        font = TTFont(input_path, recalcBBoxes=False, recalcTimestamp=False)
        font.save(output_path)
        print(f'Converted: {input_path} -> {output_path}')
        return True
    except Exception as e:
        print(f'Failed to convert {input_path} to TTF: {e}')
        return False

def convert_woff_to_ttf(input_path, output_path):
    try:
        # Используем fontTools для извлечения TTF из WOFF
        font = TTFont(input_path)
        font.flavor = None
        font.save(output_path)
        print(f'Converted: {input_path} -> {output_path}')
        return True
    except Exception as e:
        print(f'Failed to convert {input_path} to TTF: {e}')
        return False

def process_fonts_in_directory(directory_path):
    font_dirs = ['otf', 'woff']
    for font_dir in font_dirs:
        src_dir = os.path.join(directory_path, font_dir)
        if not os.path.exists(src_dir):
            print(f'{src_dir} does not exist')
            continue

        convert_dir = os.path.join(directory_path, f'{font_dir}_convert')
        os.makedirs(convert_dir, exist_ok=True)

        for file_name in os.listdir(src_dir):
            file_path = os.path.join(src_dir, file_name)
            if os.path.isfile(file_path):
                output_file_path = os.path.join(convert_dir, os.path.splitext(file_name)[0] + '.ttf')
                if font_dir == 'otf':
                    if not convert_otf_to_ttf(file_path, output_file_path):
                        os.remove(output_file_path)
                elif font_dir == 'woff':
                    if not convert_woff_to_ttf(file_path, output_file_path):
                        os.remove(output_file_path)

# Пример использования
directory_path = r'path/to/directory/for/conversion'
process_fonts_in_directory(directory_path)
