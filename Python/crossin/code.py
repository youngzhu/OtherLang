# _*- coding: utf-8 -*-
import web

urls=(
'/','index',
'/movie/(\d+)', 'movie',
'/cast/(.*)', 'cast',
)

db=web.database(dbn='sqlite',db='MovieSite.db')
movies=db.select('movie')
count=db.query('SELECT COUNT(*) AS COUNT FROM movie ')[0]['COUNT']

render=web.template.render('templates/')

class movie:
    def GET(self, movie_id):
        movie_id = int(movie_id)
        movie = db.select('movie', where='id=$movie_id', vars=locals())[0]
        return render.movie(movie)

class index:
    def GET(self):
        return render.index(movies, count, None)

    def POST(self):
        data=web.input()
        # r'' 为了防止python对 % 进行转义
        condition=r'title like "%' + data.title + r'%"'
        movies=db.select('movie', where=condition)
        count=db.query('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)[0]['COUNT']
        return render.index(movies, count, data.title)

class cast:
    def GET(self, cast_name):
        condition=r'casts like "%' + cast_name + r'%"'
        movies=db.select('movie', where=condition)
        count=db.query('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)[0]['COUNT']
        return render.index(movies, count, cast_name)

if __name__ == "__main__":
    app=web.application(urls, globals())
    app.run()
