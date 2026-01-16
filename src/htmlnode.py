class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        if tag == None and value == None:
            raise Exception("Both tag and value cannot be none")
        
        if value is None and (children is None or len(children) == 0):
            raise Exception("Both value and children cannot be null")

        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if len(self.props) == 0:
            return str("")

        formatedStr = str()
        for key, value in self.props.items():
            formatedStr += f" {key}=\"{value}\""
        
        return formatedStr

    def __repr__(self):
        propsStr = str("< ")
        for key, value in self.props.items():
            propsStr += f"{key}: {value} "
        propsStr += ">"
        return f"HTMLNode(tag:{self.tag} value:{self.value} props:{propsStr})"
    
