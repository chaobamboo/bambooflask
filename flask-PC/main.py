# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
import numpy as np

app = Flask(__name__)

# Main
def picked_up():
    messages = [
        "こんにちは、あなたの名前を入力してください",
        "やあ！お名前は何ですか？",
        "あなたの名前を教えてね"
    ]
    return np.random.choice(messages)

# Routing
@app.route('/profile')
def profile():
    title = "profile"
    img_url = '/static/pictures/oohuka.jpg'
    return render_template('profile.html',
                           user_company_name='Dreamove',
                           user_position='CEO', user_whoiam='1982年岡山生まれ。高校卒業後上京。18歳から音楽イベント主催し、日本各地での開催や、ノンスポンサーで450人のクルージングイベントを成功させる。 東京～岡山を台風の中、2日間かけてママチャリで走破したことが武勇伝。見かけとは裏腹に、まじめで固い性格&とにかくアツイ。 不動産事業では、紹介＆口コミのみで賃貸紹介や店舗の探しを行っている。 お客様よりもお客様のことを想い夢が実現される空間とご縁を繋ぐことに命をかけている。',user_last_name ='大深',user_first_name ='譲',
                           title=title, img_url=img_url)
@app.route('/')
def index():
    title = "ようこそ"
    message = picked_up()
    return render_template('index.html',
                           message=message, title=title)

@app.route('/post', methods=['POST', 'GET'])
def post():
    title = "こんにちは"
    if request.method == 'POST':
        name = request.form['name']
        return render_template('index.html',
                               name=name, title=title)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
