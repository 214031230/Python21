# from threading import Thread
# import time
# def foo():
#     while True:
#         print(123)
#         time.sleep(1)
#
# def bar():
#     print(456)
#     time.sleep(3)
#     print("end456")
#
# t1 = Thread(target=foo)
# t2 = Thread(target=bar)
#
# t1.daemon = True
# t1.start()
# t2.start()
# print("main-------")


# 主线程结束了之后守护线程也同时结束
# 守护线程会等待主线程完全结束之后才结束


from threading import RLock

lock = RLock()
lock.acquire()
lock.acquire()
print(123)
lock.release()
print(456)
lock.release()


# 普通的锁 在同一个线程中 只能acquire一次
# 所以当acquire两次的时候就容易出现死锁现象
# 出现了死锁现象可以使用递归锁去解决问题
# 但是本质上死锁的出现是因为逻辑的错误
# 因此我们更应该把注意力集中在解决逻辑错误
# 而不要在出现错误的时候直接用递归锁规避















