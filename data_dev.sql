
CREATE TABLE stores (
	id INTEGER NOT NULL, 
	store_name VARCHAR(64), 
	aver_star SMALLINT, 
	PRIMARY KEY (id), 
	UNIQUE (id)
);
INSERT INTO stores VALUES(1,'HotTea',64);
INSERT INTO stores VALUES(2,'GoodPlace',2);
INSERT INTO stores VALUES(3,'WelcomeLoppy',1);
INSERT INTO stores VALUES(4,'EnjoyingTime',64);
INSERT INTO stores VALUES(5,'SexyTea',4);
INSERT INTO stores VALUES(6,'北京烤鸭',8);
CREATE TABLE stores_info (
	inner_id INTEGER NOT NULL, 
	location VARCHAR(64), 
	report_date DATE NOT NULL, 
	link VARCHAR(64) NOT NULL, 
	main_store_id INTEGER, 
	PRIMARY KEY (inner_id), 
	FOREIGN KEY(main_store_id) REFERENCES stores (id)
);
INSERT INTO stores_info VALUES(1,'a','2019-02-21','http://www.qq.com',5);
CREATE TABLE goods (
	id VARCHAR(64) NOT NULL, 
	good_kind VARCHAR(16), 
	good_name VARCHAR(128) NOT NULL, 
	good_star SMALLINT, 
	store_dish_id INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (id), 
	FOREIGN KEY(store_dish_id) REFERENCES stores (id)
);
CREATE INDEX ix_goods_good_name ON goods (good_name);
COMMIT;
