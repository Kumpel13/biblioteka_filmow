from faker import Faker

fake = Faker()

class Movie:
    def __init__(self, tittle, year_of_production, type):
        self.tittle = tittle
        self.year_of_production = year_of_production
        self.type = type
        
        self.view_number = 0

    def play(self, step=1):
        self.view_number += step

    def __str__(self):
        return f'{self.tittle} ({self.year_of_production})'

    def __repr__(self):
        return f"Movie (tittle={self.tittle} year={self.year_of_production}, type={self.type}, view={self.view_number})"
            

class Series(Movie):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f'{self.tittle} S{self.season_number:02}E{self.episode_number:02}'

    def __repr__(self):
        return f"Serie (tittle={self.tittle} year={self.year_of_production}, type={self.type}, view={self.view_number}, episode_number={self.episode_number:02}, season_number={self.season_number:02})"

libary = []

for i in range(10):
    film = Movie(tittle=fake.word(), year_of_production=fake.year(), type=fake.word())
    libary.append(film)
    serie = Series(tittle=fake.word(), year_of_production=fake.year(), type=fake.word(), episode_number=fake.random_int(0,20), season_number=fake.random_int(0,10))
    libary.append(serie)


#def get_movies():
    

#def get_series():

first_movie = Movie(tittle="Django", year_of_production=2012, type="Western")
first_series = Series(tittle="Wiedźmin", year_of_production=2019, type="Dark fantasy",episode_number="", season_number="")

first_series.play(5)
print (first_series.view_number)
first_series.play(2)
print (first_series.view_number)
print (first_movie)
print (first_series)
print ('\n')
print(libary)