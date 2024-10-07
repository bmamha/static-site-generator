def markdown_to_blocks(text):
    text_blocks = text.split("\n\n")
    stripped_text_blocks = [line.strip() for line in text_blocks]
    return stripped_text_blocks


    


