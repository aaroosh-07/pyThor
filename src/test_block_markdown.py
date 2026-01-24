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
        # only basic funtionality has been tested in these tests
        # need to add more test for edge cases

        self.assertEqual(block_to_block_type("# this is a heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## this is a heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### this is a heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("####### this is a heading"), BlockType.PARAGRAPH)

        unorderedListMd = """
- This is first list item.
- This is second list item.
- this is third list item.
"""
        self.assertEqual(block_to_block_type(unorderedListMd), BlockType.UNORDERED_LIST)

        orderedListMd = """
1. This is first item.
2. this is second item.
3. this is third item.
"""
        self.assertEqual(block_to_block_type(orderedListMd), BlockType.ORDERED_LIST)

        codeMd = """
```
#include<iostream.h>
```
"""
        self.assertEqual(block_to_block_type(codeMd), BlockType.CODE)

        qouteMd = """
> This should be displayed in quotes
> this next line also.
"""
        self.assertEqual(block_to_block_type(qouteMd), BlockType.QUOTE)

if __name__ == "__main__":
    unittest.main()