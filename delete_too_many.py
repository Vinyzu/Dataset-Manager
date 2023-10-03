from common import get_labels_images, PATH, LABELS

# Set this Variable to the Maximum Amount of variab
max_per_label = int(input("Maximum Amount of Annotations per Label: "))
count_per_label = [0] * len(LABELS)

for label, image in get_labels_images(PATH):
    new_lines = []
    annotations = open(label, "r").read().splitlines()
    for annotation in annotations:
        annotation_label = int(annotation.split(" ")[0])
        count_per_label[annotation_label] += 1
        if count_per_label[annotation_label] <= 203:
            new_lines.append(annotation)

        with open(label, "w") as f:
            f.write("\n".join(new_lines))

print(f"Amount from Path {PATH} successfully removed.")
