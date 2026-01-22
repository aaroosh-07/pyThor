from textnode import TextNode, TextType

def main():
    obj = TextNode("this is a image link", TextType.IMAGE, "./img.jpeg")
    print(obj)

main()