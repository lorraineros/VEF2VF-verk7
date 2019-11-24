{% extends "index.html" %}

{% block content %}
    <div class="center_text">
        <h2>{{ user['email'] }}</h2>
        <h3>Username: {{ user['name'] }}</h3>
        <h3>Password: <button class="secret">{{ user['password'] }}</button></h3>
        <a href="/" class="button">Til baka</a> <a href="/utskraning" class="button">Útskráning</a>
    </div>
{% endblock %}