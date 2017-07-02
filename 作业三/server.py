#-*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler
import json

data = [
    {
        "date": "2014-10-28",
        "time": "15:37:21",
        "name": "手机50元话费充值",
        "number": 1,
        "eCoin": 190,
        "status": "兑换失败",
        "info": "充值失败，E币已退回"
    },
    {
        "date": "2014-10-23",
        "time": "21:36:44",
        "name": "手机50元话费充值",
        "number": 1,
        "eCoin": 190,
        "status": "兑换失败",
        "info": "充值失败，E币已退回"
    },
    {
        "date": "2014-10-21",
        "time": "15:29:18",
        "name": "手机50元话费充值",
        "number": 1,
        "eCoin": 190,
        "status": "兑换失败",
        "info": "充值失败，E币已退回"
    },
    {
        "date": "2014-10-21",
        "time": "15:06:51",
        "name": "手机50元话费充值",
        "number": 1,
        "eCoin": 190,
        "status": "兑换失败",
        "info": "充值失败，E币已退回"
    },
    {
        "date": "2014-10-10",
        "time": "14:56:28",
        "name": "手机50元话费充值",
        "number": 1,
        "eCoin": 190,
        "status": "兑换失败",
        "info": "充值失败，E币已退回。测试用例"
    },
    {
        "date": "2014-09-25",
        "time": "14:03:00",
        "name": "手机50元话费充值",
        "number": 1,
        "eCoin": 190,
        "status": "兑换失败",
        "info": "充值失败，E币已退回"
    },
    {
        "date": "2014-09-24",
        "time": "11:35:38",
        "name": "手机50元话费充值",
        "number": 1,
        "eCoin": 190,
        "status": "兑换失败",
        "info": "充值失败，E币已退回。测试用例"
    },
    {
        "date": "2014-09-24",
        "time": "11:34:59",
        "name": "博洋梦澜棉被",
        "number": 1,
        "eCoin": 1049,
        "status": "兑换失败",
        "info": "您兑换的商品申请处理失败，金币已退回。测试用例"
    },
    {
        "date": "2014-09-22",
        "time": "15:34:23",
        "name": "手机50元话费充值",
        "number": 1,
        "eCoin": 190,
        "status": "兑换失败",
        "info": "充值失败，E币已退回"
    },
    {
        "date": "2014-09-01",
        "time": "12:38:36",
        "name": "手机50元话费充值",
        "number": 1,
        "eCoin": 190,
        "status": "兑换失败",
        "info": "充值失败，E币已退回"
    },
    {
        "date": "2014-08-29",
        "time": "18:26:05",
        "name": "手机50元话费充值",
        "number": 1,
        "eCoin": 190,
        "status": "兑换失败",
        "info": "充值失败，E币已退回。失败处理。"
    },
    {
        "date": "2014-08-29",
        "time": "18:24:37",
        "name": "米奇真空古堡杯",
        "number": 1,
        "eCoin": 323,
        "status": "兑换失败",
        "info": "您兑换的商品申请处理失败，金币已退回。处理中。失败处理。"
    },
    {
        "date": "2014-08-18", 
        "time": "17:41:38",
        "name": "手机50元话费充值",
        "number": 1,
        "eCoin": 190,
        "status": "兑换失败",
        "info": "充值失败，E币已退回"
    }
]

class searchHandler(RequestHandler):
    def check_origin(self, origin):
        return True
    def get(self):
        msg = json.dumps(data)
        self.write(msg)

def make_app():
    return tornado.web.Application([
        (r"/search", searchHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print ('server start')
    tornado.ioloop.IOLoop.current().start()
