import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("this is a text node", TextType.BOLD, url= "www.wf.com")
        node2 = TextNode("this is a text node", TextType.BOLD, url= "www.wf.com")
        self.assertEqual(node, node2)
        #nodes have url

    def test_eq_url_none(self):
        node = TextNode("this is a text node", TextType.BOLD, url= None)
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        #1 url missing, one "none"

    def test_noteq(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("this is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        #1 url missing, one "none"






if __name__ == "__main__":
    unittest.main()