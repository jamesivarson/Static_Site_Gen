from textnode import TextNode # type: ignore

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, str):
            parts = node.split(delimiter)
            for part in parts:
                if part.strip():
                    new_nodes.append(TextNode(part.strip(), text_type))
        else:
            new_nodes.append(node) 
    return new_nodes