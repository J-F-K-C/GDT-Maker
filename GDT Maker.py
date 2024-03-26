import tkinter as tk

def bearbeite_datei():
    eingabe1 = eingabe1_var.get()
    eingabe2 = eingabe2_var.get()

    try:
        with open("pat.gdt", 'w') as ausgabe_datei:
            ausgabe_datei.write("""01380006301
014810001690
01292182.3
014300015946
0184218{}
0184247{}
0156331188251
0126361GSU
01063628
0143101NACHNAME
0173102VORNAME
017310319450818
0103110M
0183107Testweg
01031091
014311212345
0213113Testtadt
0103114D
0123622167
0123623069
019362602351 55255170
01031085
0193119F123456789
014410112024
014410417603
011410600
017410920240125
01430065.2.0
0184111101575519
0414134Techniker Krankenkasse - TK
011412200
011311646
01041321
017413320090401
01042040
0108609K
023301020240125094026\n""".format(eingabe1, eingabe2))

        print("Die Datei wurde erfolgreich bearbeitet und unter dem Namen 'pat.gdt' gespeichert.")

    except IOError as e:
        print("Fehler beim Schreiben der Datei:", e)

# GUI erstellen
root = tk.Tk()
root.title("Datei erstellen")
# root.geometry("800x600")  # Fenstergröße auf 800x600 setzen

# Eingabefelder für Variablen
eingabe1_var = tk.StringVar()
eingabe2_var = tk.StringVar()

tk.Label(root, text="BSNR:").grid(row=0, column=0)
tk.Entry(root, textvariable=eingabe1_var).grid(row=0, column=1)

tk.Label(root, text="LANR:").grid(row=1, column=0)
tk.Entry(root, textvariable=eingabe2_var).grid(row=1, column=1)

# Button zum Bearbeiten der Datei
tk.Button(root, text="Datei erstellen", command=bearbeite_datei).grid(row=2, column=1)

root.mainloop()