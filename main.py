import pyvips

print('Loading kiwi.jpg')
image = pyvips.Image.new_from_file('kiwi.jpg', access='sequential')
image *= [1, 2, 1]
mask = pyvips.Image.new_from_array([[-1, -1, -1],
                                    [-1, 16, -1],
                                    [-1, -1, -1]], scale=8)
image = image.conv(mask, precision='integer')
image.write_to_file('kiwi2.jpg')
print('Processed image saved as kiwi2.jpg')
