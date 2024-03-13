class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if self.props is {"href": "https://www.google.com", "target": "_blank"}:
            return self.props_to_html( href="https://www.google.com" target="_blank"
)
    def __repr__(self):
        return HTMLNode(tag, value, children, props)