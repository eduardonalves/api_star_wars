# api_star_wars
A uma API Star Wars com Django e Mongo DB

Requisitos:

<ul>
<li>Python 3 </li>
<li>Django 2</li>
<li>Django Rest Framework</li> 
<li>Requests</li> 
<li>Djongo</li> 
<li>Mongo DB</li> 

</ul>

Instalação:

<ul>
	<li>Configurar a variável DATABASES dentro arquivo settings.py Mongo DB</li>
	<li>Rodar o comando python manage.py migrate </li>
	<li>Rodar o comando python manage.py runserver para subir o servidor</li>
</ul>

Acesso:
<ul>
	<li>http://127.0.0.1:8000/planets/</li>
</ul>

Exemplo de pesquisa de planeta por nome:
<ul>
	<li>http://127.0.0.1:8000/planets/?name=Alderaan</li>
</ul>




