import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_node_split_delimiter(self):
        text_type_text = "text"
        text_type_code = "code"
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        correct_value = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, correct_value)

    def test_extract_markdown_image(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        response = extract_markdown_images(text)
        self.assertEqual(response, [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])
    
    def test_extract_markdown_link(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        extract = extract_markdown_links(text)
        self.assertEqual(extract, [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])
