from textnode import TextNode, TextType

def main():
    node = TextNode("garbage", TextType.BOLD, "bullshit.com")
    print(node)

if __name__ == "__main__":
    main()