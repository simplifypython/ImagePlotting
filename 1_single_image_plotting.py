import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# path to image
image_path = 'images/a1.jpeg'

# load image as NumPy Array
img_as_arr = mpimg.imread(image_path)

# print Array shape
print(img_as_arr.shape)

# show image
plt.imshow(img_as_arr/255)
plt.show()
# plt.savefig("image1.jpg")
