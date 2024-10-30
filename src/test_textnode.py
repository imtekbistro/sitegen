import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text(self):
        # Test with TextType.TEXT
        text_node = TextNode("This is normal text.", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is normal text.")
        self.assertEqual(html_node.props, None)

    def test_bold_text(self):
        # Test with TextType.BOLD
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        self.assertEqual(html_node.props, None)

    def test_italic_text(self):
        # Test with TextType.ITALIC
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        self.assertEqual(html_node.props, None)

    def test_link(self):
        # Test with TextType.LINK
        text_node = TextNode("Link text", TextType.LINK, url="http://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link text")
        self.assertIsNotNone(html_node.props)
        self.assertEqual(html_node.props["href"], "http://example.com")

    def test_image(self):
        # Test with TextType.IMAGE
        text_node = TextNode("", TextType.IMAGE, url="http://example.com/image.jpg", alt_text="A sample image")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertIsNotNone(html_node.props)
        self.assertEqual(html_node.props["src"], "http://example.com/image.jpg")
        self.assertEqual(html_node.props["alt"], "A sample image")

if __name__ == "__main__":
    unittest.main()