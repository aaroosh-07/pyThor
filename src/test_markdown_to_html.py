import unittest
from block_markdown import markdown_to_html

class TestMarkdownToHtml(unittest.TestCase):
    def test_heading_to_html(self):
        headingStr = """
# this is a heading
"""
        htmlNode = markdown_to_html(headingStr)
        rawHtml = htmlNode.to_html()

        self.assertEqual(rawHtml, "<div><h1>this is a heading</h1></div>")

if __name__ == "__main__":
    unittest.main()