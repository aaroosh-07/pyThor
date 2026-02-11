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

    def test_paragraph_to_html(self):
        paragraphMd = """
this is a simple text
"""
        htmlNode = markdown_to_html(paragraphMd)
        rawHtml = htmlNode.to_html()

        self.assertEqual(rawHtml, "<div><p>this is a simple text</p></div>")

        paragraphBoldItalicMd = """
this is a simple text with **Bold** and _italic_ text
"""
        htmlNode = markdown_to_html(paragraphBoldItalicMd)
        rawHtml = htmlNode.to_html()

        self.assertEqual(rawHtml, "<div><p>this is a simple text with <b>Bold</b> and <i>italic</i> text</p></div>")

    def test_unordered_list_to_html(self):
        unorderedListMd = """
- first item
- second item
- third item
"""
        htmlNode = markdown_to_html(unorderedListMd)
        rawHtml = htmlNode.to_html()

        self.assertEqual(rawHtml, "<div><ul><li>first item</li><li>second item</li><li>third item</li></ul></div>")

if __name__ == "__main__":
    unittest.main()