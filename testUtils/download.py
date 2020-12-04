import requests
import time

def downloadFile(name, url):
    headers = {'Proxy-Connection':'keep-alive'}
    r = requests.get(url, stream=True, headers=headers)
    print(r.headers)

    f = open(name, 'wb')
    count = 0
    count_tmp = 0
    time1 = time.time()
    for chunk in r.iter_content(chunk_size = 1):
        if chunk:
            f.write(chunk)
            count += len(chunk)
            now = time.time()
            deff= now - time1
            
            if deff > 2:
                speed = (count - count_tmp)  / 1024 /1024/  2
                count_tmp = count
                print(name + ': '  + '%' + ' Speed: ' + formatFloat(speed) )
                time1 = now
    f.close()
    
def formatFloat(num):
    return '{:.3f}'.format(num)
    
if __name__ == '__main__':
    downloadFile('t.txt', 'http://www.upload.com/down/error.txt')