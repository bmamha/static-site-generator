from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r" ) as file:
        source_content = file.read()
    with open(template_path, "r") as file:
        template_content = file.read()
    
    html_content = markdown_to_html_node(source_content).to_html()

    title = extract_title(source_content)
    generated_html_page = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    
    
    with open(dest_path, "w") as file:
        file.write(generated_html_page)






    

