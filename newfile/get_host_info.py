# getmac 
"""
python实现获取电脑IP、主机名、Mac地址
# filename get_host_info.py
使用 pyinstaller -F get_host_info.py 编译
"""
import socket
import uuid #内置uuid模块
"""
uuid1：MAC和时间戳算法
uuid2：分布式计算环境DCE算法（python内没有）
uuid3：名字空间和MD5散列值算法
uuid4：随机数算法
uuid5：名字空间的SHA-1散列值算法
"""
hostname = socket.gethostname().upper()
# IP
ip = socket.gethostbyname(hostname)
# MAC
def get_mac_address():
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
    return "-".join((mac[e:e+2] for e in range(0,11,2)))
print("计算机名:", hostname, end='\n')
print("IP  地址:", ip, end='\n')
print("MAC 地址:", get_mac_address(), end='\n')
input('press Enter key to Exit')