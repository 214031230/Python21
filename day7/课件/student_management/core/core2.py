from core import manager
from config import settings
def login():
    print('执行login')

def main():
    login()
    manager.Manager('alex')
    print(settings.userinfo_path)
