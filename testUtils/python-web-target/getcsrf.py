# coding=UTF-8
import re
import sys
import datetime

if __name__ == '__main__':
    
   data = '<html><body>隐藏了csrf的页面<input type="hidden" name="csrf" value="csrfsecr"/></body></html>'
   regex = '.*?<input.*?name="csrf".*?value="(.*?)".*?>'
   print(re.match(regex,data,re.DOTALL).groups())

   now=datetime.datetime.now()
   now_date = now.strftime("%Y-%m-%d")
   now_time = (now +datetime.timedelta(seconds=1)).strftime("%H:%M:%S")
   msg_dict = {
      "date":now_date,
      "time":now_time ,
      "user_name":"LIUJING27",
      "terminal":"DESKTOP-89I06CK", 
      "tcode":"SE16N", 
      "program":"SAPLSMTR_NAVIGATION"}

   print(msg_dict)


