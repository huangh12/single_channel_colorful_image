'''
 reference: http://stackoverflow.com/questions/3114925/pil-convert-rgb-image-to-a-specific-8-bit-palette
            http://abruzzi.iteye.com/blog/314790
			http://www.2cto.com/kf/201603/492898.html

test
'''
from PIL import Image
import numpy as np
from datasets import CONFIG

# The arr is a predicted result
arr = np.load('arr.npy')

print 'The shape of the image is:', arr.shape
print 'The classes in the image are:', np.unique(arr)

# Define the palette
palette = []
for i in range(256):
	palette.extend((i, i, i))
	
# define the color of the 21 classes(PASACAL VOC)
palette[:3*21] = CONFIG['voc12']['palette'].flatten()

assert len(palette) == 768

im = Image.fromarray(arr)
im.show()
im.putpalette(palette)
im.show()

im.save('out.png')

