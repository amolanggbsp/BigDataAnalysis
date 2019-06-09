from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import re   
import time
import numpy as np

import csv

#네이버에 검색할 키워드 input
target = input("Enter a keyword : ")

#크롤링 페이지 수 설정 
maxPages = input("Enter amount of pages to see : ")

#np.savetxt("naver blog crawling.csv", np.column_stack((maintitle, contents)), delimiter=",", fmt='%s', header=header)

#정규식 컴파일
hyperlink = re.compile(r'.*href="(.*)" target.*')

# Main Title
"""(example) <span class="title" ng-bind-html="post.title">MLB X <strong class="search_keyword">TWICE</strong> 고화질 포토월 화보 추가 공개</span>"""
maintitle = re.compile(r'ng-bind-html="post.title">(.*)</span>.*')

#author찾기 
authorRE = re.compile(r'<em class="name_author">(.*)</em>.*')
#np = re.compile(r'</span>(.*?)</a>', re.DOTALL)

intro = re.compile(r'.*<p>(.*)</p>.*', re.DOTALL)

"""authorRE = re.compile(r'</div>(.*?)</a>.*', re.DOTALL)"""

#<a ng-href="http://blog.naver.com/mychocofie/221235127857" class="text" ng-bind-html="post.contents" ng-if="post.contents" target="_blank" bg-nclick="srs*l.text" href="http://blog.naver.com/mychocofie/221235127857"><strong class="search_keyword">Twice</strong> Bunk Bed 트와이스 2층침대 ( light-gray) 3월의 끝자락. 요몇일 이어지는 비소식에 봄을 알리는 소리가 여기 파주까지 왔음을... 시작합니다 &lt; <strong class="search_keyword">Twice</strong> 2층침대 &gt; - light gray 품명 : 트와이스 2층침대 규격 : SS 수종 : 소나무 색상 : lihgt - gray &lt; <strong class="search_keyword">Twice</strong> 2층침대 &gt; - light gray 앞서 소개해드린... </a>
#contentsRE=re.compile(r'"post.contents"(.*)</a>.*')
contentsRE=re.compile(r'ng-if="post.contents" target="_blank">(.*)</a>.*')

#C:\Users\ATIV\Downloads\chromedriver_win32 #c:\python36\lib\site-packages

#Selenium 구동
driver=webdriver.Chrome("C:/Users/ATIV/Downloads/chromedriver_win32/chromedriver")
driver.set_window_size(1120,800)

#driver.get("https://section.blog.naver.com/Search/Post.nhn?pageNo=1&rangeType=ALL&orderBy=sim&keyword="+target)


time.sleep(2)



isFinished = False
row = 1

with open('GS.csv', 'w', encoding='UTF-8', newline='') as f:
    # Define the writer
    writer = csv.writer(f)
    writer.writerow( ['Field1', 'Field2', 'Field3','Field4', 'Field5'] )
    
    #while not isFinished:
    for page in range( int(maxPages) ):

    #actual page 링크에서 페이지 가져오기 
        actualPage = str(page + 1)
        print ("VIEWING PAGE N "+actualPage)
        driver.get("https://section.blog.naver.com/Search/Post.nhn?pageNo="+actualPage+"&rangeType=ALL&orderBy=sim&keyword="+target)
        #쿼리 빈도 제한
        time.sleep(3)

        #BeautifulSoup 객체 생성 div'태그의 내용 파싱
        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        #우선 전체 클라스 "list_search_post" 안의 내용을 find_all로 찾는다 
        link = soup.find_all("div", {"class":"list_search_post"})
        for posts in link:

            #쿼리 빈도 제한
            time.sleep(0.33)
            
            z = str(posts)
            url = hyperlink.search(z).group(1).strip()
            mtitle = maintitle.search(z).group(1).strip()

            #검색 키워드가 bold 처리되어 있어서 해당 부분 이외 내용 문자열 조합
            if '<strong class="search_keyword">' in mtitle:
                #
                m = re.search(r'(.*)<strong class="search_keyword">(.*)</strong>(.*)', mtitle)
                mtitle = m.group(1) + m.group(2) + m.group(3)

           

            introURL = urllib.request.urlopen(url) 
            soupURL = BeautifulSoup(introURL, "html.parser") # bs 객체 생성
            linkURL = soupURL.find_all("span", {"class":"title"}) # 블로그 제목 

            try:
                dsc = intro.search(str(linkURL)).group(1).strip() # 정규식으로 잘라내기
            except:
                dsc = ""

            """
            miscURL = soupURL.find_all("span", {"em class":"name_author"}) # 블로그 본문
            misc = str(miscURL)
            author=authorRE.search(z).group(1).strip()
            """
            #author은 r'<em class="name_author">(.*)</em>.*' 에서 바로 사이에 있는 데이터 추출 가능 
            author=authorRE.search(z).group(1).strip()
            #contents=contentsRE.search(z).group(1).strip()

            """if '<strong class="search_keyword">' in contents:
                c=re.search(r'(.*)<strong class="search_keyword">(.*)</strong>(.*)<strong class="search_keyword">(.*)</strong>(.*)',contents)
                contents=c.group(1)+c.group(2)+c.group(3)+c.group(4)+c.group(5)
               """ 
            """
            if '<em class="name_author">' in misc:
                a=re.search(r'<em class="name_author">(.*)</em>.*',author)
                author=a.group(1) 
            """         
            information = [mtitle, author]

            print(mtitle)
            #print(author)
            #print(contents)
            writer.writerows( [information] )

   
