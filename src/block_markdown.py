
def markdown_to_blocks(markdown: str) -> list[str]:
    # Currently we are distinguishing blocks with help of \n\n characted
    # but this needs to be improved in future

    blocksStrings = markdown.split("\n\n")

    blocks = []
    # remove trailing spaces
    for blockString in blocksStrings:
        if len(blockString) == 0:
            continue
        
        blocks.append(blockString.strip())

    return blocks