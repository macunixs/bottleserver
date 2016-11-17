<!DOCTYPE html>
<html>
<head>
<title> LED Webserver Bottle Python </title>
<meta name="viewport" content="width=device-width,initial-scale=1"

</head>
<body>

<h1>Door Lock using Bottle Python</h1>

<form method="POST" action="unlock">
	<p>Enter Password</p>
	<input type="password" name="password" length="20"/>
	<input id ="sub" type="submit" value="OK"/>
</form>

<form method="POST" action="rgbon">
	<p>RGBLED Switch</p>
	<button>ON LED</button>
	<a href="/">Back</a>
</form>
<form method="POST" action="rgboff">
	<p>RGBLED Switch</p>
	<button>OFF LED</button>
</form>

</body>
</html>
