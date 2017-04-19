"""
个人数据集成模型, User, Stack, FAQ, YL, SNS, Blog, Git, Media,
 Relation, EC 10大数据类
"""

# 用户类


class User:
    # 构造函数
    def __init__(self, uid, u_name, location):
        self.uid = uid
        self.u_name = u_name
        self.location = location
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
    def __init__(self, _id, uid, u_name, datetime, timestamp, service,
                 activity, title, content, keywords):
        self._id = _id
        self.uid = uid
        self.u_name = u_name
        self.datetime = datetime
        self.timestamp = timestamp
        self.service = service
        self.activity = activity
        self.title = title
        self.content = content
        self.keywords = keywords

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

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

    def get_keywords(self):
        return self.keywords

    def set_keywords(self, value):
        self.keywords = value

# ---------------------------------------------------------------------------

# 问答服务数据类


class FAQ:
    # 构造函数
    def __init__(self, _id, uid, u_name, datetime, timestamp, service,
                 activity, title, content, keywords):
        self._id = _id
        self.uid = uid
        self.u_name = u_name
        self.datetime = datetime
        self.timestamp = timestamp
        self.service = service
        self.activity = activity
        self.title = title
        self.content = content
        self.keywords = keywords

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

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

    def get_keywords(self):
        return self.keywords

    def set_keywords(self, value):
        self.keywords = value

# ---------------------------------------------------------------------------

# 问答服务数据类


class YL:
    # 构造函数
    def __init__(self, _id, uid, u_name, datetime, timestamp, service,
                 activity, title, content, keywords):
        self._id = _id
        self.uid = uid
        self.u_name = u_name
        self.datetime = datetime
        self.timestamp = timestamp
        self.service = service
        self.activity = activity
        self.title = title
        self.content = content
        self.keywords = keywords

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

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

    def get_keywords(self):
        return self.keywords

    def set_keywords(self, value):
        self.keywords = value

# ---------------------------------------------------------------------------

# 社交网络服务数据类：Twitter, Google Plus, Facebook


class SNS:
    # 构造函数
    def __init__(self, _id, uid, u_name, datetime, timestamp, service,
                 activity, title, content, keywords):
        self._id = _id
        self.uid = uid
        self.u_name = u_name
        self.datetime = datetime
        self.timestamp = timestamp
        self.service = service
        self.activity = activity
        self.title = title
        self.content = content
        self.keywords = keywords

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

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

    def get_keywords(self):
        return self.keywords

    def set_keywords(self, value):
        self.keywords = value

# ---------------------------------------------------------------------------

# 博客服务数据类：Blog, Quora, Reddit


class Blog:
    # 构造函数
    def __init__(self, _id, uid, u_name, datetime, timestamp, service,
                 activity, title, content, keywords):
        self._id = _id
        self.uid = uid
        self.u_name = u_name
        self.datetime = datetime
        self.timestamp = timestamp
        self.service = service
        self.activity = activity
        self.title = title
        self.content = content
        self.keywords = keywords

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

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

    def get_keywords(self):
        return self.keywords

    def set_keywords(self, value):
        self.keywords = value

# ---------------------------------------------------------------------------

# 开源软件托管服务数据类：Github, Bitbucket, Gitlib


class Git:
    # 构造函数
    def __init__(self, _id, uid, u_name, datetime, timestamp, service,
                 activity, title, content, keywords):
        self._id = _id
        self.uid = uid
        self.u_name = u_name
        self.datetime = datetime
        self.timestamp = timestamp
        self.service = service
        self.activity = activity
        self.title = title
        self.content = content
        self.keywords = keywords

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

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

    def get_keywords(self):
        return self.keywords

    def set_keywords(self, value):
        self.keywords = value

# ---------------------------------------------------------------------------

# 视频,照片,音乐等多媒体服务数据类：Flickr, Youtube，Last.fm


class Media:
    # 构造函数
    def __init__(self, _id, uid, u_name, datetime, timestamp, service,
                 activity, title, content, keywords):
        self._id = _id
        self.uid = uid
        self.u_name = u_name
        self.datetime = datetime
        self.timestamp = timestamp
        self.service = service
        self.activity = activity
        self.title = title
        self.content = content
        self.keywords = keywords

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

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

    def get_keywords(self):
        return self.keywords

    def set_keywords(self, value):
        self.keywords = value

# ---------------------------------------------------------------------------

# 关系类


class Relation:
    # 构造函数
    def __init__(self, pre_id, relation, post_id):
        self.pre_id = pre_id
        self.relation = relation
        self.post_id = post_id

    def get_pre_id(self):
        return self.pre_id

    def set_uid(self, value):
        self.pre_id = value

    def get_relation(self):
        return self.relation

    def set_relation(self, value):
        self.relation = value

    def get_post_id(self):
        return self.post_id

    def set_post_id(self, value):
        self.post_id = value

# ---------------------------------------------------------------------------

# 电商服务数据类：Amazon购买的物品，书籍


class EC:
    # 构造函数
    def __init__(self, _id, uid, u_name, datetime, timestamp, service,
                 activity, title, content, keywords):
        self._id = _id
        self.uid = uid
        self.u_name = u_name
        self.datetime = datetime
        self.timestamp = timestamp
        self.service = service
        self.activity = activity
        self.title = title
        self.content = content
        self.keywords = keywords

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

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

    def get_keywords(self):
        return self.keywords

    def set_keywords(self, value):
        self.keywords = value

# ----------------------------------------------------------------------------------------------------------

"""
switch功能:
"""


class Switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for
            self.fall = True
            return True
        else:
            return False


# The following example is pretty much the exact use-case of a dictionary,
# but is included for its simplicity. Note that you can include statements
# in each suite.

def get_class(value):
    for case in Switch(value):
        if case('User'):
            return User
        if case('Stack'):
            return Stack
        if case('FAQ'):
            return FAQ
        if case('YL'):
            return YL
        if case('SNS'):
            return SNS
        if case('Blog'):
            return Blog
        if case('Git'):
            return Git
        if case('Media'):
            return Media
        if case('Relation'):
            return Relation
        if case('EC'):
            return EC
        if case():  # default, could also just omit condition or 'if True'
            print("something else!")
            return None
        # No need to break here, it'll stop anyway

# ----------------------------------------------------------------------------------------------------------

"""
Relationship Rule规则
"""


def get_relation(pre_class, post_class):

    if pre_class is Media:
        if post_class is SNS:  # (Media, Share to, SNS)
            relationship = "Share to"
            return relationship
        if post_class is Stack:  # (Media, Ask Q, Stack)
            relationship = "Ask Q"
            return relationship
        if post_class is FAQ:
            relationship = "Post"  # (Media, Post, FAQ)
            return relationship
        if post_class is YL:  # (Media, Learn, YL)
            relationship = "Learn"
            return relationship
        if post_class is Blog:  # (Media, Record, Blog)
            relationship = "Record"
            return relationship
        if post_class is Git:  # (Media, VM, Git) VM: Version Management
            relationship = "VM"
            return relationship
        if post_class is Media:  # (Media, Update, Media)
            relationship = "Update"
            return relationship
        if post_class is EC:  # (Media, WB, EC) WB: want to buy
                    #  试听某段音乐，购买正版版权音乐；
                    # 看完某段视频内推荐的某书籍，笔记本电脑，在亚马逊上购买
            relationship = "WB"
            return relationship

    if pre_class is Stack:
        if post_class is Stack:  # (Stack, Update, Stack)
            relationship = "Update"
            return relationship
        if post_class in (FAQ, YL):  # (Stack, Learn, FAQ/YL)
            relationship = "Learn"
            return relationship
        if post_class is SNS:
            relationship = "Share to"  # (Stack, Share to, FAQ)
            return relationship
        if post_class is Blog:  # (Stack, Record, Blog)
            relationship = "Record"
            return relationship
        if post_class is Git:  # (Stack, VM, Git) VM: Version Management
            relationship = "VM"
            return relationship
        if post_class is Media:  # (Stack, Post, Media)
            relationship = "Post"
            return relationship
        if post_class is EC:  # (Stack, Learn, EC)
            relationship = "Learn"
            return relationship

    if pre_class is FAQ:
        if post_class is FAQ:  # (FAQ, Update, FAQ)
            relationship = "Update"
            return relationship
        if post_class in (Stack, YL):  # (FAQ, Learn, Stack/YL)
            relationship = "Learn"
            return relationship
        if post_class is SNS:
            relationship = "Share to"  # (FAQ, Share to, SNS)
            return relationship
        if post_class is Blog:  # (FAQ, Record, Blog)
            relationship = "Record"
            return relationship
        if post_class is Git:  # (FAQ, VM, Git) VM: Version Management
            relationship = "VM"
            return relationship
        if post_class is Media:  # (FAQ, Post, Media)
            relationship = "Post"
            return relationship
        if post_class is EC:  # (FAQ, Learn, EC)
            relationship = "Learn"
            return relationship

    if pre_class is YL:
        if post_class is YL:  # (YL, Update, YL)
            relationship = "Update"
            return relationship
        if post_class in (FAQ, Stack):  # (YL, Learn, FAQ/Stack)
            relationship = "Learn"
            return relationship
        if post_class is SNS:
            relationship = "Share to"  # (YL, Share to, SNS)
            return relationship
        if post_class is Blog:  # (YL, Record, Blog)
            relationship = "Record"
            return relationship
        if post_class is Git:  # (YL, VM, Git) VM: Version Management
            relationship = "VM"
            return relationship
        if post_class is Media:  # (FAQ, Post, Media)
            relationship = "Post"
            return relationship
        if post_class is EC:  # (YL, WB, EC)
            relationship = "WB"
            return relationship

    if pre_class is SNS:
        if post_class is SNS:  # (SNS, Update, SNS)
            relationship = "Update"
            return relationship
        if post_class in (Stack, YL, FAQ):  # (SNS, Ask Q, Stack/YL/FAQ)
            relationship = "Ask Q"
            return relationship
        if post_class is Blog:  # (SNS, Record, Blog)
            relationship = "Record"
            return relationship
        if post_class is Git:  # (SNS, VM, Git) VM: Version Management
            relationship = "VM"
            return relationship
        if post_class is Media:  # (SNS, Post, Media)
            relationship = "Post"
            return relationship
        if post_class is EC:  # (SNS, Like, EC)
            relationship = "Like"
            return relationship

    if pre_class is Blog:
        if post_class is Blog:  # (Blog, Update, SNS)
            relationship = "Update"
            return relationship
        if post_class in (YL, FAQ):  # (Blog, Ask Q, Stack/YL/FAQ)
            relationship = "Ask Q"
            return relationship
        if post_class is Stack:  # (Blog, Learn, Stack/YL/FAQ)
            relationship = "Learn"
            return relationship
        if post_class is SNS:  # (Blog, Share to, SNS)
            relationship = "Record"
            return relationship
        if post_class is Git:  # (Blog, VM, Git) VM: Version Management
            relationship = "VM"
            return relationship
        if post_class is Media:  # (Blog, Post, Media)
            relationship = "Post"
            return relationship
        if post_class is EC:  # (Blog, Learn, EC)
            relationship = "Learn"
            return relationship

    # 2：版本控制服务数据类
    if pre_class is Git:
        if post_class is Git:  # (Git, Update/Pull Request/Merge/Issue, Git)
            relationship = "UPM"
            return relationship
        if post_class in (YL, FAQ):  # (Git, Ask Q, YL/FAQ)
            relationship = "Ask Q"
            return relationship
        if post_class is Stack:  # (Git, Learn, Stack)
            relationship = "Learn"
            return relationship
        if post_class is SNS:  # (Git, Share to, SNS)
            relationship = "Share to"
            return relationship
        if post_class is Blog:  # (Git, Record, Blog)
            relationship = "Record"
            return relationship
        if post_class is Media:  # (Git, Post, Media)
            relationship = "Post"
            return relationship
        if post_class is EC:  # (Git, WB, EC)
            relationship = "WB"
            return relationship

    # 1: 电子商务数据服务类
    if pre_class is EC:
        if post_class is EC:  # (EC, UC, EC)  # 在不同商店购买不同的商品，这些商品的价格和质量不同，choose quality
            relationship = "CQ"
            return relationship
        if post_class in (FAQ, YL):  # (Media, Ask Q, FAQ/YL)
            relationship = "Ask Q"
            return relationship
        if post_class is Stack:  # (Media, Learn, Stack)
            relationship = "Learn"
            return relationship
        if post_class is SNS:  # (Media, Share to, SNS)
            relationship = "Share to"
            return relationship
        if post_class in (Blog, Git):  # (EC, Record, Blog)
            relationship = "Record"
            return relationship
        if post_class is Media:  # (EC, Post, Media)
            relationship = "Post"
            return relationship















