class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    


class LeafNode(HTMLNode):
    print("Inside LeafNode to_html!")
    def __init__(self, tag, value, props=False):
        if (value is None or value.isspace()):
            raise ValueError("LeafNode requires a value")
        super().__init__(tag=tag, value=value, props=props)
    def to_html(self):
        if self.tag is None:
            return self.value
        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"