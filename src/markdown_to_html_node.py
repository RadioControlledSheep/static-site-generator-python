from src.block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from src.htmlnode import HTMLNode
from src.text_to_children import text_to_children
from src.textnode import TextNode, TextType


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = HTMLNode(block_type, block)
        if block_type == BlockType.CODE:
            stripped_block = block.strip("\n` ")
            formatted_block = f"<div><pre><code>{stripped_block}\n</code></pre><div>"
            code_text_node = TextNode(formatted_block, TextType.CODE)

        else:
            child_text = text_to_children(html_node.value)
