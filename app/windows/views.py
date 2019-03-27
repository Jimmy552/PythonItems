from . import window
import flask_migrate
from ..models import Store, DetailedStore, Good
from flask import Request, request
import datetime
import json


ERROR_LOGGING = []


class DateEnconding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.date):
            return o.strftime('%Y/%m/%d')
# ---------------------
# 作者：jlbill
# 来源：CSDN
# 原文：https://blog.csdn.net/qq_42226324/article/details/82989304
# 版权声明：本文为博主原创文章，转载请附上博文链接！

# A test
@window.route('/', methods=['POST', 'GET'])
def index():
    # decide_what = str(json.loads(request.values.get('decision')))
    # decision 中存储好吃还是好玩
    query = Store.query.all()
    query_dict = {store.store_name: store.aver_star for store in query}
    if not query_dict:
        query_dict = {'return_value': False}
    return json.dumps(query_dict)


@window.route('/post', methods=['POST'])
def postdata():
    # postdata = request.data
    # try:
    #     print(request.values)
    #     print(request.data)
    # except:
    #     print('Unluckily')
    # if postdata:
    #     data = json.loads(postdata)
    #     print(repr(data))
    # try:
    #     store = 'SexyTea'
    #     # 这是测试代码
    #     t = request.data
    #     try:
    #         m = json.loads(t)
    #         print(repr(m), type(m), sep='\t', end='\n')
    #         s = m.get('store')
    #         print(repr(s), type(s), sep='\t', end='\n')
    #         try:
    #             ss = json.loads(s)
    #             print(repr(ss), type(ss), sep='\t', end='\n')
    #             store = ss
    #         except TypeError as e:
    #             print(e, end='\tError\n')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #     print(repr(t), type(t), sep='\t', end='\n')
    #
    # except json.decoder.JSONDecodeError as e:
    #     print(e)
    #     store = False
    #
    try:
        store = json.loads(request.data).get("store")
        store = json.loads(store)
    except json.decoder.JSONDecodeError as e:
        ERROR_LOGGING.append(e)
        store = False
    if store:
        try:
            main_store = Store.query.filter_by(store_name=store).first()
            branches = main_store.stores.all()
            # 列举所有的分店
        except AttributeError as e:
            ERROR_LOGGING.append(e)
            return json.dumps('No branches')
        if branches:
            query_list = \
                [{"location": store.location, "report_date": store.report_date, "link": store.link}
                 for store in branches]
            return json.dumps(query_list, cls=DateEnconding)
    return json.dumps('No store data available')


