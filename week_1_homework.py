import os
from PIL import Image


def rotate_resize_and_save(source_folder, file_name, destination_folder):
    try:
        im = Image.open("{}/{}".format(source_folder, file_name))
        new_img = im.rotate(-90).resize((128, 128)).convert("RGB")

        destination_file_name = file_name

        if not os.path.exists(destination_folder):
            os.mkdir(destination_folder)
        new_img.save("{}/{}".format(destination_folder, destination_file_name), "JPEG")
    except IOError:
        print("This file is not an image: {}".format(file_name))


if __name__ == '__main__':
    environment = "prod"

    if environment == "local":
        source_folder = "{}/images".format(os.getcwd())
        destination_folder = "converted_images"
    elif environment == "prod":
        source_folder = "{}/images".format(os.getcwd())
        destination_folder = "/opt/icons"
    else:
        raise ValueError("Unexpected environment.")

    for filename in os.listdir(source_folder):
        rotate_resize_and_save(source_folder, filename, destination_folder)

