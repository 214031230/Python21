#!/usr/bin/env python3
# 函数式简单配置
import logging
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

# 默认情况下Python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，
# 这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG），默认的日志格式为日志级别：Logger名称：用户输出消息。

# 灵活配置日志级别，日志格式，输出位置:
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./test.log',
                    filemode='w')

logging.debug('debug message')        # 非常细节的日志 —— 排查错误的时候使用
logging.info('info message')          # 正常的日志信息
logging.warning('warning message')    # 警告
logging.error('error message')        # 错误
logging.critical('critical message')  # 严重错误

# 参数
"""
logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有：

filename：用指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中。
filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
format：指定handler使用的日志显示格式。
datefmt：指定日期时间格式。
level：设置rootlogger（后边会讲解具体概念）的日志级别
stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件(f=open(‘test.log’,’w’))，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。

format参数中可能用到的格式化串：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
"""


# logger对象配置
import logging

logger = logging.getLogger()    # 实例化一个logger对象

fh = logging.FileHandler('test1.log', encoding='utf-8')  # 创建一个文件handler，用于写入日志文件
ch = logging.StreamHandler()   # 再创建一个终端handler，用于输出到控制台

formatter_File = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 定义文件日志格式
formatter_Stream = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 定义终端日志格式

logger.setLevel(logging.DEBUG)  # 定义文件日志级别
logger.setLevel(logging.DEBUG)  # 定义终端日志级别

fh.setFormatter(formatter_File)      # 设置文件日志格式
ch.setFormatter(formatter_Stream)    # 设置终端日志格式

logger.addHandler(fh)  # logger对象可以添加多个fh和ch对象
logger.addHandler(ch)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

# logging库提供了多个组件：Logger、Handler、Filter、Formatter。Logger对象提供应用程序可直接使用的接口，
# Handler发送日志到适当的目的地，Filter提供了过滤日志信息的方法，Formatter指定日志显示格式。另外，可以通过：logger.setLevel(logging.Debug)设置级别,当然，也可以通过
#
# fh.setLevel(logging.Debug)单对文件流设置某个级别。


def my_logger(log_file):
    """
    定义日志输出合格
    :return: 返回一个可以直接使用的logger对象
    """
    import logging
    logger = logging.getLogger()    # 实例化一个logger对象
    fh = logging.FileHandler(log_file, encoding='utf-8')  # 创建一个文件handler，用于写入日志文件
    ch = logging.StreamHandler()                          # 创建一个终端handler，用于输出到控制台
    formatter = logging.Formatter('%(asctime)s  %(name)s   %(levelname)s  %(message)s File:<%(filename)s line %(lineno)d>')  # 定义文件日志格式
    logger.setLevel(logging.DEBUG)  # 定义文件日志级别
    fh.setFormatter(formatter)      # 设置文件日志格式
    ch.setFormatter(formatter)      # 设置终端日志格式
    logger.addHandler(fh)           # logger对象fh对象
    logger.addHandler(ch)           # logger对象ch对象
    return logger


log = my_logger("./test1.log")
log.debug('logger debug message')
log.info('logger info message')
log.warning('logger warning message')
log.error('logger error message')
log.critical('logger critical message')
