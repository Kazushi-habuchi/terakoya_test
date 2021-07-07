from flask import Flask, render_template, request, make_response, send_file

app = Flask(__name__)


@app.route('/')
def main():
    host = request.headers['HOST']
    if host == 'car.com:5000':
        return make_response(render_template("01_car_com.html"))
    elif host == 'news.com:5000':
        return make_response(render_template("01_news_com.html"))
    elif host == 'banner.com:5000':
        referer_history = request.cookies.get('referer_history')
        if referer_history == 'http://car.com:5000/':
            response = send_file('banners/banner_car.jpg', mimetype='image/jpg')
        else:
            response = send_file('banners/banner_random.png', mimetype='image/png')
            response.set_cookie('referer_history', request.referrer)
        return response
    else:
        return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
