import cv2
import numpy as np

def convert_image_to_array(image, d):
    max_x, max_y, _ = image.shape
    # separate dx, dy in case i want change "scaling" of output image
    dx, dy = d, d
    # empty array of size image_size / delta
    output_img = np.array( [[0]*int(max_x/dx) for _ in range(int(max_y/dy))] )
    for x in range(0, max_x+1, dx):
        for y in range(0, max_y+1, dy):
            avg = np.average(image[x-1, y-1])
            output_img[int(x/dx)-1][int(y/dy)-1]=avg
    output_img.transpose()
    return output_img

def main():
    input_img = cv2.imread('pokeball.png')
    output_img = convert_image_to_array(input_img, 22)
    for row in output_img:
        print(row)

if __name__ == "__main__":
    main()
