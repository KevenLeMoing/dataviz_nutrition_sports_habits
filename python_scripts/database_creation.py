import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='lifesum',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

#@TODO --> ADD constraint, primary key.
