c) README

Pasi pentru refacerea aplicatiei:
 1. Instalare Python: Asigurati-va ca aveti Python instalat (versiunea 3.8 sau mai recenta).
 2. Instalare Pygame: Rulati "pip install pygame" pentru a instala biblioteca pygame.
 3. Instalare module suplimentare: Asigurati-va ca aveti instalate modulele "socket", "_thread", si "pickle".
 4. Instalare IDE: Pentru realizarea acestui joc am folosit PyCharm, versiunea 2024.1

Pasi pentru rularea aplicatiei:
 1. Rularea serverului: Lansati serverul cu python "server.py". Veti vedea un mesaj care indica faptul ca serverul este pornit si asteapta conexiuni.
 2. Rularea clientului: Lansati clientul cu python "client.py". Acest lucru va deschide interfata grafica si se va conecta la server.
 3. Rularea clientului urmator: Faceti un duplicat al configurarii clientului original, "client.py", din setarile PyCharm, pe care il lansati pentru a avea cel de al doilea jucator.
 4. Jucarea jocului: Dupa ce ambii jucatori s-au conectat, fiecare va alege o optiune (piatra, hartia sau foarfeca) si rezultatul va fi afisat. Jocul se va reseta dupa fiecare runda.
 5. Iesire din joc: La inchidearea unui singur client, celalalt va ramane conectat in retea si va astepta pana cand alt oponent se va conecta. Pentru inchiderea jocului este necesara deconectarea celor 2 clienti si oprirea serverului.

Versiuni software utilizate:
 1. Python: Versiunea 3.8 sau mai recenta.
 2. Pygame: Versiunea 2.0 sau mai recenta.
 3. PyCharm: Versiunea 2024.1 sau mai recenta.