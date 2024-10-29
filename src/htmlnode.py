class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
        # Ensure the string starts directly without a space
            return ' '.join(f'{k}="{v}"' for k, v in self.props.items()) + ' '
        return ''
        
    def __repr__(self):
        return(f"{self.tag}, {self.value}, {self.children}, {self.props}")
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("A value is required for a LeafNode")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value.")
        if self.tag:
            props_html = self.props_to_html().strip()
            # Check for unnecessary spaces
            if props_html:
                return f'<{self.tag} {props_html}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return self.value

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not children:
            raise ValueError("ParentNode must have children")
        if not tag:
            raise ValueError("ParentNode needs a tag")
        super().__init__(tag, None, children, props)

    def to_html(self):
        full_string = []
        for child in self.children:
            full_string.append(child.to_html())
        result = f'<{self.tag} {self.props_to_html().strip()}>{"".join(full_string)}</{self.tag}>' if self.props else f'<{self.tag}>{"".join(full_string)}</{self.tag}>'
        #print(f"Generated HTML: {result}")  # Debug print
        return result
            
    

            
