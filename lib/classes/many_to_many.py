class Band:
    all = []  # list to hold all band instances
    def __init__(self, name, hometown):
        # validate and set the hometown attribute
        if isinstance(hometown, str) and len(hometown):
            self._hometown = hometown
        else:
            raise ValueError("hometown must be a non-empty string")
        self.name = name    # set the name using the property setter
        Band.all.append(self) # add the band instance to the list of all bands   

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # validate and set the name attribute
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("name must be a non-empty string")
        
    @property
    def hometown(self):
        return self._hometown

    def concerts(self):
        # return a list of all concerts where this band performed
        return [concert for concert in Concert.all if concert.band == self]

    def venues(self):
        # return a list of unique venues where this band performed
        venues = list (set(concert.venue for concert in self.concerts()))
        return venues if venues else None

    def play_in_venue(self, venue, date):
        # create a new concert for this band in the specified venue and date
        if not isinstance(venue, Venue):
            raise ValueError("venue must be of type Venue")
        return Concert (date, self, venue)

    def all_introductions(self):
        # return a list of all concert introductions for this band
        return [
            concert.introduction() for concert in self.concerts() 
        ]


class Concert:
    all = []    # list to hold all concert instances
    def __init__(self, date, band, venue):
        # initialize a Concert instance with date,band and venue
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)  # add this instance to the list of all concerts

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        # validate and set the date attribute
        if isinstance(date, str) and len(date) > 0:
            self._date = date
        else:
            raise ValueError("date must be a non-empty string")
        
    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self, band):
        # validate and set the band attribute
        if isinstance(band, Band):
            self._band = band
        else:
            raise ValueError("band must be of type Band")
        
    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, venue):
        # validate and set the venue attribute
        if isinstance(venue, Venue):
            self._venue = venue
        else:
            raise ValueError("venue must be of type Venue")

    def hometown_show(self):
        # return True if the concert is in the band's hometown
        return self.venue.city == self.band.hometown

    def introduction(self):
        # return a string introducing the band at the concert
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    all = []   # list to hold all Venue instances
    def __init__(self, name, city):
        # initialize a Venue instance with a name and a city
        self.name = name
        self.city = city
        Venue.all.append(self)   # add this instance to the list of all Venue instances

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("name must be a non-empty string")
        
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        # validate and set the city attribute
        if isinstance(city, str) and len(city) > 0:
            self._city = city
        else:
            raise ValueError("city must be a non-empty string")

    def concerts(self):
        # return a list of all concerts held at this venue
        return [concert for concert in Concert.all if concert.venue == self]

    def bands(self):
        # return a list of unique bands who have performed at this venue
        return list({concert.band for concert in self.concerts()})
    
    def concert_on(self, date):
        # return the first concert on the specified date, or None if no concerts are found
        for concert in self.concerts():
            if concert.date == date:
                return concert
            return None
