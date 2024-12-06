import datetime

def assistente_virtuale(comando):

	if comando == "Qual è la data di oggi?":

		oggi = datetime.date.today()

		risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")

	elif comando == "Che ore sono?":

		ora_attuale = datetime.datetime.now()

		risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")

	elif comando == "Come ti chiami?":

		risposta = "Mi chiamo Assistente Virtuale"

	elif comando == "Arrivederci":

		risposta = "Arrivederci!"

	else:

		risposta = "Non ho capito la tua domanda."

	return risposta

#Ho inserito una funzione print per spiegare all'utente le funzionalita' e i comandi
print("""*** Benvenuto nell'assistente virtuale semplice. Sono in grado di fornirti la data di oggi, l'orario e di presentarmi! ***\n
Inserisci: 1 se vuoi conoscere la data di oggi - 2 se vuoi sapere l'ora - 3 se vuoi sapere il mio nome - 4 per uscire\n""")

start = True #valore inmpostato a True avvia il ciclo while che viene terminato in caso di match case 4

while start == True:

	try:
		comando_utente = int(input("Cosa vuoi sapere? >>> ")) #Converto in intero l'input ricevuto

		match comando_utente: #Implementazione Python di uno switch-case, confronto con l'input castato
			case 1:
				comando_utente = "Qual è la data di oggi?"
			case 2:
				comando_utente = "Che ore sono?"
			case 3:
				comando_utente = "Come ti chiami?"
			case 4:
				comando_utente = "Arrivederci"
				start = False #Termino l'esecuzione del programma

		print(assistente_virtuale(comando_utente))

	except ValueError: #Se l'utente non inseerisce un numero, il cast in intero fallisce e controllo l'errore chiedendo un nuovo numero
		print("Inserisci un numero!")


















