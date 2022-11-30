import cv2
import numpy as np

def rgb_to_gray(r, g, b):
    return np.average([r, g, b])

def map_gray_to_char(val):
    t = val / 255
    density = 'Ñ@#W$9876543210?!abc;:+=-,._ '
    index = int(len(density)*t)
    return density[index-1]

def convert_image_to_array(image, d):
    img_width, img_height, _ = image.shape
    # separate dx, dy in case i want change "scaling" of output image
    dx, dy = d, d
    # empty array of size image_size / delta
    output_img = [['0' for _ in range(int(img_width/dx))]  for _ in range(int(img_height/dy))]
    for y in range(len(output_img)):
        for x in range(len(output_img[y])):
            avg = rgb_to_gray(*image[x*dx, y*dx])
            char = map_gray_to_char(avg)
            output_img[y][x]=char

    return np.array(output_img).transpose()

def main():
    input_img = cv2.imread('fox.jpg')
    output_img = convert_image_to_array(input_img, 5)
    for row in output_img:
        output = "".join(char for char in row)
        print(output)

if __name__ == "__main__":
    main()
