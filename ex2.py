#x=4 y=10
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv') #se importa datele dintr-un excel

#Primul grafic in care se reprezinta Puls, MaxPuls si Calorii in functie de Durata
plt.figure(figsize=(12, 8)) #dimensionarea ferestrei cu grafic
plt.plot(df.index, df['Durata'], label='Durata', marker='*', color = '#4CAF50') #reprezentarea markerelor pe grafic cu o culoare specificata
plt.plot(df.index, df['Puls'], label='Puls', marker='*', color = 'hotpink')#reprezentarea markerelor pe grafic cu o culoare specificata
plt.plot(df.index, df['MaxPuls'], label='MaxPuls', marker='*', color = '#6A3DAC')#reprezentarea markerelor pe grafic cu o culoare specificata
plt.plot(df.index, df['Calorii'], label='Calorii', marker='*', color = 'blue') #reprezentarea markerelor pe grafic cu o culoare specificata
plt.title('Grafic - Puls, MaxPuls, Calorii in functie de Durata') #titlul graficului
plt.xlabel('Durata') #denumire axa x
plt.ylabel('Puls, MaxPuls, Calorii') #denumire axa y
plt.legend() #afisarea legendei 
plt.show()

#Al doilea grafic in care se reprezinta primele X=4 valori pt Puls, MaxPuls si Calorii in functie de durata
plt.figure(figsize=(12, 8))#dimensionarea ferestrei cu grafic
plt.plot(df.index[:4], df['Durata'][:4], label='Durata', marker='*', color = '#4CAF50')#reprezentarea markerelor pe grafic cu o culoare specificata
plt.plot(df.index[:4], df['Puls'][:4], label='Puls', marker='*', color = 'hotpink')#reprezentarea markerelor pe grafic cu o culoare specificata
plt.plot(df.index[:4], df['MaxPuls'][:4], label='MaxPuls', marker='*', color = '#6A3DAC')#reprezentarea markerelor pe grafic cu o culoare specificata
plt.plot(df.index[:4], df['Calorii'][:4], label='Calorii', marker='*', color = '#ffca33')#reprezentarea markerelor pe grafic cu o culoare specificata
plt.title('Grafic - Puls, MaxPuls, Calorii in functie de Durata (primele 4 valori)') #titlul graficului
plt.xlabel('Durata')#denumire axa x
plt.ylabel('Puls, MaxPuls, Calorii')#denumire axa y
plt.legend()#afisarea legendei 
plt.show()

#Al treilea grafic in care se reprezinta ultimele Y=10 valori doar pt Puls si Durata
plt.figure(figsize=(12, 8))#dimensionarea ferestrei cu grafic
plt.plot(df.index[-10:], df['Durata'].tail(10), label='Durata', marker='*', color = '#4CAF50')#reprezentarea markerelor pe grafic cu o culoare specificata
plt.plot(df.index[-10:], df['Puls'].tail(10), label='Puls', marker='*', color = 'hotpink')#reprezentarea markerelor pe grafic cu o culoare specificata
plt.title('Grafic - Puls in functie de Durata (ultimele 10 valori)') #titlul graficului
plt.xlabel('Durata')#denumire axa x
plt.ylabel('Puls')#denumire axa y
plt.legend()#afisarea legendei 
plt.show()
