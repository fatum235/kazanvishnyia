from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/image_mars')
def index():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="/static/img/mars.jpg">
                      </body>
                    </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
