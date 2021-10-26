import cv2
import os
import pytesseract
from pydicom import dcmread
from remove_text import draw_boxes_on_text

# Read in DICOM
data_dir = os.path.abspath("test-dicoms")
path = os.path.join(data_dir, "ultrasound1.dcm")
dicom = dcmread(path)
img = dicom.pixel_array

cv2.imshow("Output", img)
cv2.waitKey(0)

# Demo Text Blocking
if os.name == 'nt':
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img_boxes = draw_boxes_on_text(img)
cv2.imshow("Output", img_boxes)
cv2.waitKey(0)
