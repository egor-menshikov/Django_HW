from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

_INDEX = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Homepage</title>
</head>
<body>
<h1>Это домашняя страница студента GB</h1>
</body>
</html>
"""

_ABOUT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About me</title>
</head>
<body>
<p>Меня зовут Егор, я учусь на веб-разработчика.</p>
</body>
</html>
"""


# Create your views here.
def index(request):
    try:
        text = _INDEX
    except Exception as e:
        logger.exception(f'Error on "index" page: {e}')
        return HttpResponse('Something went wrong.')
    else:
        logger.debug('"Index" page accessed.')
        logger.info('Showing "index" page contents.')
        return HttpResponse(text)


def about(request):
    try:
        text = _ABOUT
    except Exception as e:
        logger.exception(f'Error on "about" page: {e}')
        return HttpResponse('Something went wrong.')
    else:
        logger.debug('"About" page accessed.')
        logger.info('Showing "About" page contents.')
        return HttpResponse(text)
