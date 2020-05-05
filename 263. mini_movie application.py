class movie:
    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def display(self):
        print('Title is :', self.title)
        print('hero is:', self.hero)
        print('Heroine is:', self.heroine)


list_of_movies=[]
while True:
    title=input('Enter the movie name:')
    hero=input('enter the hero name:')
    heroine=input('enter the heroine name:')
    m=movie(title,hero,heroine)
    m=list_of_movies.append(m)
    option = input('want more movies[y/n]')
    if option.lower()=='n':
        break
print('all movie info')
for movie in list_of_movies:
    movie.display()
    print()