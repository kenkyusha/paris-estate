import pandas as pd
import sys
import pdb

#FLAG = True
#while FLAG:
try:
	df = pd.read_csv(sys.argv[1], sep=";")
except:
	print('input path to csv file')

# DISPLAY ALL STREETS
print('SELECT COLUMN')
#print('DF :')
print(df.columns)

# fil = str(input('Enter a column: '))

fil = 'adresse_nom_voie'
print(df[fil].unique())

while 1:
	street = str(input('Enter street: '))
	print('Current street building numbers: ')

	print(df[df[fil] == street]['adresse_numero'].unique().tolist())
	number = int(input('Enter number: '))
	
	for x in df[(df[fil] == street) & (df['adresse_numero'] ==  number)].index:
		cur = df.iloc[x]
		val = cur['valeur_fonciere']
		dat = cur['date_mutation']
		size = cur['surface_reelle_bati']
		print(f'Date: {dat} Cur flat: {x},  price: {val}, size: {size}, ruut: {val/size}')
pdb.set_trace()
