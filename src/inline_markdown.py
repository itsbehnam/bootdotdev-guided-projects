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

def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)
        if len(images) == 0 or old_node.text_type != "text":
            result.append(old_node)
            continue
        original_text = old_node.text
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown: image section not closed")
            if len(sections[0]) != 0:
                result.append(TextNode(sections[0], "text"))
            result.append(TextNode(image[0], "image", image[1]))
            original_text = sections[1]
        if original_text != "":
            result.append(TextNode(original_text, 'text'))
    return result

def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        if len(links) == 0 or old_node.text_type != "text":
            result.append(old_node)
            continue
        original_text = old_node.text
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown: link section not closed")
            if len(sections[0]) != 0:
                result.append(TextNode(sections[0], "text"))
            result.append(TextNode(link[0], "link", link[1]))
            original_text = sections[1]
        if original_text != "":
            result.append(TextNode(original_text, 'text'))
    return result
