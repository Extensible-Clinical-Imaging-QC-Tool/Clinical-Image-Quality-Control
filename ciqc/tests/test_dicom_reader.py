import unittest
import numpy as np
from ciqc.DicomReader import DicomReader
from pathlib import Path


class DicomReaderTest(unittest.TestCase):

    def test_pixel_array(self):
        test_path = Path("ciqc/tests/test_dicom_pixel.npy")

        dicom_path = Path("test-dicoms/ultrasound1.dcm")

        dicom = DicomReader(dicom_path)
        img = dicom.pixel_array

        np.testing.assert_array_equal(np.load(test_path), img)

    def test_show_image(self):
        pass

    def test_write_new_image(self):
        pass

    def test_write_out_dicom(self):
        pass
