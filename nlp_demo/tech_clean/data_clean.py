import json

from nlp_demo.tech_clean.utils_mysql import query


def get_class_json():
    f_class = open ("../tech_data/tech_name_class.txt", "r", encoding='utf-8')
    res_dict = {}
    while True:
        line = f_class.readline()
        if line:
            # print(line)
            # 按\t分隔 分开名称和序号
            temp_str_list = line.split("\t")
            class_name = str(temp_str_list[0])
            class_num = str(temp_str_list[1].replace("\n",""))
            res_dict[class_name] = class_num
            # print("-------------------------")
        else:
            break
    print(json.dumps(res_dict,ensure_ascii=False))
    class_json = json.dumps(res_dict,ensure_ascii=False)
    with open("../tech_data/tech_order_class.json", "w", encoding='utf-8') as f:
        f.write(class_json)  # 自带文件关闭功能，不需要再写f.close()
    f_class.close()
    return

# 处理语料
"""
处理训练集数据格式【tech_train.txt】
关键词（使用英文逗号分隔） \t 分类号（从0开始）
-----
分类名称表【tech_name_class.txt】
分类名称 \t 分类号（从0开始）
"""
def get_tech_data():
    with open("../tech_data/tech_class.json", "r", encoding='utf-8') as fo:
        # print(fo.read())
        table_name = json.loads(fo.read())  # json 转 字典
    with open("../tech_data/tech_order_class.json", "r", encoding='utf-8') as fo_1:
        # print(fo.read())
        tech_class = json.loads(fo_1.read())  # json 转 字典
    # print(table_name)
    # 使用上面的数据 拼接字符串 拼接表名 k 是字母号 v 是名称
    for k,v in table_name.items():
        order_num = None
        if(k == None or v == None):
            continue
        for k1, v1 in tech_class.items():
            # k1 是名称 v1 是数字序号
            if(v == k1):
                order_num = v1
        print("正在处理的类别：  " + k , v)
        k = str(k)
        v = str(v)
        sql = "select * from tech_"+ k
        # print("这是sql语句： " + sql)
        # 第7个位置是 中文关键词 第16个位置是中图分类名称
        res_one_class = query(sql)
        for res_one_class_item in res_one_class:
            keywordsCn = str(res_one_class_item[7])
            classification = str(order_num)
            print(keywordsCn + " --------> " + classification)
            with open("../tech_res_data/tech_" +k+ ".txt","a+",encoding='utf-8') as fw:
                fw.write(keywordsCn.replace("；",",") + "\t" + classification + "\n")
        print("============= 这是分隔符 =============")
    return 0
if __name__ == '__main__':
    # get_class_json()    # 生成json格式的分类名称文件
    get_tech_data()