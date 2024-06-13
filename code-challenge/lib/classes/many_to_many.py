class Band:
    all_bands = []

    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        Band.all_bands.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise TypeError("Name must be of String type")

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._hometown = value
        else:
            raise TypeError("Hometown is a non-empty string")

    def concerts(self):
        return [concert for concert in Concert.all_concerts if concert.band == self]

    def venues(self):
        return [concert.venue for concert in self.concerts()]

    def play_in_venue(self, venue, date):
        concert = Concert(date, self, venue)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts()]
    
    
class Concert:
    all_concerts = set()  

    def __init__(self, date, band, venue):
        self.date = date  
        self.band = band  
        self.venue = venue 
        Concert.all_concerts.add(self)  

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Concert date must be a non-empty string")
        self._date = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise TypeError("Concert venue must be a Venue instance")
        self._venue = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise TypeError("Concert band must be a Band instance")
        self._band = value

    def hometown_show(self):
        """Returns True if the concert is in the band's hometown, False otherwise"""
        return self.band.hometown == self.venue.city

    def introduction(self):
        """Returns a string with the band's introduction for this concert"""
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"



class Venue:
    all_venues = []
    def __init__(self, name, city):
        self.name = name
        self.city = city
        Venue.all_venues.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            print("Input non-empty strings only")

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            print("Input non-empty strings only")

    @classmethod
    def all(cls):
        return cls.all_venues
    
    def concerts(self):
        return Concert.all_concerts

    def bands(self):
        return Band.all_bands