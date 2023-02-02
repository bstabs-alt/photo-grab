import os

path = "E:\DCIM"

def main():

    photofolders = [ f.name for f in os.scandir(path) if f.is_dir() and not f.name.startswith('.') ]
    print(photofolders)

if __name__ == "__main__":
    main()
