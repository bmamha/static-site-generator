from block_to_block_type import block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html import text_node_to_html_node



def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == "heading":
            heading_count, content = count_heading(block)
            node = ParentNode(f"h{heading_count}", text_to_children(content))
            children.append(node)
        
        if block_type == "quote":
            quote_text = extract_quotes(block)
            node = ParentNode("blockquote", text_to_children(quote_text))
            children.append(node)
        
        if block_type == "unordered_list":
            child_nodes = children_for_list(block)
            node = ParentNode("ul", child_nodes)
            children.append(node)
        
        if block_type == "ordered_list":
            child_nodes = children_for_list(block)
            node = ParentNode("ol",child_nodes)
            children.append(node)
        
        if block_type == "paragraph":
            node = ParentNode("p", text_to_children(block))
            children.append(node)

        if block_type == "code":
            child = children_for_code(block)
            node = ParentNode("pre", child)
            children.append(node)


    parent = ParentNode('div',children)

    return parent
            


def count_heading(heading):
    count = 0
    hash_strings = heading.split()[0]
    content = heading.split(hash_strings + " ")[1]
    return len(hash_strings), content


def children_for_list(unordered_list):
    children = [ ]
    items = unordered_list.split("\n")

    for item in items:
        differentiator = item.split(" ")[0]
        content = item.split(f"{differentiator} ")[1]
        children.append(ParentNode("li", text_to_children(content)))
    
    return children


def extract_quotes(blockquote):

    items = blockquote.split("\n")
    quote = ""

    for item in items:
        differentiator = item.split(" ")[0]
        content = item.split(f"{differentiator} ")[1]
        quote += content + " "
    
    quote = quote[:len(quote)-1]
    
    
    return quote


def children_for_code(code):
    code_text = code.split("```")[1]
    node = LeafNode("code", code_text)
    return [node]



def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes

