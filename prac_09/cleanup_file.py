import os


def main():
    """Program to consistently name files."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

    for filename in filenames:
        new_name = get_fixed_filename(filename)
        print(f"{filename} -> {new_name}")
        full_name = os.path.join(directory_name, filename)
        new_name = os.path.join(directory_name, new_name)
        os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    name = ''
    filename.replace(" ", "_").replace(".TXT", ".txt")
    for letter in filename:
        if len(name) != 0:
            if name[-1].islower() and letter.isupper():
                name += "_"
        name += letter
    return name


main()