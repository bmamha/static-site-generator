import os
import shutil
from copy_files import copy_files
from generate_pages_recursive import generate_pages_recursive



def main():
    print("Deleting public directory...")
    if os.path.exists("./public"):
        shutil.rmtree("./public")

    copy_files("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")



if __name__ == '__main__':
    main()