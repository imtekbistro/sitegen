from enum import Enum
from htmlnode import *

class TextType(Enum):
    TEXT = "normal text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    LINK = "hyperlink"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None, alt_text=None):
        self.text =  text
        self.text_type = text_type
        self.url = url
        self.alt_text = alt_text

    def __eq__(self, other):
        return (self.text == other. text and 
                self.text_type == other.text_type and
                self.url == other.url)
    
    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type}, {self.url})")
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        new_node = LeafNode(None, text_node.text, None)
        
    elif text_node.text_type == TextType.BOLD:
        new_node = LeafNode("b", text_node.text, None)
        
    elif text_node.text_type == TextType.ITALIC:
        new_node = LeafNode("i", text_node.text, None)
        
    elif text_node.text_type == TextType.CODE:
        new_node = LeafNode("code", text_node.text, None)
        
    elif text_node.text_type == TextType.LINK:
        new_node = LeafNode("a", text_node.text, {"href": text_node.url})
        
    elif text_node.text_type == TextType.IMAGE:
        new_node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.alt_text})

    else:
        raise Exception("Invalid Text Enum")
        
    return new_node
    


