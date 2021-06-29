from flask import Flask, render_template, request, make_response, send_file

app = Flask(__name__)


@app.route('/')
def main():
    host = request.headers['HOST']
    if host == 'car.com:5000':
        return make_response(render_template("02_car_com_https.html"))
    elif host == 'news.com:5000':
        return make_response(render_template("02_news_com_https.html"))
    elif host == 'banner.com:5000':
        referer_history = request.cookies.get('referer_history')
        if referer_history == 'https://car.com:5000/':
            response = send_file('banners/banner_car.jpg', mimetype='image/jpg')
        else:
            response = send_file('banners/banner_random.png', mimetype='image/png')
            response.set_cookie('referer_history', request.referrer, samesite='None', secure=True)
        return response
    else:
        return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(ssl_context=('ssl/server.crt', 'ssl/server.key'), host='0.0.0.0', debug=True)