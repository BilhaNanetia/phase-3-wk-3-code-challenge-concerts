class Band:
    all = []
    def __init__(self, name, hometown):
        if isinstance(hometown, str) and len(hometown):
            self._hometown = hometown
        else:
            raise ValueError("hometown must be a non-empty string")
        self.name = name
        Band.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("name must be a non-empty string")
        
    @property
    def hometown(self):
        return self._hometown

    def concerts(self):
        return [concert for concert in Concert.all_concerts if concert.band == self]

    def venues(self):
        venues = list (set(concert.venue for concert in self.concerts()))
        return venues if venues else None

    def play_in_venue(self, venue, date):
        if not isinstance(venue, Venue):
            raise ValueError("venue must be of type Venue")
        return Concert (self, venue, date)

    def all_introductions(self):
        return [
            concert.introduction() for concert in self.concerts() if concert.introduction()
        ]


class Concert:
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue

    def hometown_show(self):
        pass

    def introduction(self):
        pass


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def concerts(self):
        pass

    def bands(self):
        pass
