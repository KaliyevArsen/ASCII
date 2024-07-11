import PIL
import PIL.Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, new_width=200):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image


def pixels_to_ascii(image):
    pixels = image.getdata()
    scale_factor = 255 // (len(ASCII_CHARS) - 1)
    characters = "".join(ASCII_CHARS[pixel // scale_factor]
                         for pixel in pixels)
    return characters


def main(new_width=200):
    photo = input()
    try:
        image = PIL.Image.open(photo)
    except Exception as e:
        print(e)
        return

    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[index:(
        index + new_width)] for index in range(0, pixel_count, new_width))

    print(ascii_image)

    with open(f"{photo}.txt", "w") as f:
        f.write(ascii_image)


main()
