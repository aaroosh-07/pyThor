from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
import re


def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BoldText:
            return LeafNode("b", text_node.text)
        case TextType.ItalicText:
            return LeafNode("i", text_node.text)
        case TextType.Code:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            props = dict()
            props["href"] = text_node.link
            return LeafNode("a", text_node.text, props)
        case TextType.Images:
            props = dict()
            props["src"] = text_node.link
            props["alt"] = text_node.text
            return HTMLNode(tag = "img", props= props)
        case _:
            raise Exception("Cannot find TextType specified")


def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType):
    new_nodes = list()

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        textToSplit = old_node.text
        if textToSplit.count(delimiter) % 2 == 1:
            raise Exception("Markdown Syntax error: Delimiter not present in pairs")

        #Find all occurences of delimiter
        matches = list(re.finditer(re.escape(delimiter), textToSplit))

        index = 0
        startIndex = 0
        isPlainText = True

        while startIndex < len(textToSplit) and index < len(matches):
            curMatch = matches[index]
            textSliced = textToSplit[startIndex: curMatch.start()]

            if isPlainText:
                new_nodes.append(TextNode(textSliced, TextType.TEXT))
            else:
                new_nodes.append(TextNode(textSliced, text_type))

            index = index + 1
            startIndex = curMatch.end()
            isPlainText = not isPlainText
        
        # covers up a case where a plain text block is present in the end
        if (startIndex < len(textToSplit)):
            new_nodes.append(TextNode(textToSplit[startIndex: len(textToSplit)], TextType.TEXT))

    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]] :
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return matches

def extract_markdown_links(text: str) -> list[tuple[str, str]] :
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return matches

def split_nodes_image(old_nodes: list) -> list:
    # Split text according to regex expresssion
    # if block of text starts with ! then its a image in markdown
    # or use extract markdown images function call

    new_nodes = []
    for old_node in old_nodes:
        textSections = re.split(r"(!\[[^\[\]]*\]\([^\(\)]*\))", old_node.text)

        for section in textSections:
            # if a image then extract tuple
            extractedImageMarkdown = extract_markdown_images(section)

            if len(extractedImageMarkdown) == 0:
                # it is a TEXT type Node
                if len(section) == 0:
                    # if text is empty then move to next section
                    continue
                new_nodes.append(TextNode(section, TextType.TEXT))
            else:
                # it is a Image Node
                alt_text = extractedImageMarkdown[0][0]
                img_link = extractedImageMarkdown[0][1]
                new_nodes.append(TextNode(alt_text, TextType.Images, img_link))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        textSections = re.split(r"((?<!!)\[[^\[\]]*\]\([^\(\)]*\))", old_node.text)

        for sections in textSections:
            extractedLinkMarkdown = extract_markdown_links(sections)

            if len(extractedLinkMarkdown) == 0:
                # it is plain text node

                if len(sections) == 0:
                    continue
                
                new_nodes.append(TextNode(sections, TextType.TEXT))

            else:
                text = extractedLinkMarkdown[0][0]
                link = extractedLinkMarkdown[0][1]

                new_nodes.append(TextNode(text, TextType.LINK, link))
    
    return new_nodes

