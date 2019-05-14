from PIL import Image


def main():
    image = Image.open('F:\\201905122138059881-1559530.jpg')
    # image.format, image.size, image.mode('JPEG', (500, 750), 'RGB')
    # image.format = 'JPEG'
    size = 128, 128
    image.thumbnail(size)
    # image.mode = 'RGB'
    image.show()


if __name__ == "__main__":
    main()