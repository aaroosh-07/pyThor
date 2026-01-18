from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode


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