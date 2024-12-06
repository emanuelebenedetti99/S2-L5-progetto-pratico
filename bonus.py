class Lista:
	def __init__(self):
		self.lista = []

	def aggiungi(self, elemento): #Aggiunge un elemento in fondo alla lista
		self. elemento = elemento
		self.lista.append(self.elemento)
		print(self.elemento, "aggiunto con successo!\n")
		return self.lista

	def visualizza(self): #Stampa la lista in ordine alfabetico
		self.listaOrdinata = sorted(self.lista)
		print("Ecco la tua lista in ordine alfabetico: ", self.listaOrdinata, "\n")
		return self.lista

	def rimuovi(self, elemento):
		self.count = 0 #Conto gli elementi rimossi
		self.elemento = elemento
		for item in self.lista:
			if item.lower() == self.elemento.lower():
				self.lista.remove(item)
				self.count += 1
		print(f"Ho rimosso {self.count} elementi dalla lista\n")
		return self.lista

	def salvaLista(self):  #Crea un file di testo con gli elementi della lista
		self.mioFile = open("lista.txt", "a")
		for elemento in self.lista:
			self.mioFile.write(elemento)
			self.mioFile.write(", ")
		self.mioFile.close()
		print("Lista salvata in lista.txt\n")

class ListaImportata(Lista):
	def __init__(self, lista):
		self.lista = lista


def creaLista():
	print("*** Menu di creazione di una lista ***")
	scelta = input("Vuoi creare una nuova lista? [Si - No] ")
	if (scelta.lower() == "si" or scelta.lower() == "s" or scelta.lower() == "yes" or scelta.lower() == "y"):
		lista = Lista()
		gestisciLista(lista)
	else:
		importa = input("Vuoi importare la lista? ")
		if (importa.lower() == "si" or importa.lower() == "s" or importa.lower() == "yes" or importa.lower() == "y"):
			lista = importaLista()
			lista = ListaImportata(lista)
			gestisciLista(lista)
		else:
			print("Arrivederci!")


def importaLista():
	fileDaImportare = input("inserisci il nome del file da importare: ")
	try:
		with open(fileDaImportare, "r") as mioFile:
			if mioFile.readline() == None:
				print("Il file da importare e' vuoto")
			else:
				lista = mioFile.read().split(", ")
			return lista

	except FileNotFoundError:
		print("File non trovato, riprova con un nuovo file!")


def gestisciLista(lista):
	print("\nVuoi aggiungere un elemento, eliminare un elemento, visualizzare la lista o salvare?")
	azione = input("-Scrivi 'aggiungi' per aggiungere\n-Scrivi 'elimina' per eliminare un elemento\n-Scrivi 'visualizza' per vedere la lista\n-Scrivi 'salva' per salvarla\n>>>")
	if (azione.lower() == "aggiungi" or azione.lower() == "inserisci"):
		elemento = input("Inserisci l'elemento da aggiungere: ")
		lista.aggiungi(elemento)
		gestisciLista(lista)
	elif (azione.lower() == "elimina" or azione.lower == "rimuovi" or azione.lower() == "cancella"):
		elemento = input("Inserisci l'elemento da eliminare: ")
		lista.rimuovi(elemento)
		gestisciLista(lista)
	elif (azione.lower() == "visualizza" or azione.lower() == "vedi" or azione.lower() == "visualiza"):
		lista.visualizza()
		gestisciLista(lista)
	elif (azione.lower() == "salva"):
		lista.salvaLista()
	else:
		print("Non ho capito, prova a ripetere")


creaLista()



