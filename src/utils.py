from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
import re


def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.PlainText:
            return LeafNode(None, text_node.text)
        case TextType.BoldText:
            return LeafNode("b", text_node.text)
        case TextType.ItalicText:
            return LeafNode("i", text_node.text)
        case TextType.Code:
            return LeafNode("code", text_node.text)
        case TextType.Link:
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
        if old_node.text_type != TextType.PlainText:
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
                new_nodes.append(TextNode(textSliced, TextType.PlainText))
            else:
                new_nodes.append(TextNode(textSliced, text_type))

            index = index + 1
            startIndex = curMatch.end()
            isPlainText = not isPlainText
        
        # covers up a case where a plain text block is present in the end
        if (startIndex < len(textToSplit)):
            new_nodes.append(TextNode(textToSplit[startIndex: len(textToSplit)], TextType.PlainText))

    return new_nodes
