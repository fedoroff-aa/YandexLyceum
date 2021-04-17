from flask import Flask, url_for

app = Flask(__name__)


@app.route('/promotion_image')
def mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                  </head>
                  <body>
                    <h1 class="wait_mars">Жди нас, Марс!</h1></br>
                    <img src="{url_for('static', filename='img/mars.jpg')}" alt="здесь должна была быть картинка, но не нашлась"></br></br>
                    <div class="alert alert-dark" role="alert">Человечество вырастает из детства.</div></br>
                    <div class="alert alert-success" role="alert">Человечеству мала одна планета.</div></br>
                    <div class="alert alert-secondary" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</div></br>
                    <div class="alert alert-warning" role="alert">И начнем с Марса!</div></br>
                    <div class="alert alert-danger" role="alert">Присоединяйся!</div></br>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')