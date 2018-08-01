import configparser

# conf = configparser.ConfigParser()
# conf["DEFAULT"] = {'ServerAliveInterval': '45',
#                       'Compression': 'yes',
#                      'CompressionLevel': '9',
#                      'ForwardX11':'yes'
#                      }
#
# conf['bitbucket.org'] = {'User':'hg'}
# conf['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}
# with open('example.ini', 'w') as f:
#    conf.write(f)

import configparser

config = configparser.ConfigParser()
print(config.sections())
config.read('example.ini')
print(config.sections())        #   ['bitbucket.org', 'topsecret.server.com']  # DEFAULT --> 全局

# print('bytebong.com' in conf) # False
# print('bitbucket.org' in conf) # True
# print(conf['bitbucket.org']["user"])  # hg
# print(conf['DEFAULT']['Compression']) #yes
# print(conf['topsecret.server.com']['ForwardX11'])  #no
# print(conf['bitbucket.org'])          #<Section: bitbucket.org> 生成器
# for key in conf['bitbucket.org']:     # 注意,有default会默认default的键
#     print(key)
# print(conf.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键
# print(conf.items('bitbucket.org'))    #找到'bitbucket.org'下所有键值对
# print(conf.get('bitbucket.org','compression')) # yes       get方法Section下的key对应的value

import configparser
# conf = configparser.ConfigParser()
# conf.read('example.ini')
# conf.add_section('yuan')
# conf.remove_section('bitbucket.org')
# conf.remove_option('topsecret.server.com',"forwardx11")
# conf.set('topsecret.server.com','k1','11111')
# conf.set('yuan','k2','22222')
#
# conf.write(open('example.ini', "w"))