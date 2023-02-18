"""
name
document_type
document_area
document_id
publish_type
organ
pass_date
publish_date
exe_date
document_target
theme_words
key_words
text

"""
import time
from datetime import datetime

from 处理正文格式.utils_mysql import query, get_conn

sql = "select `name` ,document_type, document_area, document_id, publish_type,organ, pass_date, publish_date, exe_date, document_target, theme_words, key_words, text from policy_enter"
res=query(sql)
print("数据总长度： " + str(len(res)))
print("单条数据长度为； "+str(len(res[0])))
conn,cursor = get_conn()
count = 0
for item in res:
      # print(item[0]+"\t"+item[6] +"\t"+ str(type(item[6])))
      if(item[6]=="" or item[7] == "" or item[8] == ""):
            continue
      pass_date = item[6].replace(".","-")
      publish_date = item[7].replace(".","-")
      exe_date = item[8].replace(".", "-")

      pass_date_0 = datetime.strptime(pass_date,"%Y-%m-%d")
      pass_date_1 = datetime.strptime(publish_date, "%Y-%m-%d")
      pass_date_2 = datetime.strptime(exe_date, "%Y-%m-%d")
      print(pass_date_0)
      sql_into = "insert into policy_new(`name`,`type`,`range`,`document`,`form`,`organ`,`viadata`,`pubdata`,`perdata`" \
                 ",`category`,`theme`,`keyword`,`text`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
      cursor.execute(sql_into,[item[0],item[1],item[2],item[3],item[4],item[5],
                               pass_date_0,pass_date_1,pass_date_2,
                               item[9],item[10],item[11],item[12]])
      conn.commit()
      count = count + 1
      print(str(count))
