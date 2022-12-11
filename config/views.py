"""
To render html web pages
"""
# import random

from django.http import HttpResponse
from django.template.loader import render_to_string

from articles.models import Article


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    # name = "Justin"
    # number = random.randint(10, 1233123)
    article_obj = Article.objects.get(id=1)

    # article_title = article_obj.title
    # article_content = article_obj.content

    # Django Templates
    # H1_STRING_OLD = f"""
    # <h1>Hello {name} - {number}!</h1>
    # """
    # P_STRING_OLD = f"""
    # <p>Hi {name} - {number}!</p>

    # """
    # H1_STRING = f"""
    # <h1>Hello {article_obj.title}! ({article_obj.id})</h1>
    # """
    # P_STRING = f"""
    # <p>Hi {article_obj.content}!</p>
    # """

    article_queryset = Article.objects.all()
    context = {
        "title": article_obj.title,
        "content": article_obj.content,
        "id": article_obj.id,
        "object_list": article_queryset,
    }
    # HTML_STRING = H1_STRING + P_STRING
    # HTML_STRING = """
    # <h1>Hello {title}! ({id})</h1>
    # <p>Hi {content}!</p>
    # """.format(**context)

    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)
