import redis
import MySQLdb
import json

#没有完全确定break时机
#基于MySQLdb的, pymysql有可能有些许差别
def prosses():
	rediscli = redis.Redis(host='127.0.0.1', port=6379, db=0)
	mysqlcli = MySQLdb.connect(host = '127.0.0.1', port=3306, user='root', passwd='0000')
	
	cursor = mysqlcli.cursor()
	cursor.execute('use database;')
	
	#循环pop数据
	while True:
		# 将数据pop出来. data存储时就是json数据
		source, data = rediscli.blpop('field')
		
		try:
			data = json.loads(data)
		except:
			break
		
		cursor.execute('insert into tableN (usr, id, age, time) values(%s)'
		%(data['usr'], data['id'], data['age'], data['time']))
		
		mysqlcli.commit()
	cursor.close()

if "__name__" == "__main__":
	prosses()