import multiprocessing

def esegui_file(file):
    # Inserisci qui il codice per eseguire il file
    print(f'Eseguendo il file: {file}')

if __name__ == "__main__":
    # Lista dei file che vuoi avviare
    files_da_avviare = ["SFile.py", "SFile.py", "SFile.py"]

    # Crea un processo per ogni file
    processi = []
    for file in files_da_avviare:
        processo = multiprocessing.Process(target=esegui_file, args=(file,))
        processi.append(processo)

    # Avvia tutti i processi
    for processo in processi:
        processo.start()

    # Attendi che tutti i processi terminino
    for processo in processi:
        processo.join()

    print("Tutti i processi sono terminati.")
