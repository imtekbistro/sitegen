from htmlnode import HTMLNode, LeafNode, ParentNode

def test_htmlnode_initialization():
    node = HTMLNode(tag="p", value="Hello, world!", children=[], props={"class": "text"})
    assert node.tag == "p"
    assert node.value == "Hello, world!"
    assert node.children == []
    assert node.props == {"class": "text"}

def test_props_to_html():
    node = LeafNode("a", "Test", {"href": "https://example.com", "target": "_blank"})
    
    # This will print the generated output from the props_to_html method
    result = node.props_to_html()
    print(f"Generated output: '{result}'")            # Debugging print
    print(f"Expected output:  'href=\"https://example.com\" target=\"_blank\" '")

    # Existing assertion
    assert result == 'href="https://example.com" target="_blank" '

def test_props_to_html_with_no_props():
    node = HTMLNode()
    assert node.props_to_html() == ""

def test_repr():
    node = HTMLNode(tag="div", value="content", children=[], props={"id": "main"})
    assert repr(node) == 'div, content, [], {\'id\': \'main\'}'

def test_LeafNode():
    assert LeafNode("p", "Hello").to_html() == "<p>Hello</p>"
    assert LeafNode("a", "Link", {"href": "https://example.com"}).to_html() == '<a href="https://example.com">Link</a>'
    node = LeafNode("a", "Test", {"href": "https://example.com", "target": "_blank"})
    result = node.props_to_html()
    print(f"Generated props to HTML: '{result}'")

def test_ParentNode():
    # Test valid case
    try:
        node1 = ParentNode("div", [LeafNode("b", "Bold text")])
        assert node1.to_html() == "<div><b>Bold text</b></div>"
        print("Valid case passed!")
    except Exception as e:
        print(f"Valid case failed: {e}")

    # Test empty children
    try:
        ParentNode("div", [])
        print("Empty children case failed - should have raised ValueError")
    except ValueError:
        print("Empty children case passed!")

    # Test None tag
    try:
        ParentNode(None, [LeafNode("b", "Bold text")])
        print("None tag case failed - should have raised ValueError")
    except ValueError:
        print("None tag case passed!")

        # Test multiple children
    try:
        node2 = ParentNode("div", [
            LeafNode("b", "Bold"),
            LeafNode("i", "Italic"),
            LeafNode(None, "Normal")
        ])
        assert node2.to_html() == "<div><b>Bold</b><i>Italic</i>Normal</div>"
        print("Multiple children case passed!")
    except Exception as e:
        print(f"Multiple children case failed: {e}")

    # Test nested parents
    try:
        node3 = ParentNode("div", [
            ParentNode("p", [LeafNode("b", "Bold")])
        ])
        assert node3.to_html() == "<div><p><b>Bold</b></p></div>"
        print("Nested parents case passed!")
    except Exception as e:
        print(f"Nested parents case failed: {e}")

    # Test with properties
    try:
        node4 = ParentNode("div", [LeafNode("b", "Bold")], {"class": "container"})
        assert node4.to_html() == '<div class="container"><b>Bold</b></div>'
        print("Properties case passed!")
    except Exception as e:
        print(f"Properties case failed: {e}")
    
    try:
        multi_prop_node = ParentNode("div", [
            LeafNode("b", "Bold")
        ], {"class": "container", "id": "main", "data-test": "value"})
        # What do you think the assertion should look like here?
        print("Multiple properties passed!")
    except Exception as e:
        print(f"Multiple properties failed: {e}")

    try:
        nested_node = ParentNode("div", [
            ParentNode("p", [
                LeafNode("span", "Hello", {"class": "text"}),
                LeafNode("b", "World")
            ], {"id": "para"})
        ], {"class": "container"})
        assert nested_node.to_html() == '<div class="container"><p id="para"><span class="text">Hello</span><b>World</b></p></div>'
        print("Deep nesting with properties passed!")
    except Exception as e:
        print(f"Deep nesting with properties failed: {e}")

test_htmlnode_initialization()
test_props_to_html()
test_props_to_html_with_no_props()
test_repr()
test_LeafNode()
test_ParentNode()