#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template

from data import departures, tours


app = Flask(__name__)


@app.route('/')
def index():
    print("Здесь будет главная")
    return render_template('index.html', departures=departures, tours=tours)


@app.route('/departures/<departure>/')
def get_tours_for_departure(departure):
    print(f"Здесь будет направление '{departure}'")

    name = departures.get(departure)
    if name is not None:
        name = name.split(' ')[1]

    tours_for_departure = {id: tour for id, tour in tours.items()
                           if tour['departure'] == departure}

    return render_template('departure.html',
                           name=name,
                           tours=tours_for_departure)


@app.route('/tours/<id>/')
def get_tour(id):
    print(f"Здесь будет тур {id}")
    tour = tours.get(int(id))

    return render_template('tour.html', tour=tour)


if __name__ == '__main__':
    app.run(debug=True)
