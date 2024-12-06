
class Lista:
	def __init__(self):
		self.lista = []

	def aggiungi(self, elemento): #Aggiunge un elemento in fondo alla lista
		self. elemento = elemento
		self.lista.append(self.elemento) #aggiungo l'elemento
		print(self.elemento, "aggiunto con successo!\n")
		return self.lista

	def visualizza(self): #Stampa la lista in ordine alfabetico
		self.listaOrdinata = sorted(self.lista) #Dispongo la lista in ordine alfabetico
		print("Ecco la tua lista in ordine alfabetico: ", self.listaOrdinata, "\n")
		return self.lista

	def rimuovi(self, elemento): #rimuove un elemento dalla lista
		self.count = 0 #Conto gli elementi rimossi
		self.elemento = elemento
		for item in self.lista: #Con il ciclo for se ci sono piu' elementi da eliminare li elimino tutti
			if item.lower() == self.elemento.lower():
				self.lista.remove(item)
				self.count += 1 #Aumento il contatore se ho trovato un elemento da eliminare
		print(f"Ho rimosso {self.count} elementi dalla lista\n") #Stampo il nummero di eliminazioni
		return self.lista

	def salvaLista(self):  #Se non esiste crea un file di testo con gli elementi della lista chiamato lista.txt
		self.mioFile = open("lista.txt", "a") #Apro il file in modalita' append, per non sovrascrivere
		for elemento in self.lista: #Scrivo nel file tutti gli elementi della lista
			self.mioFile.write(elemento)
			self.mioFile.write(", ") #Aggiungo la virgola per separare gli elementi
		self.mioFile.close() #Chiudo il file
		print("Lista salvata in lista.txt\n")

class ListaImportata(Lista): #Eredita dalla classe genitore tutti i metodi, ma permette di importare una lista
	def __init__(self, lista):
		self.lista = lista


def creaLista(): #SCeglie se creare o importare una lista
	print("*** Menu di creazione di una lista ***") #Stampa all'utente il menu'
	scelta = input("Vuoi creare una nuova lista? [Si - No] ")
	if (scelta.lower() == "si" or scelta.lower() == "s" or scelta.lower() == "yes" or scelta.lower() == "y"):
		lista = Lista() #Crea l'ogetto lista
		gestisciLista(lista) #Chiama la funzione per gestire l'oggetto creato
	else:
		importa = input("Vuoi importare la lista? ")
		if (importa.lower() == "si" or importa.lower() == "s" or importa.lower() == "yes" or importa.lower() == "y"):
			lista = importaLista() #Salva la lista importata dalla funzione importaLista()
			lista = ListaImportata(lista) #Crea l'oggetto listaImportata con la lista importata
			gestisciLista(lista) #Chiama la funzione per gestire l'oggetto listaImportata
		else:
			print("Arrivederci!")


def importaLista(): #Importa una lista da un file
	fileDaImportare = input("inserisci il nome del file da importare: ")
	try:
		with open(fileDaImportare, "r") as mioFile:
			if mioFile.readline() == None: #Verifico se il file e' vuoto
				print("Il file da importare e' vuoto")
			else:
				lista = mioFile.read().split(", ") #Creo la lista utilizzando il metodo split
			return lista

	except FileNotFoundError: #Se il file non esiste gestisco l'errore chiedendo di riprovare
		print("File non trovato, riprova con un nuovo file!")


def gestisciLista(lista): #Gestisco l'oggetto lista (importato o creato)
	print("\nVuoi aggiungere un elemento, eliminare un elemento, visualizzare la lista o salvare?") #Chiede all'utente quale funzionalita' (metodo della classe) vuole utilizzare
	azione = input("-Scrivi 'aggiungi' per aggiungere\n-Scrivi 'elimina' per eliminare un elemento\n-Scrivi 'visualizza' per vedere la lista\n-Scrivi 'salva' per salvarla\n>>>")
	if (azione.lower() == "aggiungi" or azione.lower() == "inserisci"): #Confronto l'input con varie possibilita' di inserimento
		elemento = input("Inserisci l'elemento da aggiungere: ") #Prendo l'elemento come input
		lista.aggiungi(elemento) #Aggiungo l'elemento con il meetodo aggiungi
		gestisciLista(lista)
	elif (azione.lower() == "elimina" or azione.lower == "rimuovi" or azione.lower() == "cancella"):
		elemento = input("Inserisci l'elemento da eliminare: ")
		lista.rimuovi(elemento) #Rimuovo tutti gli elementi con il nome passato in input dall'utente
		gestisciLista(lista)
	elif (azione.lower() == "visualizza" or azione.lower() == "vedi" or azione.lower() == "visualiza"):
		lista.visualizza() #Stampo la lista tramite il metodo visualizza
		gestisciLista(lista)
	elif (azione.lower() == "salva"):
		lista.salvaLista() #Salva lista su file
	else:
		print("Non ho capito, prova a ripetere") #Nel caso in cui l'utente sbagli a scrivere
		gestisciLista


#Avvio il programma creando la lista o importandola chiamndo la funzione crealista
creaLista()



