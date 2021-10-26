import os
import cv2
import unittest
import numpy as np
from pydicom import dcmread
from ciqc.remove_text import draw_boxes_on_text


class TwoCompartmentModelTest(unittest.TestCase):

    def test_draw_boxes_on_text(self):
        data_dir = os.path.abspath(os.path.join("test-dicoms"))
        path = os.path.join(data_dir, "ultrasound1.dcm")
        dicom = dcmread(path)
        img = dicom.pixel_array

        test_img = cv2.imread(os.path.join("ciqc", "tests", "test_text_removal.png"))
        box_image = draw_boxes_on_text(img)

        np.testing.assert_almost_equal(box_image, test_img)
        pass
