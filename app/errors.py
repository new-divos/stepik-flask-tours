from flask import render_template

from . import app
from .data import (
    title,
    departures,
)


# noinspection PyUnusedLocal
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html',
                           title=title,
                           departures=departures,
                           mt=5,
                           message="404. Страница не найдена"), 404


# noinspection PyUnusedLocal
@app.errorhandler(500)
def iternal_server_error(e):
    return render_template('error.html',
                           title=title,
                           departures=departures,
                           mt=5,
                           message="500. Внутренняя ошибка сервера"), 500
