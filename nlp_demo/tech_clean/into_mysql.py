from nlp_demo.tech_clean.utils_mysql import get_conn, close_conn


def save_mysql():
    conn , cursor = get_conn()
    f = open('tech_train_res.txt', encoding='utf8')
    f_class = open('class.txt', encoding='utf8')
    data_txt = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
    data_class = f_class.readlines()    # 读出分类
    # num_1 = len(data_txt)
    # print("原始长度：" + str(num_1))
    for item in data_txt:
        temp = item.split("\t")
        temp_key = temp[0]  # 关键词
        temp_num = temp[1]  # 序号
        num_int = int(temp_num)
        temp_name = data_class[num_int].split("\t")[0]  # 分类名称
        temp_code = data_class[num_int].split("\t")[1] # 分类编码 class表示正统分类编码
        # print(temp_name)
        # print(temp_class)
        sql = "insert into `key_with_class` values (%s,%s,%s,%s)"
        param = (temp_key,temp_num,temp_name,temp_code)
        cursor.execute(sql,param)
        conn.commit()
    f.close()  # 关
    close_conn(conn, cursor)

if __name__ == '__main__':
    save_mysql()