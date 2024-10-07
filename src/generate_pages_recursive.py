from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files_in_dir = os.listdir(dir_path_content)
    print(f"...Listing director names {files_in_dir}")
    
    with open(template_path, "r") as file:
        template_content = file.read()
    
    for item in files_in_dir:
        file_path = os.path.join(dir_path_content, item)

        if os.path.isfile(file_path):
            print(f"{file_path} is a file")
            with open(file_path, "r") as file:
                file_content = file.read()
            
            html_content = markdown_to_html_node(file_content).to_html()
            title = extract_title(file_content)

            generated_html_page = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
            file_name = item.split(".")[0] + ".html"

            destination_page = os.path.join(dest_dir_path, file_name)

            if not os.path.exists(os.path.dirname(destination_page)):
                print("Making the directory as it does not exist")
                os.makedirs(os.path.dirname(destination_page))

            with open(destination_page, "w") as file:
                print("Writing into file")
                file.write(generated_html_page)
        
        else:
            print(f"{file_path} is a directory")
            new_dir_path_content = os.path.join(dir_path_content, item)
            print(new_dir_path_content)
            new_dest_dir_path = os.path.join(dest_dir_path,item)
            print(new_dest_dir_path)
            generate_pages_recursive(new_dir_path_content, template_path, new_dest_dir_path)


