from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag = tag, children = children, props = props)

    def to_html(self):
        if self.tag is None or len(self.tag) == 0:
            raise ValueError

        # Can Children List length be 0 ?
        if self.children is None:
            raise ValueError
        
        # should I build up children Html with recursion or iteration
        # going ahead with safe route, iteration
        # each child element handles generating its own child elements Html

        childrenHtmlStr = str("")

        for child in self.children:
            childrenHtmlStr += child.to_html()
        
        propsStr = self.props_to_html()
        return f"<{self.tag}{propsStr}>{childrenHtmlStr}</{self.tag}>"
        
