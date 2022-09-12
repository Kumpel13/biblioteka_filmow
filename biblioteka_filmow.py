import random

class Movie:
    def __init__(self, title, year_of_production, type):
        self.title = title
        self.year_of_production = year_of_production
        self.type = type
        
        self.view_number = 0

# Pkt 3 Filmy i seriale mają metodę play
    def play(self, step=1):
        self.view_number += step

    def __str__(self):
        return f'{self.title} ({self.year_of_production})'

    def __repr__(self):
        return f"Movie (tittle={self.title} year={self.year_of_production}, type={self.type}, view={self.view_number})"
            
class Series(Movie):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f'{self.title} S{self.season_number:02}E{self.episode_number:02}'

    def __repr__(self):
        return f"Serie (tittle={self.title} year={self.year_of_production}, type={self.type}, view={self.view_number}, episode_number={self.episode_number:02}, season_number={self.season_number:02})"

film_1 = Movie(title='B', year_of_production=2022, type='Comedy')
film_2 = Movie(title='A', year_of_production=2020, type='Drama')
film_3 = Movie(title='C', year_of_production=1998, type='Thriller')

Serie_1 = Series(title='E', year_of_production=2021, type='Comedy', episode_number=random.randint(1,20), season_number=random.randint(1,10))
Serie_2 = Series(title='D', year_of_production=2019, type='Drama', episode_number=random.randint(1,20), season_number=random.randint(1,10))
Serie_3 = Series(title='F', year_of_production=2000, type='Horror', episode_number=random.randint(1,20), season_number=random.randint(1,10))

# Pkt 4 Po wyświetleniu serialu jako string pokazują się informacje o konkretnym odcinku, np.: “The Simpsons S01E05"
print ("Punkt 4")
print (Serie_1)

# Pkt 5 Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”
print('----------------------------')
print("Punkt 5")
print (film_1)

# Pkt 6 Przechowuje filmy i seriale w jednej liście
library = [film_1, film_2, film_3, Serie_1, Serie_2, Serie_3]

# Pkt 7 Napisz funkcje get_movies oraz get_series posortowaną alfabetycznie

def get_movies():
    x = [x for x in library if isinstance(x, Movie)and not isinstance(x, Series)]
    y = sorted(x, key=lambda film: film.title)
    return y

print('----------------------------')
print("Punkt 7")
print (get_movies())

def get_series():
    x = [x for x in library if isinstance(x, Series)]   
    y = sorted(x, key=lambda serie: serie.title)
    return y

print('\n')
print (get_series())

# Pkt 8 Napisz funkcję search, która wyszukuje film lub serial po jego tytule.
def search(x):
    lista = []
    for film in library:
        if film.title == x:
            lista.append(film)
    return lista

print('----------------------------')
print("Punkt 8")
print (search('A'))

# Pkt 9 Napisz funkcję generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.
def generate_view():
    film_id = random.choice(library)
    how_many = random.randint(1, 100)
    for i in range(how_many):
        film_id.play()        
    return film_id,

print('----------------------------')
print("Punkt 9")
print (generate_view())

# Pkt 10 Napisz funkcję, która uruchomi generate_views 10 razy.
def multiple():
    for i in range(10):
        generate_view()
    return generate_view()    

print('----------------------------')
print("Punkt 10")
print (multiple())      

# Pkt 11 Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych tytułów z biblioteki.
def top_titles():
    n = 3
    sorted_list = sorted(library, key=lambda film: film.view_number, reverse= True)  
    return sorted_list[:n]

print('----------------------------')
print("Punkt 11")
print (top_titles())          