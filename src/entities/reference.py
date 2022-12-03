

class Reference:
    
    def __init__(self):
        self.fields = {
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
        self._required_fields = []

    def get_required_fields (self):
        return self._required_fields

    def get_fields(self):
        return self.fields