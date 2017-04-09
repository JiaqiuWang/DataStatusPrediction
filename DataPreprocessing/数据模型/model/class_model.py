"""
个人数据集成模型, User, Stack, SNS, Blog, Git, Media 6大数据类
"""

# 用户类


class User:
    # 构造函数
    def __init__(self, uid, u_name, location, URL):
        self.uid = uid
        self.u_name = u_name
        self.location = location
        self.URL = URL
        self.education = ""
        self.skill = []
        self.job_exper = ""

    def get_uid(self):
        return self.uid

    def set_uid(self, new_uid):
        self.uid = new_uid

    def get_username(self):
        return self.u_name

    def set_username(self, new_name):
        self.u_name = new_name

    def get_location(self):
        return self.location

    def set_location(self, new_l):
        self.location = new_l

    def get_URL(self):
        return self.URL

    def set_URL(self, NEW_U):
        self.URL = NEW_U

    def get_job_exper(self):
        return self.job_exper

    def set_job_exper(self, new_j):
        self.job_exper = new_j

# ---------------------------------------------------------------------------

# 问答服务数据类


class Stack:
    # 构造函数
    def __init__(self, uid, u_name, datetime, timestamp, service,
                 activity, title, content):
        self.uid = uid
        self.u_name = u_name
        self.datetime = datetime
        self.timestamp = timestamp
        self.service = service
        self.activity = activity
        self.title = title
        self.content = content

    def get_uid(self):
        return self.uid

    def set_uid(self, new_uid):
        self.uid = new_uid

    def get_username(self):
        return self.u_name

    def set_username(self, new_name):
        self.u_name = new_name

    def get_datetime(self):
        return self.datetime

    def set_datetime(self, value):
        self.datetime = value

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, value):
        self.timestamp = value

    def get_service(self):
        return self.service

    def set_service(self, value):
        self.service = value

    def get_activity(self):
        return self.activity

    def set_activity(self, value):
        self.activity = value

    def get_title(self):
        return self.title

    def set_title(self, value):
        self.title = value

    def get_content(self):
        return self.content

    def set_content(self, value):
        self.content = value

# ---------------------------------------------------------------------------

# 社交网络服务数据类：Twitter, Google Plus, Facebook


class SNS:
    # 构造函数
    def __init__(self, uid, u_name, datetime, timestamp, service,
                 activity, title, content):
        self.uid = uid
        self.u_name = u_name
        self.datetime = datetime
        self.timestamp = timestamp
        self.service = service
        self.activity = activity
        self.title = title
        self.content = content

    def get_uid(self):
        return self.uid

    def set_uid(self, new_uid):
        self.uid = new_uid

    def get_username(self):
        return self.u_name

    def set_username(self, new_name):
        self.u_name = new_name

    def get_datetime(self):
        return self.datetime

    def set_datetime(self, value):
        self.datetime = value

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, value):
        self.timestamp = value

    def get_service(self):
        return self.service

    def set_service(self, value):
        self.service = value

    def get_activity(self):
        return self.activity

    def set_activity(self, value):
        self.activity = value

    def get_title(self):
        return self.title

    def set_title(self, value):
        self.title = value

    def get_content(self):
        return self.content

    def set_content(self, value):
        self.content = value

# ---------------------------------------------------------------------------

# 博客服务数据类：Blog, Quora, Reddit


class Blog:
    # 构造函数
    def __init__(self, uid, u_name, datetime, timestamp, service,
                 activity, title, content):
        self.uid = uid
        self.u_name = u_name
        self.datetime = datetime
        self.timestamp = timestamp
        self.service = service
        self.activity = activity
        self.title = title
        self.content = content

    def get_uid(self):
        return self.uid

    def set_uid(self, new_uid):
        self.uid = new_uid

    def get_username(self):
        return self.u_name

    def set_username(self, new_name):
        self.u_name = new_name

    def get_datetime(self):
        return self.datetime

    def set_datetime(self, value):
        self.datetime = value

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, value):
        self.timestamp = value

    def get_service(self):
        return self.service

    def set_service(self, value):
        self.service = value

    def get_activity(self):
        return self.activity

    def set_activity(self, value):
        self.activity = value

    def get_title(self):
        return self.title

    def set_title(self, value):
        self.title = value

    def get_content(self):
        return self.content

    def set_content(self, value):
        self.content = value

# ---------------------------------------------------------------------------

# 开源软件托管服务数据类：Github, Bitbucket, Gitlib


class Git:
    # 构造函数
    def __init__(self, uid, u_name, datetime, timestamp, service,
                 activity, title, content):
        self.uid = uid
        self.u_name = u_name
        self.datetime = datetime
        self.timestamp = timestamp
        self.service = service
        self.activity = activity
        self.title = title
        self.content = content

    def get_uid(self):
        return self.uid

    def set_uid(self, new_uid):
        self.uid = new_uid

    def get_username(self):
        return self.u_name

    def set_username(self, new_name):
        self.u_name = new_name

    def get_datetime(self):
        return self.datetime

    def set_datetime(self, value):
        self.datetime = value

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, value):
        self.timestamp = value

    def get_service(self):
        return self.service

    def set_service(self, value):
        self.service = value

    def get_activity(self):
        return self.activity

    def set_activity(self, value):
        self.activity = value

    def get_title(self):
        return self.title

    def set_title(self, value):
        self.title = value

    def get_content(self):
        return self.content

    def set_content(self, value):
        self.content = value

# ---------------------------------------------------------------------------

# 视频,照片,音乐等多媒体服务数据类：Flickr, Youtube，Last.fm


class Media:
    # 构造函数
    def __init__(self, uid, u_name, datetime, timestamp, service,
                 activity, title, content):
        self.uid = uid
        self.u_name = u_name
        self.datetime = datetime
        self.timestamp = timestamp
        self.service = service
        self.activity = activity
        self.title = title
        self.content = content

    def get_uid(self):
        return self.uid

    def set_uid(self, new_uid):
        self.uid = new_uid

    def get_username(self):
        return self.u_name

    def set_username(self, new_name):
        self.u_name = new_name

    def get_datetime(self):
        return self.datetime

    def set_datetime(self, value):
        self.datetime = value

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, value):
        self.timestamp = value

    def get_service(self):
        return self.service

    def set_service(self, value):
        self.service = value

    def get_activity(self):
        return self.activity

    def set_activity(self, value):
        self.activity = value

    def get_title(self):
        return self.title

    def set_title(self, value):
        self.title = value

    def get_content(self):
        return self.content

    def set_content(self, value):
        self.content = value






