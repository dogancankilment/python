import numpy as np
import matplotlib.pyplot as plt
import math
import scipy


def count_mask(img_1, mask):
    counter = 0
    control_a = False
    control_b = False
    control_c = False
    control_d = False

    m, n = img_1.shape

    for i in range(m - 1):
        for j in range(n - 1):
            if (img_1[i, j] == mask[0][0]):
                control_a = True
            if (img_1[i, j + 1] == mask[0][1]):
                control_b = True
            if (img_1[i + 1, j] == mask[1][0]):
                control_c = True
            if (img_1[i + 1, j + 1] == mask[1][1]):
                control_d = True
            if (control_a and control_b and control_c and control_d):
                counter = counter + 1
    return counter


def count_internal_mask(image):
    # i_m = [internal_mask_1, internal_mask_2, internal_mask_3, internal_mask_4]
    i_m = [0, 0, 0, 0]

    counter_internal = 0
    for mask in i_m:
        counter_internal = counter_internal + count_mask(img_1, mask)
    return counter_internal


def count_external_mask(image):
    # e_m = [external_mask_1, external_mask_2, external_mask_3, external_mask_4]
    e_m = [0, 0, 0, 0]
    counter_external = 0
    for mask in e_m:
        counter_external = counter_external + count_mask(img_1, mask)
    return counter_external


# It needs test image
test_image = plt.imread("test.jpg")

c1 = count_internal_mask(test_image)
c2 = count_external_mask(test_image)
math.abs(c1 - c2) / 4
plt.imshow(test_image, cmap='Greys', interpolation='nearest')
plt.show()

img_1 = np.random.randint(10)
size = 2
img_1 = np.random.randint(0,2,(size,size))
img_1 = np.matrix('0,0,0,0,0 ; 0,1,1,1,0 ; 0,0,1,0,0 ; 0,0,1,0,0; 0,0,0,0,0')

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()

img_test = plt.imread("test.jpg")
img_test.ndim()
img_test.shape()

plt.imshow(img_test)
plt.imshow(img_test[:,:,0,+10]) # red
plt.imshow(img_test[:,:,1,+10]) # green
plt.imshow(img_test[:,:,2,+10]) # blue
rgb_pixel = [0,0,0]
gray_level_pixel = 0

# rgb_pixel = [10,0,0]
# gray_level_pixel = 10
# rgb_pixel = [0,10,0]
# gray_level_pixel = 10
# rgb_pixel = [10,10,10]
# gray_level_pixel = 12


# rgb pixel to gray level
def rgb2gray(rgb):
    return rgb[0]/3 + rgb[1]/3 + rgb[2]/3
    # gray_level = gray_level / 3


def rgb2gray_image(input_image):
    three_d_image = plt.imread(input_image)
    two_d_image = np.zeros(three_d_image.shape[0], three_d_image.shape[1])
    for i in range(three_d_image.shape[0]):
        for j in range(three_d_image.shape[1]):
            two_d_image[i, j]= three_d_image[0]/3 + three_d_image[1]/3 + three_d_image[2]/3

    scipy.misc.imsave(three_d_image + "_gray.jpg", two_d_image)

    plt.subplot(1, 2, 1)
    plt.imshow(three_d_image)
    plt.subplot(1, 2, 2)
    plt.imshow(img_2, cmap='gray')
    plt.show()


rgb2gray_image(img_test)

rgb2gray([2,5,7])
img_1 = plt.imread("test.jpg")
img_2 = np.zeros((img_1.shape[0],img_1.shape[1]))

for i in range(img_1.shape[0]):
    for j in range(img_2.shape[1]):
        img_2[i, j] = rgb2gray(img_1[i, j, :])

plt.subplot(1, 2, 1)
plt.imshow(img_1)
plt.subplot(1, 2, 2)
plt.imshow(img_2, cmap='gray')
plt.show()
scipy.misc.imread()

img_var = plt.imread("var.jpg")
img_yok = plt.imread("yok.jpg")

plt.imshow(img_yok - img_var)
plt.show()


def rgb2gray_image(input_image):
    using_image = plt.imread(input_image)

    # two_d_image = np.zeros(three_d_image.shape[0:2])
    gray_image = np.zeros(using_image.shape[0], using_image.shape[1])
    binary_image = np.zeros(using_image.shape[0], using_image.shape[1])

    threshold = 200

    for i in range(using_image.shape[0]):
        for j in range(using_image.shape[1]):
            n = using_image[i, j, 0] / 3 + using_image[i, j, 1] / 3 + using_image[i, j, 2] / 3
            gray_image[i, j] = n

            # if n>100:
            if n > threshold:
                binary_image[i,j] = 255
                # threshold_image[i, j] = 255

            else:
                binary_image[i, j] = 0
                # threshold_image[i, j] = 0

    scipy.misc.imsave(using_image + "_gray.jpg", gray_image)
    scipy.misc.imsave(binary_image + "_binary.jpg", binary_image)

    # plt.imshow(two_d_image, plt.cm.gray)
    # plt.imshow(two_d_image, plt.cm.binary)

    plt.subplot(1,3,1),plt.imshow(input_image)
    plt.subplot(1,3,2),plt.imshow(gray_image, plt.cm.gray)
    plt.subplot(1,3,3),plt.imshow(binary_image, plt.cm.binary)


img_test = plt.imread("test.jpg")
rgb2gray_image(img_test)