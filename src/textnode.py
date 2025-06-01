from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type: Enum, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            return False
        if (self.text, self.text_type, self.url) == (
            other.text,
            other.text_type,
            other.url,
        ):
            return True
        return False

    def __repr__(self) -> str:
        return f"TextNode({str(self.text)}, {self.text_type.value}, {str(self.url)})"
