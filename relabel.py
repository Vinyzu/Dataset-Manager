from common import get_labels, PATH

old_labels = [int(item) for item in input("Input the Label Indexes of the old Indexes (Example: `2, 9, 14`): ").replace(" ", "").split(",")]
new_labels = [int(item) for item in input("Input the Label Indexes of the new Indexes (Example: `1, 3, 6`): ").replace(" ", "").split(",")]
relabelled_labels = {x: y for x, y in zip(old_labels, new_labels)}

for label in get_labels(PATH):
    new_lines = []
    annotations = open(label, "r").read().splitlines()
    for annotation in annotations:
        try:
            annotation_label, annotation_rest = annotation.split(" ", 1)
            if int(annotation_label) in relabelled_labels:
                new_lines.append(f"{relabelled_labels[int(annotation_label)]} {annotation_rest}")
        except ValueError:
            continue

    with open(label, "w") as f:
        f.write("\n".join(new_lines))

print(f"Unwanted Labels from Path {PATH} successfully removed.")
