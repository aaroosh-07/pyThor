from enum import Enum

class BlockType(Enum):
    PARAGRAPH: str = "Paragraph"
    HEADING: str = "Heading"
    CODE: str = "Code"
    QUOTE: str = "Quote"
    UNORDERED_LIST: str = "Unordered List"
    ORDERED_LIST: str = "Ordered List"

def check_heading_block_type(block: str) -> bool:
    index = 0
    countPoundSign = 0
    foundPoundSign = False

    while block[index] == '#':
        index += 1
        countPoundSign += 1

    if block[index] == ' ' and countPoundSign < 7:
        return True

    return False

def check_code_block_type(block: str) -> bool:
    if len(block) < 4:
        return False
    
    slicedStr = block[:4]

    if slicedStr != "```\n"
        return False
    
    # Now check the ending 3 characters
    slicedStrEnd = block[-3:]

    if slicedStrEnd != "```"
        return False

    return True

def check_quote_block_type(block: str) -> bool:
    # each block line must start with "> " characters

    # Currently we want each line in block quote to start with "> "
    # But this can be improved further
    # take example from https://commonmark.org/help/tutorial/05-blockquotes.html

    lines = block.split("\n")

    for line in lines:
        whitespacesRemovedLine = line.lstrip()
        specialChars = whitespacesRemovedLine[:2]

        if specialChars != "> ":
            return False
    
    return True

def check_unordered_list_block_type(block: str) -> bool:
    # each block line must start with "- " characters

    # currently we do not support indentation inside unordered list
    # this can be taken up in the future

    lines = block.split("\n")

    for line in lines:
        lineAfterWhitespaceRemoval = line.lstrip()

        specialChars = lineAfterWhitespaceRemoval[:2]

        if specialChars != "- ":
            return False

    return True

def check_ordered_list_block_type(block: str) -> bool:
    # each block line must start a number followed by ". "

    lines = block.split("\n")

    for line in lines:
        lineAfterWhitespaceRemoval = line.lstrip()

        isDigit: bool = lineAfterWhitespaceRemoval[0].isDigit()

        specialChars = lineAfterWhitespaceRemoval[1:3]

        if not isDigit or specialChars != ". ":
            return False

    return True

def block_to_block_type(block: str) -> BlockType:
    # check for heading blockType
    if check_heading_block_type(block):
        return BlockType.HEADING
    
    if check_code_block_type(block):
        return BlockType.CODE

    if check_quote_block_type(block):
        return BlockType.QUOTE

    if check_unordered_list_block_type(block):
        return BlockType.UNORDERED_LIST
    
    return BlockType.PARAGRAPH


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