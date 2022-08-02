class Developer:
    def __init__(self):
        self.fields = []

    def __contains__(self, item):
        for field in self.fields:   
            if item in field:
                return True
        return False