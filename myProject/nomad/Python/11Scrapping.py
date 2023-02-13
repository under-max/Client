from requests import get
from bs4 import BeautifulSoup
#get 은 웹사이트를 복사해오는 방식
base_url = "https://weworkremotely.com/remote-jobs/search?&term="
search_thrm = "python"
response = get(f"{base_url}{search_thrm}")
#print(response.status_code) #status code 확인

if response.status_code != 200:
    print("Can't request website")
else: 
    results = []
   # print(response.text, "html.parser") #reponse로 하면 숫자값 text로 하면 구성하고 있는 코드를 확인 할 수 있음 
    soup = BeautifulSoup(response.text, "html.parser") #text를 soup쪽에 넘겨줌 전체 페이지라는 의미로 html.parser
    #print(soup.find_all("title")) #html문서의 title 찾기 
    jobs =soup.find_all('section', class_='jobs') #section tag의 class부분 확인
    #class_="jobs" arguement의 이름을 넣어주면 arguement 의 순서를 상관없게 해줌 원래는 순서대로 들어가야 함 
    #_붙여준 이유는 class 라는건 python에서 이미 이용중이기 때문에 class_가 됨 
    for job_section in jobs:
        job_posts = job_section.find_all("li") #job_posts = list의 li들, 리스트가 됨
        job_posts.pop(-1) #제일 마지막의 view all 제거
        for post in job_posts:
            anchors = post.find_all('a') #post 안에서 'a'tag 검색
            anchor = anchors[1] #beatifulsoup는 딕셔너리 처럼 바꿔줌4
            link = anchor['href']
            company, kind, region = anchor.find_all('span', class_="company") #리스트가 됨
            title = anchor.find('span', class_='title') #find 는 결과를 가져옴 find all 은 리스트를 가져옴 
            #print(company.string, kind.string, region.string, title.string)
            job_data = {
                'link' : f"https://weworkremotely.com/{link}", #.string 쓰면 tag지워줌 
                "company" : company.string,
                "resign" : region.string,
                'position' : title.string
            }
            results.append(job_data)

for result in results:
    print(result)

#list_of_number 

            