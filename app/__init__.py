from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


# Импорт компонентов приложения должен быть после
# инициализации app для предотвращения зацикливания

from .filters import (
    stars,
    withunit,
    price,
)  # noqa

from .views import (
    index,
    get_departure,
    get_tour,
)  # noqa

from .errors import (
    page_not_found,
    iternal_server_error,
)  # noqa