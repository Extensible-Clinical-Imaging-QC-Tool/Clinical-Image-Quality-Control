import os
import pytesseract
if os.name == 'nt':
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

from tqdm import tqdm
from DicomReader import DicomReader
from pathlib import Path

dicoms = []
for root, dirs, files in os.walk(Path("eval-dataset/raw-dicoms/manifest-1617826555824")):
    for file in files:
        if file.endswith('.dcm'):
            dicoms.append(os.path.join(root, file))

for dicom in tqdm(dicoms):
    data_reader = DicomReader(dicom)
    if pytesseract.image_to_string(data_reader.pixel_array).strip() != "":
        print(dicom)
        data_reader.show_image()
