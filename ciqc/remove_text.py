import cv2
import numpy as np
import pytesseract


def draw_boxes_on_text(img):
    edit_img = np.copy(img)
    raw_data = pytesseract.image_to_data(edit_img)

    for idx, data in enumerate(raw_data.splitlines()):
        if idx > 0:
            data = data.split()
            if len(data) == 12:
                x, y, w, h = int(data[6]), int(data[7]), int(data[8]), int(data[9])
                cv2.rectangle(edit_img, (x, y), (w+x, h+y), (25, 180, 255), -1)

    return edit_img
