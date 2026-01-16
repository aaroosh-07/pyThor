import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_propGen(self):
        props = { "href": "https://www.google.com", "target": "_blank", }
        htmlObj = HTMLNode("a", "link", None, props)

        propsToHtmlStr = htmlObj.props_to_html()

        correctStr = " href=\"https://www.google.com\" target=\"_blank\""

        self.assertEqual(propsToHtmlStr, correctStr)

if __name__ == "__main__":
    unittest.main()