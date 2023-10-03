from os import walk

# Set these variables to match your project
PATH = r""
LABELS = ['bridge', 'chimney', 'crosswalk', 'mountain or hill', 'palm tree', 'stair', 'tractor', 'taxi']

def get_labels(dir, file_extension=".txt"):
    for (dirpath, dirnames, filenames) in walk(dir):
        for file in filenames:
            if file.endswith(file_extension):
                yield f"{dirpath}\\{file}"

def get_image_from_label(file_path):
    return file_path.replace("\\labels\\", "\\images\\").replace(".txt", ".jpg")

def get_labels_images(dir):
    for label in get_labels(dir):
        yield label, get_image_from_label(label)
