#Primeiro exercício em python

#Imports, Librarys
import sys
import os
import time
import datetime
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) #insert to syspath a parent directory for import
from Classes import *
from Classes.Cep import Cep


#############################################################################
#MAIN
def main():
	x=''
	wait=0
	print('---------------Iniciando Programa---------------')
	#########################################################################
	#Espera de 5 segundos
	while wait <= 1:
		time.sleep(1)
		wait = wait+1
	criarArquivos()
	print('[DONE]')
	time.sleep(1)
	os.system('cls')
	while x!='exit':
		x=''
		nlinha = 0
		m = 0
		opcao = ''
		cepcontrol = ''

		##################################MENU###############################
		#CHAMADA FUNCAO MENU
		m = menu(m)

		#####################################################################
		#OPÇOES

		if m == 1:
			x = calculadora(x)

		#MENU SAIR
		if m == 10:
			x = 'exit'
			
#############################################################################
###################CONTINUAÇÂO DOS MENUS, CHAMADA EXTERNA####################
#############################################################################

		#################CPF#########################
		#Implementar apenas numeros
		#Finalizado Não

		if m == 2:
			c1 = 0
			c1 = cpf.opcao3(c1)
			print ('Seu cpf é: '+c1)
			input('\nAperte enter para continuar')
			os.system('cls')

		###################CEP#######################
		#Finalizado 23/06/2017 22:16
		#API ViaCEP

		if m == 3:
			os.system('cls')

			while cepcontrol!='exit':
				cep1 = input('Insira o seu CEP: ')
				cep2 = Cep(cep1)
				cepcontrol=''
				if len(cep1) == 8:
					print(cep2.retorna_endereco())
					cepcontrol='exit'	
				else:
					os.system('cls')
					print('Cep Inválido')
					log = open('../Logs/log.txt', 'r+')
					if log.readlines() != '':
						log.write('\n'+str(datetime.datetime.now())+' Cep Inválido: '+cep1)
					else:
						log.write(str(datetime.datetime.now())+' Cep Inválido: '+cep1)
					log.close()
					time.sleep(1)
					os.system('cls')

			input('Aperte enter para continuar')
			os.system('cls')


#############################################################################
#############################################################################
#############################################################################

		#SAIR
		if x == 'exit':
			print('Saindo....')
			print('------------------------------------------------')
			sys.exit()
#############################################################################
###################################FUNCOES###################################
#############################################################################
#FUNÇÃO LOGS
def logs():
	#########################################################################
	#Criar arquivo log e criar log se já existe	
	try:
		log = open('../Logs/log.txt', 'x+')
	except FileExistsError:
		log = open('../Logs/log.txt', 'r+')
		if log.readlines() != '':
			log.write('\n'+str(datetime.datetime.now())+' Arquivo logs.txt já existe')
		else:
			log.write(str(datetime.datetime.now())+' Arquivo logs.txt já existe')
		log.close()

#############################################################################
#CALCULADORA
def calculadora(x):	
	try:
		n1 = input ('Insira um numero: ')
		n2 = input ('Insira outro numero: ')
		n3 = int(n1) * int(n2)
		print('Resultado: ',n3,'\n')
		resultado = str(n3)
		text = 'Resultado: '+resultado
		filetxt = open('resultado.txt', 'r+')
		if filetxt.readlines() != '':
			filetxt.write('\n'+text)
		else:
			filetxt.write(text)
		filetxt.close()	
	except ValueError:
		print('Valores inválidos\n')	
		log = open('../Logs/log.txt', 'r+')
		if log.readlines() != '':
			log.write('\n'+str(datetime.datetime.now())+' Valores inválidos')
		else:
			log.write(str(datetime.datetime.now())+' Valores inválidos')
		log.close()
	x = str(input('Insira exit para sair ou menu para continuar\n'))
	os.system('cls')
	return (x)


def criarArquivos():
	##########################################################################
	#Criar diretório e criar log se já existe		
	try:	
		os.mkdir('Logs')
		logs()
		log = open('../Logs/log.txt', 'r+')
		log.close()	
	except FileExistsError:
		logs()
		log = open('../Logs/log.txt', 'r+')
		if log.readlines() != '':
			log.write('\n'+str(datetime.datetime.now())+' Diretório Logs já existe')
		else:
			log.write(str(datetime.datetime.now())+' Diretório Logs já existe')	
		log.close()	
	##########################################################################
	#Criar arquivo resultado.txt e criar log se já existe
	try:
		filetxt = open('resultado.txt', 'x+')
		filetxt.close()	
	except FileExistsError:
		filetxt = open('resultado.txt', 'r+')
		log = open('../Logs/log.txt', 'r+')
		if log.readlines() != '':
			log.write('\n'+str(datetime.datetime.now())+' Arquivo resultado.txt já existe')
		else:
			log.write(str(datetime.datetime.now())+' Arquivo resultado.txt já existe')	
		log.close()	
		filetxt.close()	


def menu(m):
	##########################################################################
	#MENU
	print('Escolha uma opção a seguir')
	print('1 - Multiplicação')
	print('2 - CPF')
	print('3 - CEP -> Edereço')
	print('10 - Sair')
	try:
		try:
			opcao = input('- Opção: ')
		except EOFError:
			log = open('../Logs/log.txt', 'r+')
			if log.readlines() != '':
				log.write('\n'+str(datetime.datetime.now())+' EOF Error, input is empty')
			else:
				log.write(str(datetime.datetime.now())+' EOF Error, input is empty')
			log.close()
			opcao = ''	
		m = int(opcao)
	except ValueError:
		log = open('../Logs/log.txt', 'r+')
		if log.readlines() != '':
			log.write('\n'+str(datetime.datetime.now())+' invalid literal for int() with base 10: '+opcao)
		else:
			log.write(str(datetime.datetime.now())+' invalid literal for int() with base 10: '+opcao)		
		log.close()	
	os.system('cls')
	return (m)
	##########################################################################


##############################################################################
#################################INICIO PROGRAMA##############################
##############################################################################		
#CHAMADA FUNÇÃO MAIN
if __name__ == '__main__':
	os.system('cls')
	main()	
