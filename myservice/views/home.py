from flask import Blueprint


home = Blueprint('home', __name__)


@home.route('/')
def index():
    """Home view.

    This view will return an empty JSON mapping.
    """
    return {}
