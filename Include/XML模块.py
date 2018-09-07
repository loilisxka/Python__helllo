# -*- coding: utf-8 -*-
from xml.parsers.expat import ParserCreate
from urllib import request
class WeatherSaxHandler(object):
    forecastDic = {}
    arry = list()
    def start_element(self,name,attrs):
        if name == 'yweather:location':
            self.forecastDic['city'] = attrs['city']
        elif name == 'yweather:forecast':
            itemInfo = {}
            for key,v in attrs.items():
                itemInfo[key] = v
            self.arry.append(itemInfo)
    def end_element(self,name):
        if name == 'channel':
            self.forecastDic['forecast'] = self.arry
def parseXml(xml_str):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.Parse(xml_str)
    return handler.forecastDic
#测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
with request.urlopen(URL,timeout=4)as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
print('ok')