import cv2
import numpy as np

def main():
    input_img = cv2.imread('pokeball.png')
    max_x, max_y, _ = input_img.shape
    d=22
    dx, dy = d, d
    output_img = np.array( [[0 for _ in range(int(max_x/dy))] for _ in range(int(max_y/dy))] )
    for x in range(0, max_x+1, dx):
        for y in range(0, max_y+1, dy):
            avg = np.average(input_img[x-1, y-1])
            output_img[int(x/dx)-1][int(y/dy)-1]=avg

    output_img.transpose()

    for row in output_img:
        print(row)

if __name__ == "__main__":
    main()
