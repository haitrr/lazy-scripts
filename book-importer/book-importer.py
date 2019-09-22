import bs4
import requests

userName = "***"
password = "*****"
rootUrl = 'https://www.biquge.com.cn'
begin = "/book/30594/715187.html"
num = 100
current = 0

login = requests.post("http://lwtapi.hai2cs.com/api/user/login",
                      json={"username": userName, "password": password})
if login.status_code != 200:
    print("Failed to login")
    exit(0)
print("Login success")
token = login.json()["token"]
link = rootUrl+begin
while current < num:
    response = requests.get(link)
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
    result = requests.post('http://lwtapi.hai2cs.com/api/text', json={
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
