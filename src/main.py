from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    print(TextNode("this is a test", TextType.LINK, "https://boot.dev"))
    node = HTMLNode("a", None, None, props=props)
    print(node.props_to_html())
    child_node = HTMLNode("p", "this is a paragraph", None, None)
    node = HTMLNode("h1", "hello", [child_node], None)
    print(node)
    leafnode = LeafNode("p", "This is a paragraph of text.").to_html()
    print(leafnode)
    lf = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
    print(lf)
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print("parentnondehtml", node.to_html())


if __name__ == "__main__":
    main()
