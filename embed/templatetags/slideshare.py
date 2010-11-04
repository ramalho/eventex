from django import template
from django.template import Context, loader, Node


register = template.Library()

def do_slideshare(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, id_, doc = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires 2 arguments" % token.contents.split()[0]
    return SlideShareNode(id_, doc)


class SlideShareNode(Node):
    def __init__(self, id_, doc):
        self.id = id_
        self.doc = doc

    def render(self, context):
        t = loader.get_template('embed/slideshare.html')
        c = Context({'id': self.id, 'doc': self.doc}, autoescape=context.autoescape)
        return t.render(c)


register.tag('slideshare', do_slideshare)
