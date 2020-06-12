# coding=utf-8
"""逻辑处理"""


def get_home():
    """获取图书馆主页资料，一般是读取数据库或者缓存系统"""
    return "data of home page"


def get_books():
    """获取所有书籍信息"""
    return "list of books basic info"


def get_book(book_id):
    """获取一本书的信息"""
    return "derailed info of book : {}".format(book_id)


def get_students():
    """获取所有学生列表"""
    return "list of students basic info"


def get_student(student_id):
    """获取一名学生的信息"""
    return "derailed info of student : {}".format(student_id)