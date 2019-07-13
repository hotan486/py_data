
########################################################
#  url test
#
########################################################

import urllib as ur
import bs4 as u

html =  ur.request.urlopen("http://naver.com")
dd = u.BeautifulSoup(html,"html.parser")
print(dd.head.title)


########################################################


########################################################
#  함수 사용법
#
########################################################
def sub(x,y):
    return x-y


result = sub(1,2)
print(result)



result = sub(x=1,y=2)

print(result)

def func(data,a=0,b=True,c=''):
    pass

func([1,2,3])   ## 1번째 인자
func([1,2,3], 100)  ## 1번째 인자
func([1,2,3], c='abc')  ## 1번째 인자 + 4번쟤 인자
func([1,2,3], c='abc')  ## 1번째 인자 + 4번쟤 인자 + 2번쨰 인자

########################################################
#  사전 인자를 받은대로 key, value를 인자를 받을 경우 만 가능
#
########################################################

def my_func(**kwargs):
    for key in kwargs:
        print(key, ":", kwargs[key])

my_func(z= 11 , a= 44534, sdkfjhsdf = 4536456)