
# test = ";;123;4"
# test1 = test.split(";")
# print("长度为："+str(len(test1))+"\n")
# # print(test1[0])
# for item in test1:
#     if (len(item) == 0):
#         print("hh")
#         continue
#     else:
#         print(item)
# 尝试正则表达式匹配
"""
[\w;?]{2,}
"""
# import re
#
# myList = ["退化草地;;;改良措施;","硫化氢;呼吸节律;"]
#
# for data in myList:
#     dataNew3 = re.match('^(?=.*;;).*$',data)
#     print(dataNew3)

# 找出多余的 制表符
def find_more_t():
    f=open('tech_train_res.txt',encoding='utf8')
    data_txt = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
    num_1 = len(data_txt)
    print("原始长度："+str(num_1))
    count = -1
    for item in data_txt:
        # print(i)
        count = count + 1
        if (len(item.split("\t"))>=2):
            print(data_txt[count])
            # data_txt.pop(count)
    f.close()  # 关
    print("查找后长度："+str(len(data_txt)))
    # for i in data_txt:
    #     with open("../tech_res_data/tech_train_res" + ".txt",
    #               "a+", encoding='utf8') as fw:
    #         fw.write(i)
    # fw.close()


if __name__ == '__main__':
    find_more_t()


