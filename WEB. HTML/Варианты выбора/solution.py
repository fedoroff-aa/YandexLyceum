from flask import Flask, url_for

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def mars(planet_name):
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
                    <div class="alert alert-light" role="alert"><h2 class="wait_mars">Мое предложение: {planet_name}</h2></div></br>
                    <div class="alert alert-light" role="alert"><h4>Эта планета близка к Земле;</h4></div></br>
                    <div class="alert alert-success" role="alert"><h4>На ней много необходимых ресурсов;</h4></div></br>
                    <div class="alert alert-secondary" role="alert"><h4>На ней есть вода и атмосфера;</h4></div></br>
                    <div class="alert alert-warning" role="alert"><h4>На ней есть небольшое магнитное поле</h4></div></br>
                    <div class="alert alert-danger" role="alert"><h4>Наконец, она просто красива!</h4></div></br>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')