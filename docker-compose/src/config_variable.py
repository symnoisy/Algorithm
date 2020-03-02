'''
config 변수 선언
'''
import logging

logger = logging.getLogger("info")
logger.setLevel(logging.INFO)
stream_hander2 = logging.StreamHandler()
logger.addHandler(stream_hander2)

#swagger
bind_addr = '0.0.0.0'
bind_port = '7777'


