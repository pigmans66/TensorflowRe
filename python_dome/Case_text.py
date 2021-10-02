#列表 元组 字典 集合 创建、常用方法的使用、
#for if else \if elif else操作


#列表的创建  里面的可以存放多种类型
class text_obj:
    def __init__(self,name):
        self.name=name

text_date=[text_obj("xioawu"),[1,2,3,4],(1,2,3,),{"case1":"xiaochen","case2":"xiaowang"}]
text_date.append("chen")
print(text_date.pop())

#字典
text_date2={"xiaochen":'23',"dfa":23}
for i in text_date2.keys():
    print(i)
for i in text_date2.values():
    print(i)
for keys,values in text_date2.items():
    print(keys,values)

text_string="""
*chen
*yin
   *fasdf
"""
print(text_string)


tuple_case=(text_date2)
text_date2.update({"chend":23})
#集合set 数据不重复

set_case={1,2,12,2,2,}
# set_case2=set([])
print(set_case)
# tan_shape=[99][99]
# heat_shape=[99][99]
# for i in range(18):
#     print("{}{}".format(' '*(100-i),"*"*(2*i)))