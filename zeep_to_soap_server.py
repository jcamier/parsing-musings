import requests
from bs4 import BeautifulSoup
import zeep

# To find methods/operations:
# in terminal type
# python -mzeep <http_url>

CALC_WSDL = 'http://www.dneonline.com/calculator.asmx?wsdl'
# python -mzeep http://www.dneonline.com/calculator.asmx?wsdl


WSDL = 'http://www.soapclient.com/xml/soapresponder.wsdl'

client = zeep.Client(wsdl=WSDL)
print(client.service.Method1('Zeep', 'is cool'))

calc_client = zeep.Client(wsdl=CALC_WSDL)
addition_test = calc_client.service.Add(1, 2)
print("SOAP Call adding = {}".format(addition_test))




