#это файл для классов доступа к данным (Data Access Object).
# Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from dao.model.movie import Movie

class MovieDAO:
    def __init__(self, session):
        self.session = session
        self.model = Movie


    #получение всех
    def get_all(self, filters):
        if filters['director_id']:
            return self.session.query(self.model).filter(
                self.model.director_id == filters['director_id']
            ).all()
        elif filters['genre_id']:
            return self.session.query(self.model).filter(
                self.model.genre_id == filters['genre_id']
            ).all()
        elif filters['year']:
            return self.session.query(self.model).filter(
                self.model.year == filters['year']
            ).all()

        return self.session.query(self.model).all()



    #получение одного по mid
    def get_by_id(self, mid):
        return self.session.query(self.model).get(mid)

    #создание
    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    #изменение
    def update(self, data):
        mid = data.pop('id')
        movie = self.get_by_id(mid)
        for field_name, field_value in data.items():
            setattr(movie, field_name, field_value)
            #movie.name = data['name'] pop позволяет убрать 'id' из data

        self.session.add(movie)
        self.session.commit()

    #удаление
    def delete(self, mid):
        movie = self.get_by_id(mid)
        self.session.delete(movie)
        self.session.commit()


