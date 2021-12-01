import os
import cv2
from remove_text import draw_boxes_on_text
from DicomReader import DicomReader
from pathlib import Path

# Read in DICOM

dicoms = []
for root, dirs, files in os.walk(Path("eval-dataset/raw-dicoms/GEMS_IMG")):
    for file in files:
        # if file.endswith('.dcm'):
        dicoms.append(os.path.join(root, file))

for dicom in dicoms:
    data_reader = DicomReader(dicom)
    data_reader.show_image(resize=False)

    # Demo Text Blockings
    img_boxes = draw_boxes_on_text(data_reader.pixel_data)
    cv2.imshow("Dicom Image", img_boxes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
