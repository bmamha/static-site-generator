from textnode import TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links
import re


def split_nodes_link(old_nodes):

    text_nodes_list = []
    
    
    for node in old_nodes:
            
        text_nodes = []
        links = extract_markdown_links(node.text)
        original_text = node.text
        

        if len(links) == 0:
            text_nodes_list.append(node)
        
        for title,url in links:
            sections = original_text.split(f"[{title}]({url})", 1)
            if len(sections[0]) > 0:
                text_nodes.append(TextNode(sections[0], "text"))
            text_nodes.append(TextNode(title, "link", url))
            original_text = sections[1]

            if len(extract_markdown_links(original_text)) == 0 and len(original_text) > 0:
                text_nodes.append(TextNode(original_text,"text"))


        text_nodes_list.extend(text_nodes)

    
    return text_nodes_list


def split_nodes_image(old_nodes):
    text_nodes_list = []
    
    
    for node in old_nodes:
        text_nodes = []
        links = extract_markdown_images(node.text)
        if len(links) == 0:
            text_nodes_list.append(node)
        
        original_text = node.text
        
        
        for img,img_url in links:
            sections = original_text.split(f"![{img}]({img_url})", 1)

            if len(sections[0]) > 0:
                text_nodes.append(TextNode(sections[0], "text"))
            text_nodes.append(TextNode(img, "image", img_url))
            original_text = sections[1]
            

            if len(extract_markdown_images(original_text)) == 0 and len(original_text) > 0:
                text_nodes.append(TextNode(original_text,"text"))

        text_nodes_list.extend(text_nodes)
    
    
    return text_nodes_list

            

            



        
