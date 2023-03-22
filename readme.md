

#Autors

Guillem Caballé Tomàs i Marc Fernández Parra

Git

To t el projecte està al git personal del Guillem Caballé:

<https://github.com/gcaballe/MyWallapop>

Engegar el projecte

Per engegar el projecte, des de la carpeta arrel:

pipenv shell

python manage.py runserver

entrar a <http://localhost:8000/playground/main_page/>

Per poder veure les dades del SQLite:

http://localhost:8000/admin





Observacions:

Vem començar el projecte a base d’un tutorial de Django, i ens vem enterar massa tard, que

estavem treballant en un sub-projecte amb nom “playground”, dins de l'aplicació

MyWallapop.

Hem tingut algun problemilla amb les URL’s de recursos estàtics com imatges, quan

intentavem refactoritzar el codi i ordenar-lo bé, així que al final t’hem entregat la versió amb

el projecte dins del projecte.

Si no ho feiem així, alguna imatges no s’ens mostraven.

Des de la main page et pots registrart / loguejar.

Registrat o no, pots veure la galeria total, la pàgina d’un usuari, i la pàgina d’un producte

(detall).

Si estàs loguejat, pots anar (pel mateix drop-down menú) a la userpanel page.

Aquí pots editar les dades d’usuari a l’esquerra.





I a la dreta, tens una llista (en negre, al centre) amb tots els productes d’aquest usuari.

Si fas click en cualsevol row de la llista et surt una vista detall d’aquest producte.

En la vista detall, es pot editar o esborrar (OJO! no demana confirmació).

I també es pot crear un producte nou.

Base de dades

Hem treballat amb el SQLite que ja ofereix django. Ho hem preferit així, que llavors et

podem passar el projecte tal cual, i ja tindras les dades de mostra que hem creat, per poder

veure l’aplicació correctament.

Per a qualsevol dubte, quedem a disposició teva per correu !

