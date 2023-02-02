import os

path = "E:\DCIM"

def main():

    photofolders = [ f.path for f in os.scandir(path) if f.is_dir() ]
    print(photofolders)

if __name__ == "__main__":
    main()
