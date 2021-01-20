import os
import shutil

EXTENSIONS = ["txt", "xlsx", "xls", "png", "jpg", "gif", "docx", "doc"]


def main():
    """Move files into their respective folders based on extension."""

    os.chdir("FilesToSort")
    make_extension_folders()
    move_file_to_directory()


def make_extension_folders():
    """Create required folder structure as per EXTENSIONS list."""
    for extension in EXTENSIONS:
        if os.path.exists(extension):
            pass
        else:
            os.mkdir(extension)


def move_file_to_directory():
    """Loop through files and move each file to directory"""
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        shutil.move(filename, extension)


main()