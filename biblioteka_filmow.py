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

library = []

for i in range(4):
    film = Movie(tittle=fake.word(), year_of_production=fake.year(), type=fake.word())
    library.append(film)
    serie = Series(tittle=fake.word(), year_of_production=fake.year(), type=fake.word(), episode_number=fake.random_int(0,20), season_number=fake.random_int(0,10))
    library.append(serie)

def get_movies():
    x = [x for x in library if isinstance(x, Movie)and not isinstance(x, Series)]
    print (x)

def get_series():
    x = [x for x in library if isinstance(x, Series)]
    print (x)

def search(x):
    for i in range(len(library)):
        if library[i].tittle == x:
            print(film)

import random

def generate_view():
    for i in range(random.randint(1,100)):
        random.shuffle(library)
        library[0].play()

def multiple():
    for i in range(10):
        generate_view()

def top_titles():
    top_titles_list = []
    unsorted_list = sorted(library, key=lambda film: film.view_number, reverse= True)
    for film in unsorted_list:
        f = film
        top_titles_list.append(f)
    print (top_titles_list)

generate_view()
multiple()
print(library)
print('\n')
top_titles()
