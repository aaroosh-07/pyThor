import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leafNode_to_html(self):
        generatedHtmlStr = LeafNode("p", "This is a paragraph of text.").to_html()
        resultStr = "<p>This is a paragraph of text.</p>"

        self.assertEqual(generatedHtmlStr, resultStr)

        generatedHtmlStr = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        resultStr = '<a href="https://www.google.com">Click me!</a>'

        self.assertEqual(generatedHtmlStr, resultStr)

if __name__ == "__main__":
    unittest.main()
