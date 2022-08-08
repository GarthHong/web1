#!python
print('Content-Type: text/html\n')
import cgi
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form['id'].value
else:
    pageId = 'WEB'
print(pageId)
print('''<!doctype html>
<html>
<head>
  <title>WEB - Welcome</title>
  <meta charset = "utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    <li><a href="index.py?id=HTML">HTML</a></li>
    <li><a href="index.py?id=CSS">CSS</a></li>
    <li><a href="index.py?id=JavaScript">JavaScript</a></li>
  </ol>
  <h2>{title}</h2>
  <p>The World Wide Web (abbreviated WWW or the Web) is an information space where documents and other web resources are identified by Uniform Resource Locators (URLs).
  </p>
</body>
</html>
'''.format(title='WEB'))
