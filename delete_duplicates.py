import os
from common import get_labels_images, PATH

used_imgs = []

labels, images = list(zip(*get_labels_images(PATH)))
for label, image in zip(labels, images):
    try:
        file_name = label.split("\\")[-1]
        prefix = file_name.split(".")[0]
        if prefix in used_imgs:
            os.remove(label)
            os.remove(image)
        else:
            used_imgs.append(prefix)
    except FileNotFoundError:
        pass

print(f"Duplicates from Path {PATH} successfully removed.")
