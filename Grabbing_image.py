import requests
import bs4

resource = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(resource.text, "lxml")
# print(soup.select("img")[10])
print(soup.select(".mw-file-element"))

computer = soup.select(".mw-file-element")[4]
print(computer)
print(computer["src"])
image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/One_of_Deep_Blue%27s_processors_%282586060990%29.jpg/220px-One_of_Deep_Blue%27s_processors_%282586060990%29.jpg")
print(image_link)
image_link.content
f = open("image1.jpg", "wb")
f.write(image_link.content)
f.close()