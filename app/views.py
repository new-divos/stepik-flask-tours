from flask import render_template, abort

from . import app
from .data import (
    title,
    subtitle,
    description,
    departures,
    tours,
)


@app.route('/')
def index():
    tours_lst = [(idx, tour) for idx, tour in tours.items()]
    tours_lst.sort(key=lambda item: int(item[1]['stars']), reverse=True)
    selected_tours = {idx: tour for idx, tour in tours_lst[:6]}

    return render_template('index.html',
                           title=title,
                           departures=departures,
                           mt=3,
                           subtitle=subtitle,
                           description=description,
                           tours=selected_tours)


@app.route('/departures/<code>/')
def get_departure(code):
    name = departures.get(code)
    if name is not None:
        name = name.split(' ')[1]
    else:
        abort(404)

    selected_tours = {id: tour for id, tour in tours.items()
                      if tour['departure'] == code}

    prices = [tour['price'] for tour in tours.values()]
    nights = [tour['nights'] for tour in tours.values()]

    return render_template('departure.html',
                           title=title,
                           departures=departures,
                           active_code=code,
                           mt=3,
                           name=name,
                           min_price=min(prices),
                           max_price=max(prices),
                           min_nights=min(nights),
                           max_nights=max(nights),
                           tours=selected_tours)


@app.route('/tours/<idx>/')
def get_tour(idx):
    tour = tours.get(int(idx))
    if tour is None:
        abort(404)

    return render_template('tour.html',
                           title=title,
                           departures=departures,
                           active_code=tour['departure'],
                           mt=0,
                           tour=tour)
