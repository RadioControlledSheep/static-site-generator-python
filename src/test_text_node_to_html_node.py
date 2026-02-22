import unittest

from htmlnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.TEXT_BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_italic(self):
        node = TextNode("This is italic", TextType.TEXT_ITALIC)
        html_node = text_node_to_html_node(node)
        expected = "<i>This is italic</i>"
        self.assertEqual(expected, html_node.to_html())

    def test_code(self):
        node = TextNode("This is code", TextType.TEXT_CODE)
        html_node = text_node_to_html_node(node)
        leaf_node = LeafNode("code", "This is code")
        self.assertEqual(html_node.to_html(), leaf_node.to_html())

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "http://www.google.com")
        html_node = text_node_to_html_node(node)
        leaf_node = LeafNode(
            "a",
            "This is a link",
            {
                "href": "http://www.google.com",
            },
        )
        self.assertEqual(html_node.to_html(), leaf_node.to_html())

    def test_invalid_type(self):
        TextNode("This is code", "BANANA")
        self.assertRaises(ValueError)

    def test_no_link_url(self):
        TextNode("This is a Link", TextType.LINK)
        self.assertRaises(ValueError)

    def test_no_image_url(self):
        TextNode("This is an image", TextType.IMAGE)
        self.assertRaises(ValueError)
