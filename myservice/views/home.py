from flakon import JsonBlueprint


home = JsonBlueprint('home', __name__)


@home.route('/')
def index():
    """Home view.

    This view will return an empty JSON mapping.
    """
    return {}
