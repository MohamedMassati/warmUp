file = "contacts.txt"


def charger_contacts():
    
    contacts = []
    
    try:
        with open(file, "r", encoding="utf-8") as f:
            
            for line in f:
                try:
                    name, tel, email = line.strip().split(";")

                    contact = {
                        "name": name, 
                        "tel": tel, 
                        "email": email
                    }

                    contacts.append(contact)
                    
                except ValueError:
                    print(f"Ligne ignorée : {line.strip()}")                  


    except FileNotFoundError:
        print("Le fichier de contacts n'existe pas. Un nouveau fichier sera créé.")

    return contacts


def sauvegarder_contacts(contacts):

    try:
        with open(file, "w", encoding="utf-8") as f:
            for c in contacts:
                f.write(f"{c['name']} ; {c['tel']} ; {c['email']}\n")
                
    except OSError as e:
        print(f"Erreur de sauvegarde : {e}")

def ajouter_contact(contacts):

    print("\n--- Ajouter un nouveau contact ---")

    name = input("Donner le nom: ").strip()
    tel = input("Donner le numéro de téléphone: ").strip()
    email = input("Donner l'adresse email: ").strip()

    if not name or not tel or not email:
        print("Tous les champs sont obligatoires.")
        return

    contact = {
        "name": name, 
        "tel": tel, 
        "email": email
    }

    contacts.append(contact)
    sauvegarder_contacts(contacts)
    print(
        f"Contact ajouté: {contact['name']}, {contact['tel']}, {contact['email']} avec succès !"
    )


def afficher_contacts(contacts):

    print("\n--- Liste des contacts ---")

    if not contacts:
        print("Aucun contact trouvé.")
        return
    
    for i, c in enumerate(contacts, start=1):
        print(f"Le contact {i}: {c['name']}, {c['tel']}, {c['email']}")


def supprimer_contact(contacts):

    print("\n--- Supprimer un contact ---")

    if not contacts:
        print("Aucun contact à supprimer.")
        return

    afficher_contacts(contacts)

    try:

        num = int(input("donner le numero du contact a supprimer: "))

        if 1 <= num <= len(contacts):
            contact = contacts.pop(num - 1)
            sauvegarder_contacts(contacts)
            print(f"Le contact: {contact['name']}  a été supprimé avec succes !\n")
            
        else:
            print("Numéro de contact invalide.")
            
    except ValueError:
        print("Veuillez entrer un numéro valide.")


def menu():
    
    contacts = charger_contacts()
    
    while True:
        print("\n--- Menu ---")
        print("1. Ajouter un contact")
        print("2. Afficher les contacts")
        print("3. Supprimer un contact")
        print("4. Quitter")

        choix = input("Choisissez une option: ")

        if choix == "1":
            ajouter_contact(contacts)
        elif choix == "2":
            afficher_contacts(contacts)
        elif choix == "3":
            supprimer_contact(contacts)
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez entrer 1, 2, 3 ou 4.")

if __name__ == "__main__":
    menu()