print("Welcome to our online Website maker...")
print("Pls enter the required Information...")
print()
shop_name = input("Enter your shop's name: ")
description = input("Enter your shop or idea description: ")
phone = int(input("Enter your ph no.: "))
address = input("Enter your shop's adsress: ")
offer = input("Enter your offer: ")
print()
print()

html = f"""
<!DOCTYPE html>
<html>
<head>
<title>{shop_name}</title>
<style>
body {{
background-color: green;
text-align: center;
font-famiy: Arial;
text-align: center;
border: 3px solid;
}}
h1 {{
font-weight: bold;
font-size: 40px;
color: red;
}}
p {{
font-size: 20px;
color: skyblue;
}}
h2 {{
font-weight: bold;
font-size: 40px;
}}
mark {{
background-color: yellow;
color: red;
}}
h3{{
font-size: 30px;
}}
</style>
</head>
<body>
<h1>{shop_name}</h1>
<p>{description}</p>
<h3><b>Phone: </b>{phone}<b><br>Address: </b>{address}</h3>
<h2><mark>{offer}</mark></h2>
</body>
</html>
"""

with open("shop_website.html", "w", encoding="utf-8") as file:
    file.write(html)
            
print("Website Created Succesfully!!!")
print("Open shop_website.html in your browser...")
