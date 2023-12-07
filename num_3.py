import os
import csv
import shutil
import random

random_numbers = random.sample(range(0, 10000), 2002)
new_names = [f"{number}.jpg" for number in random_numbers]


def dataset_3() -> None:
    """
    Данная функция создает dataset_3
    """
    if os.path.isdir("dataset_3"):
        shutil.rmtree("dataset_3")
    os.mkdir("dataset_3")

    old_paths = rel_paths()
    new_paths = new_rel_paths()

    for old_name, new_name in zip(old_paths, new_paths):
        shutil.copyfile(old_name, new_name)


def rel_paths() -> None:
    """
    Данная функция возвращает список старых относительных путей 
    """
    path_dataset_2 = os.path.relpath("dataset_2")
    names = os.listdir(path_dataset_2)

    path = [os.path.join(path_dataset_2, name) for name in names]
    rel_paths = list(path)

    return rel_paths


def new_rel_paths() -> None:
    """
    Данная функция возвращает список новых относительных путей 
    """
    path_dataset_3 = os.path.relpath("dataset_3")

    new_path = [os.path.join(path_dataset_3, name) for name in new_names]
    new_rel_paths = list(new_path)

    return new_rel_paths


def annotation_3() -> None:
    """
    Данная функция создает аннотацию
    """
    rel_path = rel_paths()
    abs_path = os.path.abspath("dataset_3")
    path = [os.path.join(abs_path, name) for name in new_names]
    new_abs_paths = list(path)

    new_rel_path = new_rel_paths()

    with open("paths_3.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", lineterminator="\r")
        for full_path, rel_path, old_rel_path in zip(
            new_abs_paths, new_rel_path, rel_path
        ):
            if "cat" in old_rel_path:
                class_name = "cat"
            else:
                class_name = "dog"
            writer.writerow([full_path, rel_path, class_name])
