import re
from textnode import TextNode
from htmlnode import LeafNode

# TODO: Using Enum for types
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(value=text_node.text)
        case "bold":
            return LeafNode(tag="b", value=text_node.text)
        case "italic":
            return LeafNode(tag="i", value=text_node.text) 
        case "code":
            return LeafNode(tag="code", value=text_node.text)
        case "link":
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case "image":
            return LeafNode(tag="img", props={"src": text_node.url})
        case _:
            raise Exception('wrong type')
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            result.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise Exception('Markdown: unmatched delimiter')
        parts = node.text.split(delimiter)
        for index, value in enumerate(parts):
            if index % 2 == 0:
                result.append(TextNode(value, node.text_type))
            else:
                result.append(TextNode(value, text_type))

    return result

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
