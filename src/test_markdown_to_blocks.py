import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
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

    def test_whitepace_removal(self):
        markdown = """   This paragraph has 3 spaces in front of it



        This paragraph had 4 carriage returns before it
        """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "This paragraph has 3 spaces in front of it",
                "This paragraph had 4 carriage returns before it",
            ],
        )
