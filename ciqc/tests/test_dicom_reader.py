import os
# import cv2
import unittest
import numpy as np
# from pydicom import dcmread
from ciqc.DicomReader import DicomReader
from pathlib import Path


class DicomReaderTest(unittest.TestCase):

    def test_pixel_array(self):
        test_data_dir = os.path.abspath("ciqc/tests")
        test_path = os.path.join(test_data_dir, "test_dicom_pixel.npy")

        data_dir = os.path.abspath(os.path.join("test-dicoms"))
        path = os.path.join(data_dir, "ultrasound1.dcm")

        dicom = DicomReader(path)
        img = dicom.pixel_array

        np.testing.assert_array_equal(np.load(test_path), img)

    def test_show_image(self):
        pass

    def test_write_new_image(self):
        pass

    def test_write_out_dicom(self):
        pass
