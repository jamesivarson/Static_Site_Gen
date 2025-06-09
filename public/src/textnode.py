from enum import Enum

class TextType(Enum):
    BOLD = 1 # **Bold text**
    ITALIC = 2 # __Italic text__
    CODE = 3 # `Code text`
    LINK = 4 # [anchor text] (url)
    IMAGE = 5 # ![alt text] (url)

class TextNode:
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text 
                and self.text_type == other.text_type
                and self.url == other.url)
    
    def __repr__(self):
        return str(f"TextNode({self.text}, {self.text_type}, {self.url})")