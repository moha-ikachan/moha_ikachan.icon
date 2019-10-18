import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

ikachan = (
    '0000000011100000000',
    '0000000133310000000',
    '0000001333331000000',
    '0000013333333100000',
    '0000133333333310000',
    '0001333333333331000',
    '0013333333333333100',
    '0133333333333333310',
    '0133312221222133310',
    '1333122112112213331',
    '1333122211122213331',
    '1333122112112213331',
    '0113112221222113110',
    '0001311111111131000',
    '0001333333334331000',
    '0000133333333310000',
    '0001433333334341000',
    '0001433343343341000',
    '0000141441441410000',
    '0000110110110110000',
)
ikachan = np.array([[int(_) for _ in line] for line in ikachan], np.uint8)

colors = (
    (0, 0, 0, 0),
    (45, 62, 79, 255),
    (236, 240, 241, 255),
    (124, 223, 146, 255),
    (63, 173, 168, 255)
)

# settings
icon_size = 400
icon_scale = 0.8

# compute parameters
rows, cols = ikachan.shape
pixel_size = int((icon_size * icon_scale) / max(rows, cols))
offset_y = (icon_size - (rows * pixel_size)) // 2
offset_x = (icon_size - (cols * pixel_size)) // 2

# make a bitmap
im = np.zeros((icon_size, icon_size, 4), np.uint8)
for i, j in np.ndindex(ikachan.shape):
    y0 = i * pixel_size + offset_y
    y1 = y0 + pixel_size
    x0 = j * pixel_size + offset_x
    x1 = x0 + pixel_size
    im[y0:y1, x0:x1] = colors[ikachan[i, j]]

# save an image
Image.fromarray(im).save('./moha_ikachan.icon.png')

# show an image
plt.imshow(im)
plt.show()
