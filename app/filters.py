from . import app


@app.template_filter()
def stars(rating: str):
    return '&#9733;' * int(rating)


@app.template_filter()
def withunit(value: int, unit: str):
    value = abs(value)
    r10, r100 = value % 10, value % 100

    name = None
    if unit == 'night':
        if r10 == 1 and not 10 < r100 < 20:
            name = "ночь"
        elif 1 < r10 < 5 and not 10 < r100 < 20:
            name = "ночи"
        else:
            name = "ночей"

    elif unit == 'tour':
        if r10 == 1 and not 10 < r100 < 20:
            name = "тур"
        elif 1 < r10 < 5 and not 10 < r100 < 20:
            name = "тура"
        else:
            name = "туров"

    return f"{value} {name}" if name is not None else str(value)


@app.template_filter()
def price(value: int):
    return "{:,}".format(value).replace(',', ' ') + ' &#8381;'
