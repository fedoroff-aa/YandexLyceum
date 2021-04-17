from flask import Flask, url_for

app = Flask(__name__)


@app.route('/image_mars')
def mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1></br>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')