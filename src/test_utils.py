import unittest
from textnode import TextNode, TextType
from utils import text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, extract_markdown_links

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

        node3 = TextNode("This is text with a _italic text_ in the middle", TextType.PlainText)

        new_nodes3 = split_nodes_delimiter([node3], "_", TextType.ItalicText)

        expected_result3 = [
            TextNode("This is text with a ", TextType.PlainText),
            TextNode("italic text", TextType.ItalicText),
            TextNode(" in the middle", TextType.PlainText),
        ]

        self.assertEqual(new_nodes3, expected_result3)

    def test_spliting_text_nodes_multiple(self):
        node = TextNode("This is text with a `code block` word and another `code block`", TextType.PlainText)

        new_nodes = split_nodes_delimiter([node], "`", TextType.Code)

        expected_result = [
            TextNode("This is text with a ", TextType.PlainText),
            TextNode("code block", TextType.Code),
            TextNode(" word and another ", TextType.PlainText),
            TextNode("code block", TextType.Code),
        ]

        self.assertEqual(new_nodes, expected_result)

    def test_spliting_text_nodes_size_2(self):
        node1 = TextNode("This is text with a `code block` word and another `code block`", TextType.PlainText)
        node2 = TextNode("This is text with a `code block` word", TextType.PlainText)

        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.Code)

        expected_result = [
            TextNode("This is text with a ", TextType.PlainText),
            TextNode("code block", TextType.Code),
            TextNode(" word and another ", TextType.PlainText),
            TextNode("code block", TextType.Code),
            TextNode("This is text with a ", TextType.PlainText),
            TextNode("code block", TextType.Code),
            TextNode(" word", TextType.PlainText),
        ]

        self.assertEqual(new_nodes, expected_result)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )

        self.assertListEqual(
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")],
            matches
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )

        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],
            matches
        )


if __name__ == "__main__":
    unittest.main()