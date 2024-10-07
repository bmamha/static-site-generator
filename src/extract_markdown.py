import re
def extract_markdown_images(text):
    images_list = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images_list


def extract_markdown_links(text):
    links_list = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return links_list

