import funções as fc

chave = '4d237ac186c4d4348ee029706edec059'

lista_da_localização = fc.localizar('RJ', chave)  # Formato (('Cidade', 'País', latitude, longitude))

latitude = lista_da_localização[2]
longitude = lista_da_localização[3]

clima_atual_bruto = fc.clima(chave, latitude, longitude)

weather = clima_atual_bruto['weather']


print(weather)

print(clima_atual_bruto)
