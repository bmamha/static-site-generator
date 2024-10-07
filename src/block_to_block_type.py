import re

def block_to_block_type(block):
    if re.search(r'^#{1,6} ', block):
        return 'heading'
    
    elif re.search(r'^```(.+)(\n*)```', block):
        return 'code'
    
    elif re.search(r'^(\*|-) ', block):
        list_lines = block.split('\n')
        if all([re.search(r'^(\*|\-) ', line) for line in list_lines]):
            return 'unordered_list'
        else:
            return 'paragraph'

    elif re.search(r'^(>|> )', block):
        list_lines = block.split('\n')
        if all([re.search(r'^>', line) for line in list_lines]):
            return 'quote'    
        else:
            return 'paragraph'
    
    elif re.search(r'^1. ', block):
        ordered_lines = block.split('\n')
        for i in range(len(ordered_lines)):
            if not re.search(rf'^{i+1}. ', ordered_lines[i]):
                return 'paragraph'
            
        return 'ordered_list'
    
    else:
        return 'paragraph'
        



