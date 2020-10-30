from urllib.parse import urlencode, quote_plus
from urllib.request import Request, urlopen

url = 'http://apis.data.go.kr/B553734/iseelectricprod/getElectricProduction'
'''queryParams = '?' + urlencode({ quote_plus('serviceKey') : 'ys8iBd7f3EkNukbdy3G5zDTVv8E45MzWWaZyvZX0I1%2BjqZwtbBeY90I%2BXyOsgnl0tzStPeO695EtHBba6qJ47g%3D%3D',             
                                quote_plus('returnType') : 'xml/json', 
                                quote_plus('numOfRows') : '10', 
                                quote_plus('pageNo') : '1', 
                                },encoding='UTF-8')
'''
key = 'serviceKey=ys8iBd7f3EkNukbdy3G5zDTVv8E45MzWWaZyvZX0I1%2BjqZwtbBeY90I%2BXyOsgnl0tzStPeO695EtHBba6qJ47g%3D%3D'
returnType='&returnType=xml/json'
numOfRow='&numOfRows=10'
pageNo='&pageNo=1'
queryParams = '?' + key + returnType + numOfRow + pageNo
request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print (response_body)