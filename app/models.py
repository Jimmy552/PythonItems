from . import db
import random
import json
from collections import namedtuple
from collections.abc import Sequence, AsyncIterable


'''
You can use the flask_migrate(included in this package) or something else
to manage the database and the tables,
use command 'upgrade' to ensure tables can be altered frequently according to the demands.
'''


class Store(db.Model):
    '''
    Basic Store info
    Tablename: stores;
    Primary key: id;
    Foreign key:
        stores: Record every branches detailed info of the main store(eg. Starbucks branch);
        goods: Connect to the dishes in the store;
    Store_name: store name;
    Aver_star: Score related to the store;
    '''
    __tablename__ = 'stores'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    store_name = db.Column(db.String(64))
    aver_star = db.Column(db.SmallInteger)
    # Highest star: Five star;
    # Lowest star: Zero star.

    stores = db.relationship('DetailedStore', backref='store', lazy='dynamic')
    goods = db.relationship('Good', backref='store', lazy='dynamic')

    def set_aver_star(self, *args):
        self.aver_star = sum(args)/len(args)

    @staticmethod
    def insert_items(gen_items=5):
        # onion infos
        store_names = ['GoodPlace', 'WelcomeLoppy', 'EnjoyingTime', 'SexyTea', '北京烤鸭']
        aver_stars = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
        if isinstance(gen_items, int) and gen_items < 6:
            random.shuffle(aver_stars)
            for store_name, aver_star in zip(store_names, aver_stars[:gen_items]):
                if Store.query.filter_by(store_name=store_name).first() is None:
                    db.session.add(Store(store_name=store_name, aver_star=aver_star))
            db.session.commit()
        else:
            raise ValueError('我们只能制造5条onion')

    def __repr__(self):
        return '<Store %s>' % self.store_name


class DetailedStore(db.Model):
    '''
    Tablename: stores_info;
    Primary key: inner_id;
    Foreign key: main_store_id(backref: store);
    Info:
        location: The specific location of the store;
        report_data: The time when a record is established;
        link: Connect to the article link(You can use a <web-view> container to represent);
    '''
    __tablename__ = 'stores_info'
    inner_id = db.Column(db.Integer, primary_key=True, nullable=False)
    # 分店的记录会记在这里
    location = db.Column(db.String(64))
    report_date = db.Column(db.Date, nullable=False)
    link = db.Column(db.String(64), nullable=False)
    main_store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    # def __init__(self, **other_info):
    #     # other_info 应该是一个嵌套字典的有两个元素的元组或列表或其他
    #     if other_info:
    #         try:
    #             for item_name, addition in other_info:
    #                 self.item_name = db.Column(getattr(db, addition['type']), **addition.pop('type'))
    #         except Exception as e:
    #             pass

    def __repr__(self):
        return '<Store(Detailed) %s>' % self.store.store_name


class Good(db.Model):
    '''
    The basic goods info
    Tablename: goods;
    Primary key: id;
    Foreign key: store_dish_id(backref: store);
    Good_kind: ("好吃 还是 好玩")(Here you may have another choices like ("好吃又好玩");
    Good_name: that's it, right.(eg. '北京烤鸭');
    Good_star: score;
    '''
    __tablename__ = 'goods'
    id = db.Column(db.String(64), primary_key=True, unique=True)
    good_kind = db.Column(db.String(16))
    good_name = db.Column(db.String(128), index=True)
    good_star = db.Column(db.SmallInteger)
    store_dish_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    def __repr__(self):
        return '<Good %s>' % self.good_name

    @staticmethod
    def insert_item(gen_items=4):
        good_kinds = ['Playful', 'Tasty', 'WeAllLike']
        aver_stars = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
        good_names = ['北京烤鸭', 'LongJing', 'Tianfu_Park', 'SwimmingPool']
        if isinstance(gen_items, int) and gen_items < 5:
            random.shuffle(aver_stars)
            random.shuffle(good_kinds)
            for good_kind, aver_star, good_name in zip((good_kinds*2)[:gen_items], aver_stars[:gen_items], good_names):
                # if Good.query.filter_by(good_name=good_name).first() is None:
                good = Good(good_kind=good_kind, good_star=aver_star, good_name=good_name)
                db.session.add(good)
                db.session.commit()
        else:
            raise ValueError('Only 4 onion infos can we make')


