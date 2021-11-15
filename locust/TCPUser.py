import time
import socket
import json
from locust import User, TaskSet, events, task, between

token = 100


class TcpSocketClient(socket.socket):

    def __init__(self, af_inet, socket_type):
        super(TcpSocketClient, self).__init__(af_inet, socket_type)

    def connect(self, addr):
        start_time = time.time()
        try:
            super(TcpSocketClient, self).connect(addr)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(
                request_type="tcpsocket", name="connect", response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type="tcpsocket", name="connect", response_time=total_time,
                                        response_length=0)

    def send(self, msg):
        start_time = time.time()
        try:
            super(TcpSocketClient, self).send(msg)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(
                request_type="tcpsocket", name="send", response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type="tcpsocket", name="send", response_time=total_time,
                                        response_length=0)

    def recv(self, bufsize):
        recv_data = ''
        start_time = time.time()
        try:
            recv_data = super(TcpSocketClient, self).recv(bufsize)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(
                request_type="tcpsocket", name="recv", response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type="tcpsocket", name="recv", response_time=total_time,
                                        response_length=0)
        return recv_data


class TcpSocketUser(User):
    abstract = True
    port = None
    """
    This is the abstract Locust class which should be subclassed. It provides an TCP socket client
    that can be used to make TCP socket requests that will be tracked in Locust's statistics.
    author: Max.bai@2017
    """

    def __init__(self, *args, **kwargs):
        super(TcpSocketUser, self).__init__(*args, **kwargs)
        self.client = TcpSocketClient(socket.AF_INET, socket.SOCK_STREAM)
        ADDR = (self.host, self.port)
        self.client.connect(ADDR)


def user_send_msg():
    send_json = {
        "access_token": "101",
        "sess_id": 101
    }
#    send_json['access_token'] = str(random.randint(100,5000))
    global token
    if (token > 10000):
        token = 100
    else:
        token += 1
    send_json['access_token'] = str(token)
    send_str = json.dumps(send_json)

    value = (len(send_str)).to_bytes(4, byteorder='big')+send_str.encode()
    lenght = (len(value)+4).to_bytes(4, byteorder='big')
    tag = b'\x12\x00\x00\x02'
    byte_str = tag + lenght + value + b'\x00\x00\x00\x00'
    return byte_str


def user_recv_msg(data):
    pass


class user_set(TaskSet):
    @task
    def send_data(self):
        print("send data")
        # byte_str = user_send_msg()

        # # send msg
        # self.client.send(byte_str)
        # data = self.client.recv(2048)
        # user_recv_msg(data)

    @task
    def recv_data(self):
        print("start sleep")
        time.sleep(5)
        # data = self.client.recv(2048)
        # user_recv_msg(data)

    def on_start(self):

        print("on start")
        pass

    def on_stop(self):
        print("on stop")
        pass


class TcpTestUser(TcpSocketUser):
    host = "192.168.31.252"  # host
    port = 80  # port
    # between the execution of tasks (min_wait and max_wait) as well as other user behaviours
    wait_time = between(3, 3)
    tasks = [user_set]
