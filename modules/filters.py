import random
import cv2
import numpy as np


def cartoon_edit(image_name):
    image = cv2.imread(image_name)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)

    color = cv2.bilateralFilter(image, 12, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    name = f'images/cartoon{random.randint(1, 100)}.jpg'
    cv2.imwrite(name, cartoon)
    return name


def blur_edit(image_name):
    image = cv2.imread(image_name)

    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayImage = cv2.GaussianBlur(grayImage, (3, 3), 0)
    edgeImage = cv2.Laplacian(grayImage, -1, ksize=5)
    edgeImage = 255 - edgeImage

    ret, edgeImage = cv2.threshold(edgeImage, 150, 255, cv2.THRESH_BINARY)

    edgePreservingImage = cv2.edgePreservingFilter(image, flags=2, sigma_s=50, sigma_r=0.4)

    output = np.zeros(grayImage.shape)

    blur = cv2.bitwise_and(edgePreservingImage, edgePreservingImage, mask=edgeImage)

    name = f'images/blur{random.randint(1, 100)}.jpg'
    cv2.imwrite(name, blur)
    return name


def style_edit(image_name):
    image = cv2.imread(image_name)

    style_image = cv2.stylization(image, sigma_s=150, sigma_r=0.25)

    name = f'images/style{random.randint(1, 100)}.jpg'
    cv2.imwrite(name, style_image)
    return name


def sketch1_edit(image_name):
    image = cv2.imread(image_name)

    sketch_image1, sketch_image2 = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.5, shade_factor=0.02)

    name = f'images/sketch1{random.randint(1, 100)}.jpg'
    cv2.imwrite(name, sketch_image1)
    return name


def sketch2_edit(image_name):
    image = cv2.imread(image_name)

    sketch_image1, sketch_image2 = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.5, shade_factor=0.02)

    name = f'images/sketch2{random.randint(1, 100)}.jpg'
    cv2.imwrite(name, sketch_image2)
    return name
