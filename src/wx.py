import itchat
import time
import datetime


def timer_handle(exec_time):
    flag = 0
    while True:
        now = datetime.datetime.now()
        if now > exec_time and now < exec_time + datetime.timedelta(seconds = 1):
            send_to()
            time.sleep(1)
            flag = 1
        else:
            if flag == 1:
                exec_time + datetime.timedelta(hours=1)
                flag = 0


def send_to():
    # 找到想发给的好友
    users = itchat.search_friends(name="忘")
    print(users)
    # 获取UserName,用于发送消息
    userName = users[0]['UserName']
    itchat.send("起床了", toUserName=userName)   # toUserName留空则表示发送给自己
    # itchat.send("@fil@%s" % './file/test.text', toUserName=userName)   # 发送文件
    # itchat.send("@img@%s" % './img/0.jpg', toUserName=userName)    # 发送图片
    # itchat.send("@vid@%s" % '/video/test.mp4', toUserName=userName)    # 发送视频
    print('发送成功！')

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)    # 弹出二维码扫描登录（保持登录状态）
    exec_time = datetime.datetime(2017, 11, 19, 22, 50, 10)
    print('任务将执行于 {0}'.format(exec_time))
    timer_handle(exec_time)
