class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None or not isinstance(self.props, dict):
            return ""
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if (value is None or value.isspace()):
            raise ValueError("LeafNode requires a value")
        super().__init__(tag=tag, value=value, props=props)
    def to_html(self):
        if self.tag is None:
            return self.value
        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode requires a tag")
        if self.children is None:
            raise ValueError("ParentNode requires children")
        children_html = "".join(child.to_html() for child in self.children)
        props_html = self.props_to_html()
        space_before_props = " " if props_html else ""
        return f"<{self.tag}{space_before_props}{props_html}>{children_html}</{self.tag}>"