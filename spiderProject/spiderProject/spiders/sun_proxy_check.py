import requests
from lxml import etree
from queue import Queue
import threading
import time

class climbvideo():
    def __init__(self):
        self.data = [
            "http://168.119.137.56:3128",
            "http://102.129.249.120:3128",
            "http://46.223.255.8:8080",
            "http://178.62.56.172:80",
            "http://84.91.22.240:80",
            "http://14.97.2.104:80",
        ]
        self.headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
        }
        self.threads = [] #创建一个线程池
        self.threads_nums = 100 #设置10个线程
        self.start_time = time.time() #开始时间
        self.result = []


    #1、给队列添加值
    def queue_ssignment(self):

        self.link_queue = Queue()  # 创建队列对象
        for item in self.data:
            self.link_queue.put(item)  # 添加到队列

        # 打印队列中的值 - 查看有啥内容
        # while not self.link_queue.empty():
        #     print(self.link_queue.get())
        # print(self.link_queue.qsize())
        self.setThreads()

    # 2、线程控制
    def setThreads(self):
        for i in range(self.threads_nums):
            t = threading.Thread(target=self.business_module)  # 创建一个线程
            t.start()  # 启动线程
            self.threads.append(t)  # 添加到线程池

        # 阻塞队列,直到队列被清空才会继续往下执行
        self.link_queue.join()
        # 向队列发送N个None,通知线程退出
        for i in range(self.threads_nums):
            self.link_queue.put(None)
        # 阻塞主线程,直到退出主线程
        for t in self.threads:
            t.join()
        cost_seconds = time.time() - self.start_time
        print('处理完成,用时 %.2f 秒' % cost_seconds)
        #print(self.link_queue.qsize()) #打印队列是否都消费完

    #3、队列中元素移除
    def business_module(self):
        while True:
            link = self.link_queue.get()  # 阻塞,直到从队列中取得一条消息,说明:这里获取不到数据,不会往下执行,阻塞形式
            #print("A %s Z" % link)
            if link is None:  # 如果取到的数据是None,则退出循环,线程即可也消失
                break
            self.sun_proxy(link)  # 把从消息队列中获取的值,传给爬虫函数,执行操作
            #print(link)
            self.link_queue.task_done()  # 执行到这里,告诉队列,本次循环执行完了,它会从队列里面删掉一条数据
            #print('队列中剩余 %d 条数据' % self.link_queue.qsize())

    #4、业务逻辑模块
    def sun_proxy(self,level2_url):

        try:
            r2 = requests.get(level2_url, headers=self.headers, timeout=1)
            print(r2.status_code)
            if r2.status_code == 200:
                self.result.append(level2_url)
        except Exception as result:
            # print(result)
            pass


if __name__=='__main__':
    sun = climbvideo()
    sun.queue_ssignment()
    print('一下是可用代理')
    for item in sun.result:
        print(item)
