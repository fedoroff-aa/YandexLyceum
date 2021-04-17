from flask import Flask, url_for

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def mars(nickname, level, rating):
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
                    <div class="alert alert-light" role="alert"><h2>Результаты отбора</h2></div></br>
                    <div class="alert alert-light" role="alert"><h4>Претендента на участие в миссии {nickname}:</h4></div></br>
                    <div class="alert alert-success" role="alert"><h4>Поздравляем! Ваш рейтинг после {level} этапа отбора</h4></div></br>
                    <div class="alert alert-light" role="alert"><h4>составляет {rating}!</h4></div></br>
                    <div class="alert alert-warning" role="alert"><h4>Желаем удачи!</h4></div></br>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')