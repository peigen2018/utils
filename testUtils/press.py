# coding=utf-8
import requests
from locust import HttpUser,TaskSet,task,between
from locust.contrib.fasthttp import FastHttpUser
import os
import json

class TestLogin:
    def __init__(self) -> None:
        print("")

class Test(FastHttpUser):
    wait_time = between(0, 0)

    @task
    def test(self):
     
        res = self.client.get("/")
        if res.status_code != 200:
            print(res.text)


  

    def on_start(self):
        print("start")
       #self.client.post("/login", {"username":"user", "password":"pwd"})


if __name__ == "__main__":
    os.system("locust -f hello.py --host=http://www.upload.com")

 