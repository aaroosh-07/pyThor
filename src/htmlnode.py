class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list() = None, props: dict() = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self): str
        if self.props == None:
            return str("")

        formatedStr = str()
        for key, value in self.props:
            formatedStr += f" {key}=\"{value}\""
        
        return formatedStr
    
