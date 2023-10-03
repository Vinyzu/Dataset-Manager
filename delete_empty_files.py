import os
from common import get_labels_images, PATH

path = r""
for label, image in get_labels_images(PATH):
    try:
        if not open(label, "r").read():
            os.remove(label)
            os.remove(image)
    except FileNotFoundError:
        pass

print(f"Empty Files from Path {PATH} successfully removed.")
