import pydicom
import numpy as np
from pathlib import Path
import cv2
from tkinter import Tk


class DicomReader:
    """
    A Dicom Reader object that can parse DICOM files, with functionality to read
    and write tags within the file.
    
    :param path: String path to the DICOM file 
    :type path: str, optional
    :ivar dicom: A dataset object for the DICOM file, using the pydicom package.
    :type dicom: FileDataset
    :ivar path: Converted Path to the DICOM file
    :type path: PosixPath
    :ivar pixel_array: Array of pixel values in the dicom file.
    :pixel_array type: ndarray
    """

    def __init__(self, path: str) -> None:   
        self.path = Path(path)
        self.dicom = self.read_file()

    @property
    def pixel_array(self):
        return self.dicom.pixel_array

    def read_file(self):
        dicom = pydicom.dcmread(self.path)
        return dicom

    def show_image(self, resize=True) -> None:
        """Displays the image data of the dicom using OpenCV.
        Supports displaying images with a bit depth of 8 or 16.
        Unsuppoted bit depths may not be displayed correctly by OpenCV.

        :param resize: Option to resize images before display, defaults to True
        :type resize: bool, optional
        """       
        # Display image depending on its bit depth
        if self.dicom.BitsStored == 8:
            pixel_data = self.dicom.pixel_array
        elif self.dicom.BitsStored == 16:
            pixel_data = self.dicom.pixel_array * 16
        else:
            print("Unsupported bit depth, image may not be displayed correctly.")
            pixel_data = self.dicom.pixel_array
        #pixel_data = cv2.cvtColor(pixel_data, cv2.COLOR_BGR2RGB)
        
        if resize:
            #Resize Images so they are consistent and scaled so they are all of the same height.
            if len(pixel_data.shape) == 2:
                height, width = pixel_data.shape
            elif len(pixel_data.shape) == 3:
                height, width, _ = pixel_data.shape
            else:
                raise ValueError("Can only process DICOM images with 2 or 3 dimensions.")
            
            # Display image as half window height
            
            root = Tk()
            w_height = root.winfo_screenheight()
            required_height = int(w_height * 0.5)
            resize_ratio = required_height / int(height)
            required_width = int(width *  resize_ratio)
            display_img = cv2.resize(pixel_data, (required_width, required_height))
        else:
            display_img = pixel_data
        
        cv2.imshow("Dicom Image", display_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def write_new_image(self, pixel_data: np.ndarray) -> None:
        """Takes in a byte array and writes out a new image to the PixelData.
        Saves all images as uncompressed using little endian explicit, changing the transfer 
        protocol UID as well.

        :param pixel_data: Array of pixel values to be saved.
        :type pixel_data: np.ndarray
        """
        # TODO Allow changing of image size & bit depth

        # Ensure that the width and height of the image are the same
        if not (pixel_data.shape[0] == self.dicom.Rows and pixel_data.shape[1] == self.dicom.Columns):
            raise ValueError("The pixel data provided must have the same dimensions as the original DICOM image.")

        self.dicom.PixelData = pixel_data.tobytes()
        self.dicom.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian

    def write_out_dicom(self, fname: str = None, path: str = '.') -> None:
        """Writes out the dicom to a dcm file. If no filename is provided then the original
        dcm file will be overwritten.

        :param fname: Filename to save, defaults to None and overwrites original
        :type fname: str, optional
        :param path: Path to save directory, defaults to '.'
        :type path: str, optional
        """
        if fname:
            fname = Path(fname)
            save_path = path.parent / fname
            self.dicom.save_as(save_path)
        else:
            self.dicom.save_as(self.path)
