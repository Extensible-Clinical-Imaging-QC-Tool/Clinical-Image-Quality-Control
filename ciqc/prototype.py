import cv2
import os
import pytesseract
from remove_text import draw_boxes_on_text
from DicomReader import DicomReader
from pathlib import Path

# Read in DICOM

dicoms = ['ct1', 'ct2', 'ct3','xray1', 'xray2', 'xray3', 'pet1', 'pet2', 'pet3', 'mri1', 'mri2', 'mri3','ultrasound1', 'ultrasound2' ]
for dicom in dicoms:
    print(Path.cwd())
    data_reader = DicomReader(Path("test-dicoms") / (dicom + '.dcm'))
    data_reader.show_image()


# Demo Text Blocking
    if os.name == 'nt':
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    img_boxes = draw_boxes_on_text(data_reader.pixel_array)
    data_reader.write_new_image(img_boxes)
    data_reader.show_image()
