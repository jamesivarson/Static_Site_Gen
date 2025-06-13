import unittest

from textnode import TextNode
from delimiter import split_nodes_delimiter


class TestDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [
            "This is a text node",
            TextNode("This is a text node", "BOLD"),
            "Another text node",
        ]
        delimiter = ","
        text_type = "TEXT"

        expected_nodes = [
            TextNode("This is a text node", text_type),
            TextNode("This is a text node", "BOLD"),
            TextNode("Another text node", text_type),
        ]

        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(new_nodes, expected_nodes)
    




if __name__ == "__main__":
    unittest.main()