from enum import Enum
from utils import text_to_textnodes, text_node_to_html_node
from parentnode import ParentNode
from htmlnode import HTMLNode

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
    # remove any whitespaces if present
    # doing this for testcase strings
    block = block.strip()

    if len(block) < 5:
        return False
    
    slicedStr = block[:4]

    if slicedStr != "```\n":
        return False
    
    # Now check the ending 3 characters
    slicedStrEnd = block[-3:]

    if slicedStrEnd != "```":
        return False

    return True

def check_quote_block_type(block: str) -> bool:
    # each block line must start with "> " characters

    # Currently we want each line in block quote to start with "> "
    # But this can be improved further
    # take example from https://commonmark.org/help/tutorial/05-blockquotes.html

    lines = block.split("\n")

    for line in lines:
        if len(line) == 0:
            continue
        
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
        if len(line) == 0:
            continue

        lineAfterWhitespaceRemoval = line.lstrip()

        specialChars = lineAfterWhitespaceRemoval[:2]

        if specialChars != "- ":
            return False

    return True

def check_ordered_list_block_type(block: str) -> bool:
    # each block line must start a number followed by ". "

    lines = block.split("\n")

    for line in lines:
        if len(line) == 0:
            continue
        
        lineAfterWhitespaceRemoval = line.lstrip()

        isDigit: bool = lineAfterWhitespaceRemoval[0].isdigit()

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

    if check_ordered_list_block_type(block):
        return BlockType.ORDERED_LIST
    
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

def heading_block_to_html_node(block: str) -> HTMLNode:
    #find the type of heading
    index = 0
    countPoundSign = 0
    foundPoundSign = False

    while block[index] == '#':
        index += 1
        countPoundSign += 1

    tag :str = f"h{countPoundSign}"

    #create LeafNodes of heading
    text = block[index + 1:]

    textNodes = text_to_textnodes(text)

    childHtmlNodes = []
    for textNode in textNodes:
        childHtmlNodes.append(text_node_to_html_node(textNode))

    #create Parent Node for heading tag
    headingHtmlNode = ParentNode(tag = tag, children = childHtmlNodes)

    return headingHtmlNode

def paragraph_block_to_html_node(block: str) -> HTMLNode:
    # the paragraph may contain italics and bolds

    textNodes = text_to_textnodes(block)

    childHtmlNodes = []

    for textNode in textNodes:
        childHtmlNodes.append(text_node_to_html_node(textNode))

    paragraphHtmlNode = ParentNode(tag="p", children=childHtmlNodes)

    return paragraphHtmlNode
    

def markdown_to_html(markdown: str) -> HTMLNode:

    #split markdown into separate blocks
    blocks = markdown_to_blocks(markdown)

    generatedHtmlNodes = []
    for block in blocks:
        blockType = block_to_block_type(block)

        match blockType:
            case BlockType.HEADING:
                #call function associated with heading
                generatedHtmlNodes.append(heading_block_to_html_node(block))
            case BlockType.PARAGRAPH:
                generatedHtmlNodes.append(paragraph_block_to_html_node(block))
            case _:
                raise Exception("Processing Error: Invalid BlockType")
            
    
    parentHtmlNode = ParentNode(tag="div", children=generatedHtmlNodes)

    return parentHtmlNode