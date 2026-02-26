import os
from shutil import copy, rmtree


def copy_files_recursive(source_dir, destination_dir):
    if os.path.exists(source_dir):
        if os.path.exists(destination_dir):
            print(f"Removing: {destination_dir}")
            rmtree(destination_dir)
        print(f"Creating: {destination_dir}")
        os.mkdir(destination_dir)
        listing = os.listdir(source_dir)
        for item in listing:
            item_path = os.path.join(source_dir, item)
            destination = os.path.join(destination_dir, item)
            if os.path.isfile(item_path):
                print(f"Copying {item_path} to {destination}")
                copy(item_path, destination)
            elif os.path.isdir(item_path):
                print(f"Entering directoy: {item_path}")
                copy_files_recursive(item_path, destination)
    else:
        raise ValueError("invalid source directory")
