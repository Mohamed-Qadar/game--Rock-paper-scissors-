import random
kmbtr = 0
ciyaare = 0

def qodob_doorasho():
    isticmalaha_dookhiisa= input("dooro midkamid ah  dhagax, warqad or manqas: ")
    if isticmalaha_dookhiisa in ["Dhagax", "dhagax", "d", "D"]:
        isticmalaha_dookhiisa = "d"
    elif isticmalaha_dookhiisa in ["Warqad", "warqad", "w", "W"]:
        isticmalaha_dookhiisa= "w"
    elif isticmalaha_dookhiisa in ["Manqas", "manqas", "m", "M"]:
        isticmalaha_dookhiisa = "m"
    else:
        print("waxa aad galisay ma garanine , iskuday markale.")
        qodob_doorasho()
    return isticmalaha_dookhiisa

def computer_dokhisa():
    doorashad_kumbterka = random.randint(1, 3)
    if doorashad_kumbterka == 1:
        doorashad_kumbterka = "d"
    elif doorashad_kumbterka == 2:
        doorashad_kumbterka = "w"
    else:
        doorashad_kumbterka = "m"
    return doorashad_kumbterka


while True:
    print("")
    
    isticmalaha_dookhiisa= qodob_doorasho()
    doorashad_kumbterka = computer_dokhisa()

    print("")
    
    if isticmalaha_dookhiisa== "d":
        if doorashad_kumbterka == "d":
            print("waxaad doratay dhagax. computerkuna waxa uu doortay dhagax. waxaa noqoteen barbardhac.")
        
        elif doorashad_kumbterka == "w":
            print("waxaad doratay dhagax. computerkuna waxa uu doortay warqada. waadna khasaartay.")
            kmbtr += 1
            
        elif comp_choice == "m":
            print("waxaad doratay dhagax. computerkuna waxa uu doortaymanqas. waadns guuleysatay.")
            ciyaare += 1

    elif isticmalaha_dookhiisa == "w":
        if doorashad_kumbterka == "d":
            print("waxaad doratay warqad. computerkuna waxa uu doortay dhagax. waadna guuleysatay.")
            ciyaare += 1
        
        elif doorashad_kumbterka == "w":
            print("waxaad doratay warqad. computerkuna waxa uu doortay warqada.  waxaa noqoteen barbardhac.")
            
            
        elif doorashad_kumbterka == "m":
            print("waxaad doratay warqad.computerkuna waxa uu doortay manqas. waadna khasaartay.")
            kmbtr += 1

    elif isticmalaha_dookhiisa == "m":
        if doorashad_kumbterka == "d":
            print("waxaad doratay manqas. computerkuna waxa uu doortay dhagax. waadna khasaartay.")
            kmbtr += 1
        
        elif doorashad_kumbterka == "w":
            print("waxaad doratay manqas. computerkuna waxa uu doortay paper.  waadna guuleysatay.")
            ciyaare += 1
            
        elif doorashad_kumbterka == "m":
            print("waxaad doratay manqas. computerkuna waxa uu doortay manqas. waxaa noqoteen barbardhac.")

    print("")
    print("waxaa guuleystay qofka: " + str(ciyaare))
    print("waxaa guuleystay kombuyutarka: " + str(kmbtr))
    print("")
    
    isticmalaha_dookhiisa = input("Do you want to play again? (h/m)")
    if isticmalaha_dookhiisa in ["H", "h", "haa", "Haa"]:
        pass
    elif isticmalaha_dookhiisa in ["M", "m", "maya", "Maya"]:
        break
    else:
        break
