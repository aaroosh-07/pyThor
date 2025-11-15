from enum import Enum, auto

class TextType(Enum):
    PlainText: str = "Plain Text"
    BoldText: str = "Bold Text"
    ItalicText: str = "Italic Text"
    Code: str = "Code"
    Link: str = "Link"
    Images: str = "Images"

class TextNode():
    def __init__(self, text: str, textType: TextType, link: str = none):
        self.text = text
        self.text_type = textType
        self.link = link
    
    def __eq__(self, other):
        if self.text != other.text:
            return False
        
        if self.text_type != other.text_type:
            return False
        
        if self.link != other.link:
            return False

        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.link})"

