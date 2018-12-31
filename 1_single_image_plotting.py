import matplotlib.pyplot as plt
from keras.preprocessing import image


# path to training & testing dataset
image_path = 'images/a1.jpeg'


# image datasets variables
# image_size = (28, 28)
# colorscale = 'rgb'  # grayscale

# load image
img = image.load_img(image_path)
# or
# img = image.load_img(image_path, target_size=image_size)


print(img)


img_as_arr = image.img_to_array(img)
print(img_as_arr.shape)


img_as_flatten_arr = img_as_arr.flatten()
print(img_as_flatten_arr.shape)

plt.imshow(img_as_arr/255)
plt.show()
# plt.savefig("image1.jpg")
