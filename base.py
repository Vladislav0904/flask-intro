from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index_1():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    deviz = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(deviz)


@app.route('/image_mars')
def image_mars():
    return f'''
<!DOCTYPE html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <title>Привет, Марс!</title>
            </head>
            <body>
            <h1> Жди нас, Марс! </h1>
            <img src='{url_for('static', filename='img/mars_planet.png')}'>
            </body>
            </html>
'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
