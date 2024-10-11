import numpy as np
from PIL import Image


def open_image_asRGB(name):
    # every third row contains values for the same color channel
    img = Image.open(name)
    imgArray = np.array(img, dtype=np.float32)
    print(imgArray.shape)  # height, width, color channels
    retArray = np.empty((imgArray.shape[0] * imgArray.shape[2], imgArray.shape[1]))
    retArray[0::3, :] = imgArray[:, :, 0]
    retArray[1::3, :] = imgArray[:, :, 1]
    retArray[2::3, :] = imgArray[:, :, 2]
    print(retArray.shape)
    return retArray, imgArray.shape


def open_image_as3D(name):
    # third array dimension is for color channels
    img = Image.open(name)
    imgArray = np.array(img)
    return imgArray.astype(np.float32)


def store_img_bw(data, name):
    dataint = data.astype(np.int8)
    img = Image.fromarray(dataint, "L")
    img.save(name)


def store_img_rgb(data, name):
    if data.ndim == 2:
        dataint = np.empty((data.shape[0] // 3, data.shape[1], 3), dtype=np.int8)
        dataint[:, :, 0] = data[0::3, :]
        dataint[:, :, 1] = data[1::3, :]
        dataint[:, :, 2] = data[2::3, :]
    else:
        dataint = data.astype(np.int8)
    img = Image.fromarray(dataint, "RGB")
    img.save(name)
