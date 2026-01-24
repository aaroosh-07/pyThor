from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
import unittest

class Test_block_markdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# this is a heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## this is a heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### this is a heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("####### this is a heading"), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()