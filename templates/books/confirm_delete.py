{% include '../header.html' %}

<center>
    <h1>Вы уверенны что хотите удалить книгу?</h1>
    <form method="POST">
        {% csrf_token %}
        <button type="submit">Да</button>
        <button><a href="/Books_list/">Нет</a></button>
    </form>
</center>




{% include '../footer.html' %}