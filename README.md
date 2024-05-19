# Font_Processing_Toolkit
 This toolkit provides a set of Python scripts and Jupyter notebooks to assist with the management, conversion, and validation of font files. The toolkit includes scripts for analyzing, copying, verifying, converting, and validating font files.
## Repository Structure

- `font_analysis.ipynb`: Jupyter notebook for analyzing font collections, including finding duplicate fonts and counting unique fonts by extension.
- `font_copy_and_verify.py`: Script for copying font files from a source directory to a destination directory and verifying their validity.
- `font_conversion.py`: Script for converting OTF and WOFF font files to TTF format.
- `font_validation.py`: Script for validating TTF font files and removing invalid ones.

## How to Use

### 1. Font Analysis

The `font_analysis.ipynb` notebook helps you analyze font collections by finding duplicate fonts and counting unique fonts by extension. The main advantage of this notebook is its recursive search, which explores all subdirectories.

#### Usage

1. Open the `font_analysis.ipynb` notebook in Jupyter Notebook or Jupyter Lab.
2. Modify the `directory_path` variable in the first cell to point to the directory containing your font collection.
   ```python
   directory_path = r"path/to/your/font/directory"
   ```
3. Run the cells in the notebook to perform analysis tasks such as finding duplicate fonts and counting unique fonts by extension.

### 2. Font Copy and Verify
The `font_copy_and_verify.py` script copies font files from a source directory to a destination directory and verifies their validity. This saves time by automating the process of copying fonts and checking for duplicates. It considers files with the same name and extension, choosing the larger file size, which likely includes more glyphs or information. The script divides the files into three folders (ttf, otf, woff) and verifies their functionality.

#### Usage
1. Open the script `font_copy_and_verify.py` in your preferred code editor.
2. Modify the `src_directory` and `dst_directory` variables to point to your source and destination directories.
3. Run code

### 3. Font Conversion
The `font_conversion.py` script converts OTF and WOFF font files to TTF format. This is useful if you need all your font files in TTF format for compatibility or other reasons.

#### Usage
1. Open the script `font_conversion.py` in your preferred code editor.
2. Modify the `directory_path` variable to point to the directory containing the fonts you want to convert.
3. Run code

### 4. Font Validation
The `font_validation.py` script validates TTF font files in a directory and removes invalid ones. This is important after conversion, as some files might get corrupted.

#### Usage
1. Open the script `font_validation.py` in your preferred code editor.
2. Modify the `directory_path` variable to point to the directory containing the TTF fonts you want to validate.
3. Run code

### How This Toolkit Can Help
This toolkit can help you manage large collections of font files by automating common tasks such as analyzing, copying, verifying, converting, and validating fonts. It can be particularly useful for graphic designers, typographers, and developers working with diverse font collections.

### Key Benefits
Automation: Save time by automating repetitive tasks related to font file management.
Accuracy: Ensure the validity of your font files and avoid using corrupted or invalid fonts.
Convenience: Easily convert between different font formats to suit your project requirements.
Analysis: Gain insights into your font collection by identifying duplicates and counting unique fonts by type.
Feel free to explore and modify the scripts to fit your specific needs. Contributions and suggestions are welcome!

