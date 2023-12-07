import os
import csv
import shutil


def replace_images(class_name: str) -> list[str]:
    """
    Данная функция изменяет имена изображений и переносит их в другую директорию
    """
    relative_path = os.path.relpath("dataset_2")
    class_path = os.path.join(relative_path, class_name)
    image_names = os.listdir(class_path)
    image_rel_paths = [os.path.join(class_path, name) for name in image_names]
    new_image_names = [f"{class_name}_{name}" for name in image_names]
    new_image_rel_paths = [
        os.path.join(relative_path, name) for name in new_image_names
    ]
    for old, new in zip(image_rel_paths, new_image_rel_paths):
        os.replace(old, new)

    os.chdir("dataset_2")

    if os.path.isdir(class_name):
        os.rmdir(class_name)

    os.chdir("..")


def getting_absolute_path(class_name: str) -> list[str]:
    """
    Данная функция возвращает список измененных абсолютных путей для изображений
    """
    absolute_path = os.path.abspath("dataset_2")
    image_names = os.listdir(absolute_path)
    image_class_names = []
    for name in image_names:
        if class_name in name:
            image_class_names.append(name)
    image_absolute_path = [os.path.join(absolute_path, name) for name in image_names]

    return image_absolute_path


def getting_relative_path(class_name: str) -> list[str]:
    """
    Данная функция возвращает список измененных относительных путей для изображений
    """
    relative_path = os.path.relpath("dataset_2")
    image_names = os.listdir(relative_path)
    image_class_names = []
    for name in image_names:
        if class_name in name:
            image_class_names.append(name)
    image_relative_path = [os.path.join(relative_path, name) for name in image_names]

    return image_relative_path


def dataset_2() -> None:
    """
    Данная функция создает dataset_2
    """
    first_class = "cat"
    second_class = "dog"

    if os.path.isdir("dataset_2"):
        shutil.rmtree("dataset_2")

    path_dataset_1 = os.path.relpath("dataset_1")
    path_dataset_2 = os.path.relpath("dataset_2")
    shutil.copytree(path_dataset_1, path_dataset_2)

    replace_images(first_class)
    replace_images(second_class)


def second_annotation() -> None:
    """
    Данная функция создает аннотацию
    """
    first_class = "cat"
    second_class = "dog"

    dog_abs_paths = getting_absolute_path(first_class)
    dog_rel_paths = getting_relative_path(first_class)
    cat_abs_paths = getting_absolute_path(second_class)
    cat_rel_paths = getting_relative_path(second_class)

    with open("paths_2.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", lineterminator="\r")
        for abs_path, rel_path in zip(dog_abs_paths, dog_rel_paths):
            writer.writerow([abs_path, rel_path, first_class])
        for abs_path, rel_path in zip(cat_abs_paths, cat_rel_paths):
            writer.writerow([abs_path, rel_path, second_class])
