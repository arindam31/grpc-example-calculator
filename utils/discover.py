# Helper functions
import os
from pathlib import Path


def find_all_proto_files(location):
    return os.listdir(location)


if __name__ == '__main__':
    proto_folder = Path(os.path.abspath(__file__)).parent.parent.joinpath('proto')
    files = find_all_proto_files(proto_folder)
    for file_ in files:
        print(file_)
