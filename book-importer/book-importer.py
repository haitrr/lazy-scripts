import bs4
import requests
import time

userName = "***"
password = "*****"
rootUrl = 'https://www.biquge.com.cn'
begin = "/book/30594/974624.html"
num = 40
current = 0
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

login = requests.post("https://lwt-api.haitran.dev/api/user/login",
                      json={"username": userName, "password": password})
if login.status_code != 200:
    print("Failed to login")
    exit(0)
print("Login success")
token = login.json()["token"]
link = rootUrl+begin
while current < num:
    for i in range(10):
        try:
            print("try to fetch page: time {count}".format(count=i + 1))
            response = requests.get(link, headers=headers, timeout=3)
            print("fetch page success")
            break
        except:
            print("failed to fetch page, wait for 5 seconds")
            time.sleep(5)
    if(response.status_code != 200):
        print("Can not get book")
        print(link)
        exit(0)
    soup = bs4.BeautifulSoup(response.content, 'lxml')
    for br in soup.find_all("br"):
        br.replace_with("\n")
    title = soup.select(".bookname>h1")[0].getText()
    print("Importing "+title)
    content = soup.select("#content")[0].getText()
    result = requests.post('https://lwt-api.haitran.dev/api/text', json={
        "title": title,
        "content": content,
        "language": 2
    }, headers={"Authorization": "Bearer "+token})
    if(result.status_code != 200):
        print("Fail")
        exit(0)

    print("Success")

    nextLink = soup.select(".bottem2>a")[2]["href"]
    link = rootUrl+nextLink
    current += 1

print("Imported " + str(num) + " book!")
print("Next link "+link)
