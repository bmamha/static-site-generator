


def extract_title(markdown):
    lines = markdown.split("\n")
    header = ""

    for line in lines:
        if line.startswith("# "):
            header += line.strip("# ")
            break
    
    if len(header) == 0:
        raise Exception("Markdown has no h1 header line")
    
    return header
    