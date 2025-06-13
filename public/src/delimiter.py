from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Splits a list of nodes into a list of multiple text types based on a delimiter.
    Args:
        old_nodes (list): List of nodes to be split.
        delimiter (str): The delimiter to split the nodes by.
        text_type (TextType): The type of text for the new nodes.
        Returns a list of new nodes with the specified text type.
        """
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, str):
            parts = node.split(delimiter)
            for part in parts:
                if part.strip():  # Avoid adding empty strings
                    new_nodes.append(TextNode(part.strip(), text_type))
        else:
            new_nodes.append(node)  # Keep the original node if it's not a string
    return new_nodes