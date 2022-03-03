#!/usr/bin/env python3

from math import floor

from PIL import Image


def main(image):

    # image.show()
    w, h = image.size
    pixels = list(image.getdata())

    if len(pixels[0]) != 3:
        print("Pixels is not RGB. Given pixel data = " + str(pixels[0]))
        return

    average_colour_pixels = []

    for pixel in pixels:
        average_colour = sum(pixel) / len(pixel)  # Getting the average value from the RBG values
        average_colour_pixels.append(average_colour)

    density_chars = "Ñ@#W$9876543210?!abc;:+=-,._      "
    # density_chars = "_.,-=+:;cba!?0123456789$W#@Ñ   "
    density_chars_len = len(density_chars)
    pixel_index_count = 0
    string_buffer = []
    for y in range(h):
        for x in range(w):
            average_colour_pixel = average_colour_pixels[pixel_index_count]

            density_index = floor((average_colour_pixel * density_chars_len) / 255)

            string_buffer.append(density_chars[density_index - 1])
            pixel_index_count += 1
        print("".join(string_buffer))
        string_buffer.clear()


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Specify image")
        print("Usage: python3 ascii.py blake_oakfield.jpg")
        exit()

    image_path = sys.argv[1]
    img = Image.open(image_path)
    main(img)
    img.close()
