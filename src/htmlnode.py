class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if self.props:
            for key in self.props:
                result += f' {key}="{self.props[key]}"'
        
        return result
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        
        if not self.tag:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag,None, children, props)
    
    def to_html(self):
        html = ""
        if not self.tag:
            raise ValueError("Must have a tag")
        if not self.children:
            raise ValueError("Must have children")
        
        for child in self.children:
            if isinstance (child, ParentNode):
                parentnode = child.to_html()
                html += parentnode
            
            if isinstance (child, LeafNode):
                leafnode = child.to_html()
                html += leafnode

        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"
