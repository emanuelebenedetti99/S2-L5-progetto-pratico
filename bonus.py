class Lista:
    def __init__(self):
        self.lista = []

    def aggiungi(self, elemento):  # Aggiunge un elemento in fondo alla lista
        if isinstance(elemento, list):  # Se l'elemento è una lista, aggiungiamo tutti gli elementi
            self.lista.extend(elemento)  # Usa extend per aggiungere tutti gli elementi della lista
            print(f"Elementi {elemento} aggiunti con successo!\n")
        else:
            self.lista.append(elemento)  # Aggiunge un singolo elemento
            print(f"{elemento} aggiunto con successo!\n")
        return self.lista

    def visualizza(self):  # Stampa la lista in ordine alfabetico
        listaOrdinata = sorted(self.lista)  # Dispongo la lista in ordine alfabetico
        print("Ecco la tua lista in ordine alfabetico: ", listaOrdinata, "\n")
        return listaOrdinata

    def rimuovi(self, elemento):  # Rimuove un elemento dalla lista
        count = 0  # Conto gli elementi rimossi
        for item in self.lista[:]:  # Itero su una copia della lista
            if item.lower() == elemento.lower():
                self.lista.remove(item)
                count += 1  # Aumento il contatore se ho trovato un elemento da eliminare
        print(f"Ho rimosso {count} elemento/i dalla lista\n")  # Stampo il numero di eliminazioni
        return self.lista

    def salvaLista(self):  # Se non esiste crea un file di testo con gli elementi della lista chiamato lista.txt
        with open("lista.txt", "w") as mioFile:  # Apro il file in modalità "w" per sovrascrivere
            for elemento in self.lista:  # Scrivo nel file tutti gli elementi della lista
                mioFile.write(elemento + "\n")  # Aggiungo ogni elemento su una nuova riga
        print("Lista salvata in lista.txt\n")


class ListaImportata(Lista):  # Eredita dalla classe genitore tutti i metodi, ma permette di importare una lista
    def __init__(self, lista):
        super().__init__()
        self.lista = lista


def creaLista():  # Scegli se creare o importare una lista
    print("*** Menu di creazione di una lista ***")
    scelta = input("Vuoi creare una nuova lista? [Si - No] ")
    if scelta.lower() in ["si", "s", "yes", "y"]:
        lista = Lista()  # Crea l'oggetto lista
        gestisciLista(lista)  # Chiama la funzione per gestire l'oggetto creato
    else:
        importa = input("Vuoi importare la lista? ")
        if importa.lower() in ["si", "s", "yes", "y"]:
            lista = importaLista()  # Salva la lista importata dalla funzione importaLista()
            lista = ListaImportata(lista)  # Crea l'oggetto listaImportata con la lista importata
            gestisciLista(lista)  # Chiama la funzione per gestire l'oggetto listaImportata
        else:
            print("Arrivederci!")


def importaLista():  # Importa una lista da un file
    fileDaImportare = input("Inserisci il nome del file da importare: ")
    try:
        with open(fileDaImportare, "r") as mioFile:
            contenuto = mioFile.read().strip()  # Leggi tutto il contenuto e rimuovi gli spazi superflui
            if contenuto:
                lista = contenuto.splitlines()  # Crea una lista separando per le nuove righe
            else:
                lista = []  # Se il file è vuoto, restituisci una lista vuota
            return lista
    except FileNotFoundError:  # Se il file non esiste gestisco l'errore chiedendo di riprovare
        print("File non trovato, riprova con un nuovo file!")
        return importaLista()  # Richiedi un nuovo nome del file


def gestisciLista(lista):  # Gestisco l'oggetto lista (importato o creato)
    print("\nVuoi aggiungere un elemento, eliminare un elemento, visualizzare la lista o salvare?")
    azione = input("-Scrivi 'aggiungi' per aggiungere\n-Scrivi 'elimina' per eliminare un elemento\n-Scrivi 'visualizza' per vedere la lista\n-Scrivi 'salva' per salvarla\n-Scrivi 'esci' per uscire\n>>> ")
    
    if azione.lower() in ["aggiungi", "inserisci"]:
        tipo_aggiunta = input("Vuoi aggiungere uno o più elementi? [1 - uno, 2 - più] ")
        if tipo_aggiunta == "1":
            elemento = input("Inserisci l'elemento da aggiungere: ")
            lista.aggiungi(elemento)
        elif tipo_aggiunta == "2":
            elementi = input("Inserisci gli elementi da aggiungere, separati da virgola: ")
            lista.aggiungi([elem.strip() for elem in elementi.split(",")])  # Aggiungi la lista di elementi
        else:
            print("Opzione non valida!")
        gestisciLista(lista)
    elif azione.lower() in ["elimina", "rimuovi", "cancella"]:
        elemento = input("Inserisci l'elemento da eliminare: ")
        lista.rimuovi(elemento)
        gestisciLista(lista)
    elif azione.lower() in ["visualizza", "vedi", "visualiza"]:
        lista.visualizza()
        gestisciLista(lista)
    elif azione.lower() == "salva":
        lista.salvaLista()
        gestisciLista(lista)
    elif azione.lower() in ["esci", "stop"]:
        print("Arrivederci!")
        return
    else:
        print("Non ho capito")
        scelta = input("Vuoi uscire dal programma? ")
        if scelta.lower() in ["si", "s", "yes", "y"]:
            print("Arrivederci!")
            return
        else:
            gestisciLista(lista)


# Avvio del programma
creaLista()
