# PR

# **Laboratorul 1. Programarea în rețea. Socket | HTTP | Multithreading**

1. Să se creeze o cerere(request) GET HTTP către web-serverul website-ului me.utm.md utilizînd
socket.
2. Cu ajutorul expresiilor regulate să se extragă toate imaginile din raspunsul primit din punctul 1.
3. Utilizînd Socket, HTTP și firele de execuții să se descarce toate imaginile găsite din puncul 2 într-un
folder. Imaginile să se descarce utilizînd maximum 4 fire de execuție concomitent.

## **Pentru nota 9 si 10:**
* utilizînd 4 fire de execuție nu mai mult de 2 imagini să fie salvate în folder în același timp
* programul elaborat trebuie să funcționeze și pentru utm.md

## **Atenție:**
* Să nu utilizați librării HTTP, pentru acest laborator utilizați sintaxa protocolului HTTP.
* Fiecare cerere(request) GET HTTP să conțină minim 6 antete.
* Pentru punctul 2 alegeți doar JPG, PNG și GIF.
* în rețea totul este la nivel de octeți așa ca înainte de a scrie în socket asigurați-vă că datele sunt
convertite în octeți.
* Pentru utm.md utilizați portul 443, pentru me.utm.md portul 80.
* Puteți utiliza semaforul pentru a sincroniza firele de execuție

# **Laboratorul 2. Programarea în rețea. SMTP | POP3 | IMAP**

Să se creeze un program client de poștă electronică(MUA – Mail User Agent) apt să trimită și să 
citească mesajele prin intermediul unui cont de poștă electronică.

## **Pentru nota 9 si 10:**

* să se poată atașa și fișiere în mesaj ce nu depășesc 2MB, cele care depășesc să fie respinse
* să se creeze un GUI(Graphical User Interface) pentru clientul de poștă electronică

## **Atenție:**

* Pentru acest laborator utilizați librării deja existente pentru SMTP, POP3 sau IMAP, nu este 
necesar de a utiliza socket. Cine dorește poate să facă prin socket ca și la primul laborator.
* Pentru contul poștei electronice puteți alege Yandex, Gmail, Yahoo Mail, Outlook, GMX etc.
* Pentru a transmite mesajele utilizați SMTP, pentru a extrage și citi mesajele utilizați POP3 sau 
IMAP, la dorință.
