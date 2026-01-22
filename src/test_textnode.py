import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is Plain Text", TextType.TEXT)
        node2 = TextNode("This is Plain Text", TextType.TEXT)
        self.assertEqual(node1, node2)

    def test_ineq(self):
        node1 = TextNode("This is Plain text", TextType.TEXT)
        node2 = TextNode("This is Link", TextType.LINK)
        self.assertNotEqual(node1, node2)

    def test_inEqEdgeCase(self):
        node1 = TextNode("This is plain text", TextType.TEXT, "Dummy Link")
        node2 = TextNode("This is plain text", TextType.TEXT)
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()