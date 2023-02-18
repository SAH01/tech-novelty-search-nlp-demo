import json
import random
from nlp_demo.tech_clean.utils_mysql import query
"""
关键词（使用英文逗号分隔） \t 分类号（从0开始）
------------------
分类名称表【tech_name.txt】
医药、卫生
一般工业技术
生物科学
数理科学和化学
农业科学
  "R": "0",
  "TB": "1",
  "Q": "2"
"""
def get_tech_data():
    with open("../tech_data/tech_word.json", "r", encoding='utf-8') as fo:
        # print(fo.read())
        table_word = json.loads(fo.read())  # json 转 字典

    # 使用上面的数据 拼接字符串 拼接表名 k 是字母号 v 是名称
    for techWord,techNum in table_word.items():
        print("正在处理的类别：  " + techWord , techNum)
        sql = "select * from tech_"+ techWord
        # 第7个位置是 中文关键词 第16个位置是中图分类名称
        res_one_class = query(sql)      # 查出来结果 ((),(),)
        for res_one_class_item in res_one_class:
            keywordsCn = str(res_one_class_item[7])
            if (keywordsCn == "" or keywordsCn == None):
                continue
            else:
                keywordsCn1 =  keywordsCn.replace(";"," ") # 替换英文; 为 空格
                keywordsCn2 = keywordsCn1.replace("；"," ") # 替换中文；为 空格
                keywordsCn3 = keywordsCn2.replace("\n"," ") # 替换换行符为 空格
                keywordsCn2List = keywordsCn2.split(" ")
                write_str = "" # 最终写入的字符串
                for item in keywordsCn2List :
                    if (len(item) == 0):
                        continue
                    else:
                        # print(item)
                        write_str = write_str + item + " "
                with open("../tech_res_data/tech_train" + ".txt",
                    "a+", encoding='utf-8') as fw:
                    fw.write(write_str + "\t" + techNum + "\n")
        print("============= 这是分隔符 =============")
        fw.close()
    return 0

if __name__ == '__main__':
    get_tech_data()