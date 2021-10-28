import os
import unittest
from numpy.testing import assert_equal
from pydicom import dcmread
import pytesseract
from ciqc.remove_text import draw_boxes_on_text

if os.name == 'nt':
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


class RemoveTextTest(unittest.TestCase):
    """
    Tests the draw_boxes_on_text function by checking that tesseract does not detect text
    on the image returned by draw_boxes_on_text
    """
    def test_draw_boxes_on_text(self):
        data_dir = os.path.abspath(os.path.join("test-dicoms"))
        path = os.path.join(data_dir, "pet5.dcm")
        dicom = dcmread(path)
        img = dicom.pixel_array
        box_image = draw_boxes_on_text(img)
        assert_equal(pytesseract.image_to_string(box_image), " \n\x0c")
