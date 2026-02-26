import unittest

from block_markdown import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        markdown = """
###### Heading our way
Coming soon
"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_two(self):
        markdown = """
# Heading our way
Coming soon
"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_failed_heading(self):
        markdown = """
####### Heading our way
Coming soon
"""
        block_type = block_to_block_type(markdown)
        self.assertNotEqual(block_type, BlockType.HEADING)

    def test_failed_heading_two(self):
        markdown = """
        #Heading our way
Coming soon
"""
        block_type = block_to_block_type(markdown)
        self.assertNotEqual(block_type, BlockType.HEADING)

    def test_unordered_list(self):
        markdown = """
- Lions
- Tigers
- Bears
- Oh My!
"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.ULIST)

    def test_faulty_unordered_list(self):
        markdown = """
- Tables
- Ladders
- Chairs
Its a slobberknocker
"""
        block_type = block_to_block_type(markdown)
        self.assertNotEqual(block_type, BlockType.ULIST)

    def test_faulty_ordered_list(self):
        markdown = """
1. Nothing wrong with me
2. Nothing wrong with me
3. Nothing wrong with me
Oops yes there is
"""
        block_type = block_to_block_type(markdown)
        self.assertNotEqual(block_type, BlockType.OLIST)

    def test_ordered_list(self):
        markdown = """
1. Something's got to give
2. Something's got to give
3. Something's got to give, noooow
"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.OLIST)

    def test_quote(self):
        markdown = """
>Once more unto the breach, dear friends, once more;
>Or close the wall up with our English dead.
>In peace there's nothing so becomes a man
>As modest stillness and humility:
>But when the blast of war blows in our ears,
>Then imitate the action of the tiger;
"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_rimmers_quote(self):
        markdown = """
>Now...
something something, something, great speech
"""
        block_type = block_to_block_type(markdown)
        self.assertNotEqual(block_type, BlockType.QUOTE)

    def test_code(self):
        markdown = """
```
print("Hello Muddah")
print("Hello Faddah")
print("Here I am at, Camp Granada")
print("And they say we'll have some fun if it stops raining")
```
"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.CODE)

    def test_not_code(self):
        markdown = """
```
print("I went hiking, with Joe Spivy")
print("He developed, poison Ivy")
print("You remember Leonard Skinner")
print("He got ptomaine poisoning last night after dinner")
"""
        block_type = block_to_block_type(markdown)
        self.assertNotEqual(block_type, BlockType.CODE)

    def test_paragraph(self):
        markdown = """
            This one is actually meant to just be a paragraph believe it or not!
            """
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
