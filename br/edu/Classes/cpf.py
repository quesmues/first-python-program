#CHAMAR CPF WebService e Retornar String com Endereço

#Imports, Librarys
import sys
import os
import time
import datetime

def opcao3(c1):
	c1 = ''
	while len(c1) != 11:
		try:
			c1 = input('Digite o seu cpf, apenas numeros: ')
			
		except EOFError:  
			log = open('../Logs/log.txt', 'r+')
			if log.readlines() != '':
				log.write('\n'+str(datetime.datetime.now())+' error: '+c1)
			else:
				log.write(str(datetime.datetime.now())+' error: '+c1)		
			log.close()
			c1=''		
	os.system('cls')

	cpfmask = c1[0]+c1[1]+c1[2]+'.'+c1[3]+c1[4]+c1[5]+'.'+c1[6]+c1[7]+c1[8]+'-'+c1[9]+c1[10]

	return(cpfmask)

	# else:
	# 	print('Não é um CPF válido')
	# 	log = open('../Logs/log.txt', 'r+')
	# 	if log.readlines() != '':
	# 		log.write('\n'+str(datetime.datetime.now())+' Não é um CPF válido')
	# 	else:
	# 		log.write(str(datetime.datetime.now())+' Não é um CPF válido')		
	# 	log.close()	

# def func1(c):
# 	c = 40
# 	return(c)




		


