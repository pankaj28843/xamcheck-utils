# Standard Library
import re

# Third Party Stuff
from html2text import HTML2Text


def check_if_html_has_text(html):
    """ Checks if given html string has any text
    >>> check_if_html_has_text("<p>   &nbsp;</p>")
    False
    >>> check_if_html_has_text("<p>   &  \\n</p>")
    True
    """
    html = html.encode('ascii', 'xmlcharrefreplace')
    # html = html.decode('utf-8', 'ignore')
    h = HTML2Text()
    h.ul_item_mark = ''
    h.emphasis_mark = ''
    h.strong_mark = ''

    text = h.handle(html)

    text = re.sub(r"\s", "", text)

    if text == "":
        return False
    return True
