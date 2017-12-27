---
layout: post
---

## change background ##



> polls/templates/polls/index.html

> `{% load static %}`

> `<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" />`

> `body {
    	 background: white url("images/background.gif") no-repeat right bottom;
    	}`


DIR:

appname/static/polls/style.css
appname/static/polls/images/background.gif