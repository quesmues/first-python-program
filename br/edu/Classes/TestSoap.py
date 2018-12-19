import zeep
import sys, os
import requests



###############################################################################################################################################
###############################################################################################################################################
#Exemplo de um client SOAP simples


def main():
	#Cria uma string com a url da wsdl
	wsdl = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'
	#Define o transport para não verificar o certificado ssl
	session = requests.Session()
	session.verify = False
	transport = zeep.Transport(session=session)
	#Cria um objeto Client
	client = zeep.Client(wsdl=wsdl, transport=transport)
	print(client.service.consultaCEP('99070220'))



if __name__ == '__main__':
	main()