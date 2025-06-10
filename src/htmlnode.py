class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict | None = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        new_props = []
        if self.props and isinstance(self.props, dict):
            for k, v in self.props.items():
                new_props.append(f' {k}="{v}"')
        return "".join(n for n in new_props)

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {str(self.children)}, {str(self.props)}"


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict | None = None) -> None:
        super().__init__()
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError()
        if self.tag is None:
            return self.value
        elif self.props:
            return f"<{self.tag}{self.props_to_html()}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
