# _*- coding: utf-8 -*-
import web

urls=(
'/','index',
'/movie/(\d+)', 'movie'
)

db=web.database(dbn='sqlite',db='MovieSite.db')
movies=db.select('movie')

render=web.template.render('templates/')

class movie:
    def GET(self, movie_id):
        movie_id = int(movie_id)
        movie = db.select('movie', where='id=$movie_id', vars=locals())[0]
        return render.movie(movie)

class index:
    def GET(self):
        return render.index(movies)

    def POST(self):
        data=web.input()
        # r'' 为了防止python对 % 进行转义
        condition=r'title like "%' + data.title + r'%"'
        movies=db.select('movie', where=condition)
        return render.index(movies)

if __name__ == "__main__":
    app=web.application(urls, globals())
    app.run()
