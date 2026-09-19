def controlla_password(password):  
    punteggio = 0                  
    ha_un_numero = False
    ha_maiuscola = False
    ha_simbolo = False 
    ha_minuscola = False

    for character in password:
        if character.isupper():       
            ha_maiuscola = True
        if character.islower():
            ha_minuscola =True
        if character.isdigit():
            ha_un_numero =True
        if  not character.isalnum():
            ha_simbolo =True  
    
    if ha_maiuscola:       
        punteggio += 1                  
    if ha_un_numero:
        punteggio += 1
    if ha_minuscola:
        punteggio += 1
    if ha_simbolo:
        punteggio += 1
    if len(password) >= 8:
        punteggio += 1
    if len(password) >= 12:
        punteggio += 1
    print(f"Punteggio: {punteggio}/6")
   
    if punteggio <=2:
       print("Password inserita: DEBOLE")
    elif punteggio <=4:
       print("Password inserita: MEDIA")
    else:
       print("Password inserita: FORTE")
    
    print("Suggerimenti: ")
    if len(password) <8:
       print("Usa almeno 8 caratteri")
    if not ha_maiuscola:
       print("Usa almeno una maiuscola")
    if not ha_un_numero:
       print("Usa almeno un numero")
    if not ha_simbolo:
       print("Usa almeno un simbolo")
    if not ha_minuscola:
       print("Usa almeno una minuscola")



password_utente= input("Inserisci password da controllare: ")
controlla_password(password_utente)
       
        
        
   
