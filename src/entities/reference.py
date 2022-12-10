class Reference:
    def __init__(self):
        self._fields = {
            "citekey": None,
            "author": None,
            "title": None,
            "journal": None,
            "year": None,
            "volume": None,
            "pages": None,
            "publisher": None,
            "volume_or_number": None,
            "number": None,
            "series": None,
            "edition": None,
            "address": None,
            "month": None,
            "note": None
        }
        self._required_fields = ["citekey",
                                 "author", "title", "journal", "year"]

    def get_required_fields(self) -> list:
        return self._required_fields

    def get_fields(self) -> dict:
        return self._fields

    def set_field(self, key: str, value: str):
        if key in self._fields:
            self._fields[key] = value

    def __str__(self):
        return self._fields
