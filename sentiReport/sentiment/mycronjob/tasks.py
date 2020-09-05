import datetime
from sentiment.myCelery import app
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from sentimentWork.sentimentSpider.sentimentSpider.spiders.sentiSpider import SentispiderSpider
from .connectDb import ConnDb
import pandas as pd
from snownlp import SnowNLP

# 封装成任务
@app.task()
def task1():
    return 'test1'

@app.task()
def task2():
    return 'test2'

@app.task()
def crawlTask():
    return crawl_run()

def crawl_run():
    print('开始爬取............')
    scope = 'all'
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(SentispiderSpider, scope)
    process.start()
    process.join()
    print('爬取结束............')

@app.task()
def clean_up_data():
    # 清洗并处理情感结果存入清洗表
    print('开始清洗............')
    currentDate = datetime.datetime.now().strftime('%Y-%m-%d')
    conn = ConnDb()
    result = conn.getRecentCommentData(currentDate)
    if result is not None and len(result) != 0:
        # 清洗数据
        df = pd.DataFrame(list(result))
        df.dropna()
        df.drop_duplicates()
        data_list = df.values.tolist()
        # 保存到清洗表
        for item in data_list:
            elem = {}
            # [544, '24500449', 'yj124', '原价谁会买，这价都贵了', '2020-09-03 23:32:39', '2020-09-04 09:32:39']
            elem['productCode'] = item[1]
            elem['user_name'] = item[2]
            elem['content'] = item[3]
            elem['comment_time'] = item[4]
            # 情绪分析
            s = SnowNLP(item[2])
            # snowNLP形式 >= 0.5 积极 
            if s.sentiments >= 0.5:
                elem['sentiment'] = '1'
            else:
                elem['sentiment'] = '0'
            elem['crt_time'] = item[5]
            # 保存清洗表
            ret = conn.checkClnSameComments(elem['user_name'], elem['content'])
            if ret is None or ret == '':
                conn.saveCleanComments(elem)
    print('清洗结束............')