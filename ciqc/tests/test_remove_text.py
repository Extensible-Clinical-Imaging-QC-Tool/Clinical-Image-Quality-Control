import os
import cv2
import unittest
from pydicom import dcmread
from ciqc.remove_text import draw_boxes_on_text


class TwoCompartmentModelTest(unittest.TestCase):

    def test_draw_boxes_on_text(self):
        data_dir = os.path.abspath("test-dicoms")
        path = os.path.join(data_dir, "ultrasound1.dcm")
        dicom = dcmread(path)
        img = dicom.pixel_array

        test_img = cv2.imread("test_boxes_img.png")
        box_image = draw_boxes_on_text(img)

        self.assertEqual(box_image, test_img)
