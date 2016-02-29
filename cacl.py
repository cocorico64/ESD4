chiffre1 = raw_input ('Veuillez entrer le premier chiffre :')
operateur = raw_input ('Veuillez entrer votre operateur :')
chiffre2 = raw_input ('Veuillez entrer le deuxieme chiffre ')
chiffre3 = int(chiffre1) + int(chiffre2)
chiffre4 = int(chiffre1) - int(chiffre2)
chiffre5 = int(chiffre1) * int(chiffre2)
chiffre6 = int(chiffre1) / int(chiffre2)


if operateur == "+":
	print chiffre3
elif operateur == "-":
	print chiffre4
elif operateur == "*":
	print chiffre5
elif operateur == "/":
	print chiffre6