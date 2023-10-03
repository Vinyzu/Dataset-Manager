from common import get_labels_images, PATH, LABELS

count_per_label = [0] * len(LABELS)

for label, image in get_labels_images(PATH):
    annotations = open(label, "r").read().splitlines()
    for annotation in annotations:
        annotation_label = int(annotation.split(" ")[0])
        count_per_label[annotation_label] += 1

print(dict(zip(LABELS, count_per_label)))
