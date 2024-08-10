import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.").to_html()
        html = "<p>This is a paragraph of text.</p>"

        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        html2 = '<a href="https://www.google.com">Click me!</a>'

        node3 = LeafNode(value="This is a paragraph of text.").to_html()
        html3 = "This is a paragraph of text."

        self.assertEqual(node, html)
        self.assertEqual(node2, html2)
        self.assertEqual(node3, html3)

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
            tag="p",
            children = [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        ).to_html()
        html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node, html)

if __name__ == "__main__":
    unittest.main()
