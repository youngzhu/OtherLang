import web

urls=(
'/','index'
)

db=web.database(dbn='sqlite',db='MovieSite.db')
movies=db.select('movie')

render=web.template.render('templates/')

class index:
    def GET(self):
        return render.index(movies)

if __name__ == "__main__":
    app=web.application(urls, globals())
    app.run()
