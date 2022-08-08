# -*- coding: utf-8 -*-
from movie1 import *
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests
import pandas as pd
import bs4

app = Flask(__name__)

# Channel Access Token
Channel_Access_Token = 'your token'
line_bot_api = LineBotApi(Channel_Access_Token)
# Channel Secret
Channel_Secret = 'your Channel Secret'
handler = WebhookHandler(Channel_Secret)

line_bot_api.push_message('your ID', TextSendMessage(text='請開始你的表演'))


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

 
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'






@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    map=["台北市","新北市","桃園市","新竹市","苗栗市","台中市","彰化市",""]
    type1=["火鍋","燒肉","日式","泰式","漢堡","美式","韓式"]
    stockname=['0050','0056','2300']

    message  = TextSendMessage(text='http://www.google.com.tw/maps/place/'+event.message.text)
    message1 = TextSendMessage(text='https://tw.news.yahoo.com/')
    message2 = TextSendMessage(text='https://ifoodie.tw/explore/%E5%8F%B0%E5%8C%97%E5%B8%82/list/'+event.message.text)
    message3 = TextSendMessage(text=movie1())
    #message4 = TextSendMessage(text=stock3(event.message.text))


    if event.message.text in map:
        line_bot_api.reply_message(event.reply_token,message) 
    elif "新聞" in event.message.text:
        line_bot_api.reply_message(event.reply_token,message1)
    elif event.message.text in type1:
        line_bot_api.reply_message(event.reply_token,message2)

    elif event.message.text in stockname:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=stock3(event.message.text)))

    elif "電影" in event.message.text:
        line_bot_api.reply_message(event.reply_token,message3)
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("還有什麼需要服務"))




#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)




