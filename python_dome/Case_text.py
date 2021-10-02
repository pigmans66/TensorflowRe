# #列表 元组 字典 集合 创建、常用方法的使用、
# #for if else \if elif else操作
#
#
# #列表的创建  里面的可以存放多种类型
# class text_obj:
#     def __init__(self,name):
#         self.name=name
#
# text_date=[text_obj("xioawu"),[1,2,3,4],(1,2,3,),{"case1":"xiaochen","case2":"xiaowang"}]
# text_date.append("chen")
# print(text_date.pop())
#
# #字典
# text_date2={"xiaochen":'23',"dfa":23}
# for i in text_date2.keys():
#     print(i)
# for i in text_date2.values():
#     print(i)
# for keys,values in text_date2.items():
#     print(keys,values)
#
# text_string="""
# *chen
# *yin
#    *fasdf
# """
# print(text_string)
#
#
# tuple_case=(text_date2)
# text_date2.update({"chend":23})
# #集合set 数据不重复
#
# set_case={1,2,12,2,2,}
# # set_case2=set([])
# print(set_case)
# # tan_shape=[99][99]
# # heat_shape=[99][99]
# # for i in range(18):
# #     print("{}{}".format(' '*(100-i),"*"*(2*i)))
#
# tuple_case1=([1,2,3,4])
# tuple_case[1]=23
# print(tuple_case1)
# # 全局变量的使用 globel
# def sum1(a,v):
#     global c
#     c=a+v
#     return c
# result=sum1(1,4)
# print(result)
# print(c)

#类的继承 以文件为操作
import time
# print("类")
# class File:
#     def __init__(self,name):
#         self.name=name
#         self.time=time.asctime()
#     def change_file_name(self,new_name):
#         self.name=new_name
#         return self.name
# my_file=File("Case.py")
# print(my_file)
# new_file_name=my_file.change_file_name("modify_name")
# print(new_file_name)
#
# print("继承")
# class Files:
#     def __init__(self, name):
#         self.name = name
#         # self.time = time.asctime()
#
#     def change_file_name(self, new_name):
#         self.name = new_name
#         return self.name
#     # def Fil_Inf(self):
#     #    return self.name,self.time
#
# # 问题继承父类的基础上  出现增加的属性没有定义的情况 问题在init 写成ini
# class Video(Files):
#     def __init__(self,name,wind=12):
#         # 在父类基础上再增加属性
#         super().__init__(name=name)
#         self.wind=wind
#     # def super_inf(self):
#     #     print(self.name,self.wind)
#     # def Inf(self,name):
#     #     self.change_file_name(name)
#     def Inf(self):
#         return self.name
# class Text:
# file1=Files("一生一世")
# Video1.super_inf()
# print(Video1.name)
# print(video1.window_size)
# file=Files("周生如故")

#私有方法 私有属性  保护属性
# import time
# class roles:
#     def __init__(self,name,level,sex):
#         self.name=name
#         self.level=level
#         self.__id=time.asctime()
#         self._sex=sex
#         #私有属性还是可以通过内部方法进行访问
#     #可以通过repr内置方法  改变输出对象的 从地址改变为所需的内容
#     # def __repr__(self):
#     #     return "roles:name:{} level:{} id:{} sex:{}".format(self.name,self.level,self.__id,self._sex)
#     #与repr功能类似
#     def __str__(self):
#         return "roles:name:{} level:{} id:{} sex:{}".format(self.name,self.level,self.__id,self._sex)
#
#     def _Get_roles(self):
#         return self._sex,self.__id
#     # 私有方法可以当做内部执行操作命令
#     def __get_id(self):
#         return self.__id
# roles1=roles("关羽",13,'man')
# print(roles1)
# # print(roles1.name)
# # print(roles1._sex)
# #无法访问私有属性
# # print(roles1.__id)
# # print(roles1._Get_roles())
#
# # class atack():
# #     def __repr__(self):

#__iter__ __next__两种方法的实现
# class case:
#     def __init__(self,data):
#         self.data=data
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.data>5:
#             raise  StopIteration
#         else:
#             self.data+=1
#             return self.data
# for i in case(3):
#     print(i)

#将上面案例扩展到列表为对象
# 下列案例没有解决
# class case():
#     def __init__(self,roles):
#         self.roles=roles
#     def __iter__(self):
#         print("iter:",self.roles)
#         return self
#     def __next__(self):
#         if self.roles=="xiaowu":
#             raise StopIteration
#         else:
#           return self.roles
# for i in  case(["xiaochen","xiaowang","xiaowu","xiaogao"]):
#     print()
# from .shape_dome import tans_case


#module方法 两点
# from 目录.文件名 import 方法名  这种方式是在不同目录下实现
# .文件名 同一个目录下


# 文件操作  文件写入  文件读取  二进制方式、txt形式 以及  encoding在读入和写入使用 各种mode形式 除了常见的外  ab w+ r+ a+ x
#以及seek(0)调到开头
# with open("new_file.txt","w+") as f:
#     f.write("w的模型进行写入")
#     f.seek(0)
#     print(f.read())
# with open("new_file.txt","r") as f:
#     print(f.read())
# with open("new_file.txt","wb") as f:
#     # f.seek()
#     f.write("wb模式进行写入操作且编码所gbk".encode("gbk"))
# with open("new_file.txt",encoding="gbk") as f:
#     print(f.read())
# with open("new_file.txt","a+") as f:
#     f.write("接着写入操作")
# with open('new_file.txt',"r") as f:
#     print(f.read())
# with open("new_file1.txt",'ab') as f:
#     f.write('dsfaf'.encode("gbk"))
# with open("new_file.txt","a") as f:
#     # print(f.readlines())
#     f.writelines("\nwaga")
# with open("new_file.txt",'ab') as f:
#     f.write('0101010'.encode("gbk"))