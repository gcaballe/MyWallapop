TODO LIST

1. Afegir dropdown menú on top right corner with "userpanel" options:
	- register
	- sign in
	- go to user panel (localhost:8080/playground/'userpanel':)
	- log out

2. Crear una pàgina http:localhost:8080/playground/'register'
	- Amb un formulari amb tots els camps
	- fer el insert user al clickar al botó
	- redirect main page
	
3. Crear una pàgina http:localhost:8080/playground/'login'
	- Formulari amb username i password
	- botó de login que miri si el user + password es correcte, i si ho és, guardi l'username en session
	
4. Crear log out (poc prioritari)

---

Tot això dins de localhost:8080/playground/'userpanel':

5. Formulari de perfil per "update" user.
	(Poder canviar description, city, avatar image)

6. Una vista mestre - detall de productes
	- Llista de tots els productes de usuari, i al costat un formulari de producte individual.
	- Un botó de "modificar" o "Crear" un usuari nou
	- Cuan fas click a un producte de la llista, es carrega la info a la "fitxa individual"
	i el text del botó es canvia per "modificar"
	- S'ha de crear el controlador que faci el INSERT o UPDATE del producte
	- Afegir el botó de eliminar producte, que està disabled si no es selecciona cap producte


---
Tema comentaris:

7. Afegir nº de comentaris en una fitxa de producte (la que es veu en una vista galeria).

8. Afegir tota una template "comments_of_product.html" per enganxar-la a sota del "single_product.html"
passant-li com a parametre { "comments" : Comment[] }

9. Afegir el formulari d'afegir comment a product. Que t'apareixi només si estàs logged (if session is set)

---

main page és una gallery de TOTS els products. Es pot reutilitzar el codi per posar-ho dins de la pàgina
localhost:8080/playground/author/id_author.
Aquesta pàgina hauria de ser, el perfil del author, seguit de la gallery de TOTS els seus productes.