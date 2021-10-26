import pydicom
import numpy as np
from pathlib import Path
import cv2

class DicomReader:

    def __init__(self, fname, path=".") -> None:
        
        self.fpath = Path(path) / fname
        self.dicom = self.read_file()
        self.pixel_array = self.dicom.pixel_array
        
    def read_file(self):
        dicom = pydicom.dcmread(self.fpath)
        return dicom

    
    def show_image(self) -> None:
        # Multiply image by 16 to increase dynamic range for CV2
        pixel_data = self.pixel_array  * 16
        cv2.imshow("Dicom Image", pixel_data)
        cv2.waitKey(0)
        cv2.destroyAllwindows




        

class DicomObject: