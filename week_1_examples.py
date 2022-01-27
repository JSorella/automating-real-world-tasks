import PIL
from PIL import Image


def print_help():
    print(help(PIL))


def open_teacup_45():
    im = Image.open("teacup.jpg")
    im.rotate(45).show()


def resize_image_and_save_new_image_with_new_name():
    im = Image.open("teacup.jpg")
    new_im = im.resize((640, 480))
    new_im.save("example_resized.jpg")


def rotate_resize_and_save():
    im = Image.open("teacup.jpg")
    im.rotate(180).resize((640, 480)).save("flipped_and_resized.jpg")


if __name__ == '__main__':
    rotate_resize_and_save()
