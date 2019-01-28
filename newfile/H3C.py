import logging
import telnetlib
import time

"""
python自动化运维之Telnetlib https://www.cnblogs.com/lsdb/p/9258964.html
H3C 巡检命令 http://blog.51cto.com/coolner/1391470
"""

class TelnetClient():
    """
    telnet类 初始化 登陆函数 执行命令 退出
    """
    def __init__(self,):
        self.tn = telnetlib.Telnet() # 别名
 
    def login_host(self,host,username,password,Superuser,Superpassword):
        """
        实现telnet登录主机函数
        """
        try:
            """ 初次登陆 """
            # self.tn = telnetlib.Telnet(host,port=23)
            self.tn.open(host,port=23)
        except:
            # logging.warning('%s网络连接失败'%host)
            print('%s网络连接失败'%host)

            return False
        # 等待login出现后输入用户名，最多等待10秒 H3C 直接输入密码
        # self.tn.read_until(b'login: ',timeout=10)
        # self.tn.write(username.encode('ascii') + b'\n')
        self.tn.read_until(b'Password: ',timeout=10) # 监听字符
        self.tn.write(password.encode('ascii') + b'\n')
        # 延时两秒再收取返回结果
        time.sleep(2)

        try:
            """ 二次登陆 """
            self.tn.write(Superuser.encode('ascii') + b'\n')
            self.tn.read_until(b'Password: ',timeout=10)
            self.tn.write(Superpassword.encode('ascii') + b'\n')
            time.sleep(2)
            # 延时两秒再收取返回结果，给服务端足够响应时间
        except Exception as identifier:
            return identifier

        # 获取登录结果
        # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode('ascii')
        if 'Login incorrect' not in command_result:
            # logging.warning('%s登录成功'%host)
            print('%s登陆成功'%host)
            return True
        else:
            # logging.warning('%s登录失败，用户名或密码错误'%host)
            print('%s登陆失败'%host)
            return False


    def execute_some_command(self,commands):
        """ 此函数实现执行传过来的命令，并输出其执行结果 """
        # 执行命令
        self.tn.write(command.encode('ascii')+b'\n')
        time.sleep(10)
        # 获取命令结果
        command_result = self.tn.read_very_eager().decode('ascii')
        print(command_result)
        # logging.warning('命令执行结果：\n%s' % command_result)

    def logout_host(self):
        """ 退出telnet """
        self.tn.write(b"exit\n")

if __name__ == '__main__':
    """ 参数初始化 """
    Hosts = ['10.135.100.1', '10.135.100.2']
    username = 'xxx'
    password = 'xxx'
    Superuser = 'su'
    Superpassword = 'xxxx'

    # commands  = ['system', 'dis time all', 'dis clock', 'display ntp-service status','dis cpu-usage', 'dis users']
    commands  = ['dis time all', 'dis clock', 'display ntp-service status','dis cpu-usage'] # 用户视图下能执行的命令


    telnet_client = TelnetClient()
    # 如果登录结果返加True，则执行命令，然后退出
    for host in Hosts: # 迭代主机
        if telnet_client.login_host(host,username,password,Superuser,Superpassword):
            for command in commands: # 迭代执行命令集
                telnet_client.execute_some_command(command)

    telnet_client.logout_host() #退出
