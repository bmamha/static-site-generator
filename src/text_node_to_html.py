from htmlnode import HTMLNode, LeafNode 
from textnode import TextNode

def text_node_to_html_node(text_node):
    
    type = text_node.text_type

    match type:
        case "text":
            return LeafNode("", text_node.text)
    
        case "bold":
            return LeafNode("b", text_node.text)
    
        case "italic":
            return LeafNode("i", text_node.text)
    
        case "code":
            return LeafNode("code", text_node.text)
    
        case "link":
            return LeafNode("a",text_node.text, {"href": text_node.url})
    
        case "image":
            return LeafNode("img","", {"src": text_node.url, "alt": text_node.text})
        
        case _:
            raise Exception("not proper text_type")
        
    