import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image

image_dir_path = 'images'

# # image datasets variables
image_size = (128, 128)
colorscale = 'rgb'  # grayscale

images_list = []

img_names = ['a1.jpeg', 'a2.jpeg', 'a3.jpeg', 'a4.jpeg']


for img_name in img_names:
    img = image.load_img(image_dir_path + '/' + img_name,
                         color_mode=colorscale, target_size=image_size)
    img2 = image.img_to_array(img)
    print(img2.shape)
    images_list.append(img2)


images_list = np.asarray(images_list)
print(images_list.shape)


# # Plotting-1
# for i in range(4):
#     plt.imshow(images_list[i]/255)
#     plt.show()


# # Plotting-2
# fig = plt.figure(figsize=(8, 8))
# columns = 2
# rows = 2
# for i in range(1, columns*rows + 1):
#     img = images_list[i-1]
#     fig.add_subplot(rows, columns, i)
#     plt.imshow(img/255)
# plt.show()


# # Plotting-3
fig, axes = plt.subplots(2, 2, figsize=(8, 8), subplot_kw={
                         'xticks': [], 'yticks': []})

for i, ax in enumerate(axes.flat):
    img = images_list[i-1] / 255
    ax.imshow(img, cmap='binary', interpolation='nearest')
    ax.text(0, -.1, str(img_names[i]),
            transform=ax.transAxes, color='black')

plt.show()
