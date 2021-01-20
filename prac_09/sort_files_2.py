import os
import shutil


def main():


    extension_to_category = {}
    os.chdir("FilesToSort")

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input(f"What category would you like to sort {extension} files into? ")
            extension_to_category[extension] = category
            if os.path.exists(category):
                pass
            else:
                os.mkdir(category)
            shutil.move(filename, category)


main()