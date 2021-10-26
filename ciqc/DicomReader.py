import pydicom
import numpy as np
from pathlib import Path
import cv2

class DicomReader:
    """
    A Dicom Reader object that can parse DICOM files, with functionality to read 
    and write tags within the file.
    
    :param fname: File name for the DICOM file
    :type fname: str
    :param path: Path to the DICOM file using forward-slash, defaults to "."
    :type path: str, optional
    :ivar dicom: A dataset object for the DICOM file, using the pydicom package.
    :type dicom: FileDataset
    :ivar fpath: Full path to the DICOM file
    :type fpath: PosixPath
    :ivar pixel_array: Array of pixel values in the dicom file.
    :pixel_array type: ndarray
    """
 

    def __init__(self, fname: str, path: str = ".") -> None:   
        self.fpath = Path(path) / fname
        self.dicom = self.read_file()
        self.pixel_array = self.dicom.pixel_array
        
    def read_file(self):
        dicom = pydicom.dcmread(self.fpath)
        return dicom

    
    def show_image(self) -> None:
        """Displays the image data of the dicom using OpenCV.
        Supports displaying images with a bit depth of 8 or 16. 
        Unsuppoted bit depths may not be displayed correctly by OpenCV.
        """        
        # Display image depending on its bit depth
        if self.dicom.BitsStored == 8:
            pixel_data = self.pixel_array
        elif self.dicom.BitsStored == 16:
            pixel_data = self.pixel_array * 16
        else:
            print("Unsupported bit depth, image may not be displayed correctly.")
        cv2.imshow("Dicom Image", pixel_data)
        cv2.waitKey(0)
        cv2.destroyAllwindows
    
    def write_new_image(self, pixel_data: np.ndarray) -> None:
        pass

    def write_out_dicom(self, fname, path='.') -> bool:
        pass