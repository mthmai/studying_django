from my_app.abstract_classes import ViewsABC


class GenericViews(ViewsABC):
    def __init__(self, request: str = None) -> None:
        self.request = request
