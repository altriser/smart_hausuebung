x = raw_input("Bitte geben Sie eine Zahl ein!")
y = raw_input("geben Sie eine zweite Zahl ein!")

x_neu = int(x)
y_neu= int(y)
print "Ergebnis", x_neu + y_neu

z = int(x_neu+y_neu)

if z<10:
    print "Falsch,hoeher!"
elif z>10:
    print "Falsch,niederiger!"
else:
    print "richtiges Ergebnis"