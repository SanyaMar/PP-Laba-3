import os
import csv


def getting_absolute_path(images_class: str) -> list[str]:
    """
    Данная функция возвращает список list абсолютных путей изображений
    Parameters: class_name : str, second_dataset: str
    Returns: list
    """
    absolute_path = os.path.abspath("dataset_1")
    class_path = os.path.join(absolute_path, images_class)
    image_names = os.listdir(class_path)
    image_absolute_path = [os.path.join(class_path, name) for name in image_names]

    return image_absolute_path


def getting_relative_path(images_class: str) -> list[str]:
    """
    Данная функция возвращает список list относительных путей изображений(относительно dataset)
    Parameters: class_name : str, path_dataset: str
    Returns: list
    """
    relative_path = os.path.relpath("dataset_1")
    class_path = os.path.join(relative_path, images_class)
    image_names = os.listdir(class_path)
    image_relative_path = [os.path.join(class_path, name) for name in image_names]

    return image_relative_path


def first_annotation() -> None:
    """
    Данная функция создает аннотацию
    """
    first_class = "cat"
    second_class = "dog"

    cat_abs_paths = getting_absolute_path(first_class)
    cat_rel_paths = getting_relative_path(first_class)
    dog_abs_paths = getting_absolute_path(second_class)
    dog_rel_paths = getting_relative_path(second_class)

    with open("paths_1.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", lineterminator="\r")
        for abs_path, rel_path in zip(cat_abs_paths, cat_rel_paths):
            writer.writerow([abs_path, rel_path, first_class])
        for abs_path, rel_path in zip(dog_abs_paths, dog_rel_paths):
            writer.writerow([abs_path, rel_path, second_class])
