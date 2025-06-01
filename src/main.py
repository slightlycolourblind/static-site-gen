from textnode import TextNode, TextType


def main():
    print(TextNode("this is a test", TextType.LINK, "https://boot.dev"))


if __name__ == "__main__":
    main()
