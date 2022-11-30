import cv2
import numpy as np
import math

def rgb_to_gray(r, g, b):
    return np.average([r, g, b])

def convert_image_to_array(image, d):
    img_width, img_height, _ = image.shape
    # separate dx, dy in case i want change "scaling" of output image
    dx, dy = d, d
    # empty array of size image_size / delta
    output_img = [[0] * math.ceil(img_width/dx)  for _ in range(math.ceil(img_height/dy))]
    for y, row in enumerate(output_img):
        for x in range(len(row)):
            avg = rgb_to_gray(*image[x*dx, y*dy])
            output_img[y][x]=math.floor(avg)

    return output_img

def main():
    # input_img = cv2.imread('pokeball.png')
    input_img = cv2.imread('fox.jpg')
    output_img = convert_image_to_array(input_img, 22)
    for row in output_img:
        print(row)

if __name__ == "__main__":
    main()
