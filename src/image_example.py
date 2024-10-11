from image import open_image_asRGB, open_image_as3D, store_img_rgb, store_img_bw


import numpy as np

data, (w, h, c) = open_image_asRGB("minion.jpg")

data2 = open_image_as3D("minion.jpg")


new = np.empty((w, h))


# store_img_bw(new, "test_bw.jpg")
store_img_rgb(data, "test_color.jpg")
store_img_rgb(data2, "test_color2.jpg")
