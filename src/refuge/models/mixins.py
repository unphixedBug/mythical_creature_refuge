class FlyingMixin():
    def __init__(self, *args, **kwargs):
        self.flight_log = []

        super().__init__(*args, *kwargs)

    def travel_mode(self):
        return f"by air"

    def fly(self, destination):
        log = f"{self.name} soars towards {destination}"
        self.flight_log.append(log)
        return log