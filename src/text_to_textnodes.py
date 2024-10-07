from textnode import TextNode
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image_and_link import split_nodes_link, split_nodes_image


def text_to_textnodes(text):
    bold_splits = split_nodes_delimiter([TextNode(text, "text")], "**", "bold")
    code_splits = split_nodes_delimiter(bold_splits, "`", "code")
    italic_splits = split_nodes_delimiter(code_splits, "*", "italic")
    image_splits = split_nodes_image(italic_splits)
    final_splits = split_nodes_link(image_splits)


    return final_splits








