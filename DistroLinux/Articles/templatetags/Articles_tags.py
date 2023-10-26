from django import template
from Articles.models import *
import math

register = template.Library()


@register.simple_tag(name="getThemeList")
def get_articles_themes():
    return {"Linux": ["Ubuntu", "Mint", "Debian", "Fedora", "Manjaro", "Other_Distro"],
            "Linux Gaming": ["Native_Gaming", "Proton", "Wine"]}


@register.simple_tag(name='replace_underlines')
def replace_underlines(filter="__Test__"):
    if "_" in filter:
        return filter.replace('_', ' ')
    else:
        return filter


@register.simple_tag(name="getThemeCountList")
def get_articles_count(theme="Ubuntu"):
    return Article.objects.filter(theme=theme).count()


@register.simple_tag(name="all_articles_count")
def get_all_articles_count(number_of_article_on_page=7, theme=None):
    if theme is None:
        print(math.ceil((Article.objects.all().count())/number_of_article_on_page))
        return math.ceil((Article.objects.all().count())/number_of_article_on_page)
    else:
        print("Hello World!", math.ceil(Article.objects.filter(theme=theme).count()/number_of_article_on_page))
        return math.ceil(Article.objects.filter(theme=theme).count()/number_of_article_on_page)


@register.simple_tag(name="getlist_from_integers")
def getlist_from_integers(top_value=7):
    return list(range(top_value))


@register.simple_tag(name="devide_numbers")
def devide_numbers(value=1, arg=1):
    try:
        return int(int(value)/int(arg))
    except (ValueError, ZeroDivisionError):
        return None


@register.simple_tag(name="multiply_numbers")
def multiply_numbers(value=1, arg=1):
    try:
        return int(int(value)*int(arg))
    except (ValueError):
        return None


@register.simple_tag(name="minus_numbers")
def minus_numbers(value=1, arg=1):
    try:
        return int(int(value)-int(arg))
    except ValueError:
        return None


@register.simple_tag(name="create_list")
def create_list(start=1, end=1):
    return list(range(start, end+1, 1))


@register.simple_tag(name="limited_query_data")
def limited_query_data(start=1, end=1, theme=None):
    if theme is None:
        return Article.objects.all().order_by('-creation_time')[start:end]
    else:
        return Article.objects.filter(theme=theme).order_by('-creation_time')[start:end]


@register.inclusion_tag("Articles/inclusion_tags/page_changer_sequence.html")
def page_changer_sequence(page_count=2, cur_page=1, theme=None):
    return {'page_numbers': list(range(1, page_count+1, 1)),
            'current_page_id': cur_page,
            'theme': theme,
            }


@register.inclusion_tag("Articles/inclusion_tags/page_changer_left.html")
def draw_page_changer_left(page_count=2, cur_page=1, theme=None):
    return {'page_numbers': list(range(1, 6, 1)),
            'current_page_id': cur_page,
            'last_page': page_count,
            'theme': theme,
            }


@register.inclusion_tag("Articles/inclusion_tags/page_changer_right.html")
def draw_page_changer_right(page_count=2, cur_page=1, theme=None):
    return {'page_numbers': list(range(page_count-4, page_count+1, 1)),
            'current_page_id': cur_page,
            'last_page': page_count,
            'theme': theme,
            }


@register.inclusion_tag("Articles/inclusion_tags/page_changer_center.html")
def draw_page_changer_center(page_count=2, cur_page=1, theme=None):
    return {'current_page_id': cur_page,
            'last_page': page_count,
            'theme': theme,
            }


@register.inclusion_tag("Articles/inclusion_tags/sidebar_creation.html")
def draw_nav_sidebar(mobile_sidebar=False, class_name='left-sidebar-sticky', page_theme=None):
    return {
        "sidebar_for_mobiles": mobile_sidebar,
        "class_name": class_name,
        "current_theme": page_theme,
    }


