nome = input('Digite o nome de sua cidade: ')

variavel_splited = nome.split(" ")

variavel_casa = variavel_splited[0]

variavel_achar = variavel_casa.find('Santo') 
 
print(variavel_achar)



# correção

#cid = str(input('Digite o nome de sua cidade')).strip()   <eliminando espaços indesejados 
#print(cid[:5].upper() == 'SANTO')  < aqui faz retornar verdadeiro ou falso, foi colocado o upper caso saia alguma letra com maiusculo e minusculo e assim n ira confundir o codigo 
#