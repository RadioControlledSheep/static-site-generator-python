import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered-list"
    OLIST = "ordered-list"


def block_to_block_type(markdown):
    markdown_lines = markdown.split("\n")
    if re.findall(r"^#{1,6} ", markdown):
        return BlockType.HEADING
    if markdown.startswith(">"):
        for line in markdown_lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if markdown.startswith("- "):
        for line in markdown_lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if re.findall(r"^\d+\.", markdown):
        for line in markdown_lines:
            if not re.findall(r"^\d+\.", line):
                return BlockType.PARAGRAPH
        return BlockType.OLIST
    if re.findall(r"^```\n", markdown) and re.findall(r"\n```$", markdown):
        return BlockType.CODE
    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
    blocks = [block for block in blocks if block != ""]
    return blocks
