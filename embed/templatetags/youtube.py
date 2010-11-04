from django import template
from django.template import Context, loader, Node


register = template.Library()

def do_youtube(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, id_ = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires 1 argument" % token.contents.split()[0]
    return YoutubeNode(id_)


class YoutubeNode(Node):
    def __init__(self, id_):
        self.id = id_

    def render(self, context):
        t = loader.get_template('embed/youtube.html')
        c = Context({'id': self.id}, autoescape=context.autoescape)
        return t.render(c)


register.tag('youtube', do_youtube)
