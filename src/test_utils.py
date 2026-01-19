import unittest
from textnode import TextNode, TextType
from utils import text_node_to_html_node, split_nodes_delimiter

class TestUtils(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.PlainText)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_spliting_text_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.PlainText)
        new_nodes = split_nodes_delimiter([node], "`", TextType.Code)

        expected_result = [
                            TextNode("This is text with a ", TextType.PlainText),
                            TextNode("code block", TextType.Code),
                            TextNode(" word", TextType.PlainText),
                          ]

        self.assertEqual(new_nodes, expected_result)

        node2 = TextNode("This is text with a **bolded phrase** in the middle", TextType.PlainText)

        new_nodes2 = split_nodes_delimiter([node2], "**", TextType.BoldText)

        expected_result2 = [
                                TextNode("This is text with a ", TextType.PlainText),
                                TextNode("bolded phrase", TextType.BoldText),
                                TextNode(" in the middle", TextType.PlainText),
                            ]

        self.assertEqual(new_nodes2, expected_result2)

if __name__ == "__main__":
    unittest.main()