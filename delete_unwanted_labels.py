from common import get_labels, PATH

wanted_labels = [int(item) for item in input("Input the Label Indexes you want to keep (Example: `2, 9, 14`): ").replace(" ", "").split(",")]

for label in get_labels(PATH):
    new_lines = []
    annotations = open(label, "r").read().splitlines()
    for annotation in annotations:
        try:
            if int(annotation.split(" ")[0]) in wanted_labels:
                new_lines.append(annotation)
        except ValueError:
            continue

    with open(label, "w") as f:
        f.write("\n".join(new_lines))

print(f"Unwanted Labels from Path {PATH} successfully removed.")
