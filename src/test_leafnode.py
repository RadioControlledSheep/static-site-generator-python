import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_a_tag(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = LeafNode("a", "Google it!", props)
        result = node.to_html()
        expected = '<a href="https://www.google.com" target="_blank">Google it!</a>'
        self.assertEqual(result, expected)

    def test_none_value(self):
        LeafNode("p", None)
        self.assertRaises(ValueError)

    def test_no_tag(self):
        node = LeafNode(None, "hello, world")
        self.assertEqual(node.to_html(), "hello, world")

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Hello, world!")
        self.assertEqual(node.to_html(), "<i>Hello, world!</i>")

    def test_leaf_to_html_code(self):
        node = LeafNode("code", "print('Hello, world!')")
        self.assertEqual(node.to_html(), "<code>print('Hello, world!')</code>")

    def test_repr(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual('LeafNode("p", "Hello, world!", None)', repr(node))
