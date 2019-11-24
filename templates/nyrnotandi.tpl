{% extends "index.html" %}

{% block content %}
   <div class="container center_text">
      <form action="" method="post">
         <p><input type="text" name="name" maxlength="32" placeholder="Notendanafn" required></p>
         <p><input type="text" name="email" maxlength="32" placeholder="email" required></p>
         <p><input type="text" name="password" maxlength="32" minlength="4" placeholder="Lykilorð" required></p>
         <p><input type="submit" value="Create User"></p>
      </form>
      {% if error == True %}
         <p style="color:#ff0000;">Þetta Notendanafn er nú þegar tekið</p>
      {% else %}
         <p style="color:#ffffff">_</p>
      {% endif %}
   </div>
{% endblock %}