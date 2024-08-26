class TextNode:
    def __init__(self, text,text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        #das url ist noch nicht richtig

    def __eq__(self, other):
        if not isinstance(other, TextNode):  # Ensure the other object is also a TextNode
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url== other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    



