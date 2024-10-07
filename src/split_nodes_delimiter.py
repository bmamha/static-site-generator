from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_nodes_list = []

    text_type_text = "text"
    text_type_code = "code"
    text_type_bold = "bold"
    text_type_italic = "italic"
    

   
    if delimiter not in ["*", "**", "`"]:
        raise Exception("invalid mark down syntax")


    for node in old_nodes:
        text_nodes = []
        if node.text_type != text_type_text:
            text_nodes_list.append(TextNode(node.text, node.text_type))
            continue
            

        split_text = node.text.split(delimiter)
        for i in range(len(split_text)):
            if i % 2 == 0 and len(split_text[i]) > 0:
                text_nodes.append(TextNode(split_text[i], text_type_text))
            
            if i % 2 != 0:
                if delimiter == "`":
                    text_nodes.append(TextNode(split_text[i], text_type_code))
                
                if delimiter == "*":
                    text_nodes.append(TextNode(split_text[i], text_type_italic))
                
                if delimiter == "**":
                    text_nodes.append(TextNode(split_text[i], text_type_bold))
                
                
        text_nodes_list.extend(text_nodes)
    
    return text_nodes_list







