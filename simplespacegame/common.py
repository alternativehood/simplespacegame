import os


RESOURCES_PATH = os.path.join('rc')


def resource_path(path: str):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), RESOURCES_PATH, path)
