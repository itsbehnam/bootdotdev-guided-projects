class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("method no implemented")

    def props_to_html(self):
         return " " + " ".join([f"{key}=\"{value}\"" for key, value in self.props.items()]) if self.props != None else ""
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None) -> None:
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError('Missing Value')
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        # if children == None:
        #     raise ValueError("Children property is required")
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag is missing")
        if self.children == None:
            raise ValueError("Children propery is missing")
        html = f"<{self.tag}{self.props_to_html()}>"
        html += "".join([child.to_html() for child in self.children])
        html += f"</{self.tag}>"
        return html
