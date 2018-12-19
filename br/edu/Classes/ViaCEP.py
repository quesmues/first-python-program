#Primeiro exercício em python

#Imports, Librarys
import json
import requests



#Exemplo de como se define uma classe em python
class ViaCEP:

    #Construtor com recebimento de parametro cep
    def __init__(self, c):
        self.c = c

    #Retorno do json completo
    def retorna_json_completo(self):
    	url_api = ('http://www.viacep.com.br/ws/%s/json' % self.c)
    	req = requests.get(url_api)
    	dados_json = json.loads(req.text)
    	return dados_json

    #Retorna UF
    def retorna_uf(self):
    	url_api = ('http://www.viacep.com.br/ws/%s/json' % self.c)
    	req = requests.get(url_api)
    	dados_json = json.loads(req.text)
    	return dados_json['uf']

    def retorna_localidade(self):
        url_api = ('http://www.viacep.com.br/ws/%s/json' % self.c)
        req = requests.get(url_api)
        dados_json = json.loads(req.text)
        return dados_json['localidade']

    def retorna_logradouro(self):
        url_api = ('http://www.viacep.com.br/ws/%s/json' % self.c)
        req = requests.get(url_api)
        dados_json = json.loads(req.text)
        return dados_json['logradouro']

    def retorna_bairro(self):
        url_api = ('http://www.viacep.com.br/ws/%s/json' % self.c)
        req = requests.get(url_api)
        dados_json = json.loads(req.text)
        return dados_json['bairro']                

    


#Teste
# if __name__ == '__main__':
# 	test1 = ViaCEP('78048000')
# 	print(u'%s' % test1.retorna_json_completo())