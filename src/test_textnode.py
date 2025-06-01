import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        self.assertIsNone(node.url)

    def test_url_is_not_none(self):
        node = TextNode("This is a text node", TextType.NORMAL, "https://boot.dev")
        self.assertIsNotNone(node.url)

    def test_url_begins_with_http(self):
        node = TextNode("This is a text node", TextType.NORMAL, "https://boot.dev")
        self.assertTrue(str(node.url).startswith("http"))


if __name__ == "__main__":
    unittest.main()
