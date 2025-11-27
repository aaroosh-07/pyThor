import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is Plain Text", TextType.PlainText)
        node2 = TextNode("This is Plain Text", TextType.PlainText)
        self.assertEqual(node1, node2)

    def test_ineq(self):
        node1 = TextNode("This is Plain text", TextType.PlainText)
        node2 = TextNode("This is Link", TextType.Link)
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()