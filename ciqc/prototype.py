import cv2
import os
import pytesseract
from remove_text import draw_boxes_on_text
from DicomReader import DicomReader
from pathlib import Path

# Read in DICOM
data_reader = DicomReader("ultrasound1.dcm", "test-dicoms")
data_reader.show_image()


# Demo Text Blocking
if os.name == 'nt':
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img_boxes = draw_boxes_on_text(data_reader.pixel_array)
cv2.imshow("Output", img_boxes)
cv2.waitKey(0)
