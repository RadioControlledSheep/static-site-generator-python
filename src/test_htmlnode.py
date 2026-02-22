import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_1(self):
        props1 = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(None, None, None, props1)
        result = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(expected, result)

    def test_default_tag(self):
        node = HTMLNode()
        result = node.tag
        expected = None

        self.assertEqual(expected, result)

    def test_default_value(self):
        node = HTMLNode()
        result = node.value
        expected = None

        self.assertEqual(expected, result)

    def test_default_children(self):
        node = HTMLNode()
        result = node.children
        expected = None
        self.assertEqual(result, expected)
