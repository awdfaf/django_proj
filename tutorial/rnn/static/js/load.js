function doSumething() {
    {% csrf_token %}
    fm = document.getElementById("fm");
    fm.action ='/rnn/load/'
    fm.submit();
}
