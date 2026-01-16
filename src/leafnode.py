from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        # Does not allow children Html nodes
        super().__init__(tag = tag, value = value, props = props)

        if value is None or len(value) == 0:
            raise ValueError

    def to_html(self) -> str:
        if len(self.value) == 0:
            raise ValueError

        if self.tag is None or len(self.tag) == 0:
            # return raw string
            return value
        
        #enclose value in opening the closing tags
        propsStr = self.props_to_html()
        htmlString = f"<{self.tag}{propsStr}>{self.value}</{self.tag}>"
        return htmlString

    def __repr__(self):
        propsStr = str("< ")
        for key, value in self.props.items():
            propsStr += f"{key}: {value} "
        propsStr += ">"

        tagStr = self.tag if self.tag is not None else str("")
        return f"HTMLNode(tag:{tagStr} value:{self.value} props:{propsStr})"

