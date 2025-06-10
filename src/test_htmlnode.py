import unittest
from htmlnode import HTMLNode, LeafNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_begins_with_space(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("a", None, None, props=props)
        self.assertTrue(str(node.props_to_html()).startswith(" "))

    def test_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("a", None, None, props=props)
        self.assertRaises(NotImplementedError, node.to_html)

    def test_child_node_is_a_list(self):
        child_node = HTMLNode("p", "this is a paragraph", None, None)
        node = HTMLNode("h1", "hello", [child_node], None)
        self.assertTrue(isinstance(node.children, list))

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com"</a>')
