version="ALPHA 0.1"
print("Chargement...") # Chargement
try:
    from tkinter.messagebox import * # Import tkinter.messagebox et tkinter
    from tkinter import *
    import webbrowser as web
    from time import *
except Exception as e: # En cas d'erreur pendant le chargement des bibliothèques
    try:showerror("Erreur fatale",e) # Essayer d'afficher une erreur avec tkinter.messagebox...
    except Exception:print("Erreur fatale lors du chargement de Expience : "+e) 

E=Tk()
TEXTES=["Expience v"+version] # Liste des textes renseignés plusieurs fois
E.title("Expience v" + version)
def showinfo_desactive():showinfo("Information","Cette option a été désactivée.") # messagebox d'information : option désactivées
def ouvrir_propos():web.open("https://github.com/MonsieurOuiplala/expience/")
def fermer_experience():E
Label(E,text=TEXTES[0]).pack()

print("Chargement des expériences...")
def sulfate_de_cuivre_anhydre():
    sca_label=Label(E,text="Le test au sulfate de cuivre anhydre permet de déterminer la présence d'eau :\nsi le sulfate devient bleu, cela indique que la substance testée contient de l'eau, tandis que l'absence de changement de couleur\nsignifie qu'il n'y a pas d'eau ou en quantité trop faible pour être détectée.")
    sca_label.pack()
    sca_canvas=Canvas(E, width=750, height=500, background="#CECECE") # Canvas
    sca_canvas.pack()
    sca_ligne0=sca_canvas.create_line(120,0,120,502) # Séparation liste réactifs/zone d'expérience
    sca_coupelle = sca_canvas.create_polygon(325,325,350,350,500,350,525,325,fill='white', outline='white', width=0)
    sca_ligne1=sca_canvas.create_line(300,300,350,350) # Coupelle
    sca_ligne2=sca_canvas.create_line(350,350,500,350)
    sca_ligne3=sca_canvas.create_line(500,350,550,300)
    sca_texte_resultat=sca_canvas.create_text(425,380,text="En attente d'un premier test...")
    sca_reactifs={"Eau":True,"Lait":True,"Pétrole":False,"Vinaigre":True,"Huile":False,"Pomme de terre":True,"Tomate":True,"Papier":False} # Réactifs
    def sca_reaction(reactif:str):
        sca_resultat=sca_reactifs[reactif]
        if sca_resultat:
            for i in range(256):
                couleur = f"#{255 - i:02x}{255 - i:02x}ff"
                sca_canvas.itemconfig(sca_coupelle,fill=couleur,outline=couleur)
                E.update()
                sleep(0.004)
            sca_canvas.itemconfig(sca_texte_resultat,text="Résultat du test au sulfate de cuivre anhydre : positif",fill="blue")
            print("Résultat positif au test au sulfate de cuivre anhydre avec pour réactif : "+reactif)
            sleep(5)
            sca_canvas.itemconfig(sca_coupelle,fill="white",outline="white")
        elif not sca_resultat:
            sleep(3)
            sca_canvas.itemconfig(sca_texte_resultat,text="Résultat du test au sulfate de cuivre anhydre : négatif",fill="black")
            print("Résultat négatif au test au sulfate de cuivre anhydre avec pour réactif : "+reactif)
    sca_canvas.create_window(60, 20, window=Button(E, text="Eau", command=lambda:sca_reaction("Eau")))
    sca_canvas.create_window(60, 50, window=Button(E, text="Lait", command=lambda:sca_reaction("Lait")))
    sca_canvas.create_window(60, 80, window=Button(E, text="Pétrole", command=lambda:sca_reaction("Pétrole")))
    sca_canvas.create_window(60, 110, window=Button(E, text="Vinaigre", command=lambda:sca_reaction("Vinaigre")))
    sca_canvas.create_window(60, 140, window=Button(E, text="Huile", command=lambda:sca_reaction("Huile")))
    sca_canvas.create_window(60, 170, window=Button(E, text="Pomme de terre", command=lambda:sca_reaction("Pomme de terre")))
    sca_canvas.create_window(60, 200, window=Button(E, text="Tomate", command=lambda:sca_reaction("Tomate")))
    sca_canvas.create_window(60, 230, window=Button(E, text="Papier", command=lambda:sca_reaction("Papier")))

menu=Menu(E) # Barre d'outils
smenu0=Menu(menu,tearoff=0)
smenu0.add_command(label="Quitter",command=E.destroy)
menu.add_cascade(label="Fenêtre",menu=smenu0)
smenu1=Menu(menu,tearoff=0)
smenu1.add_command(label="Nouvelle expérience",command=showinfo_desactive)
smenu1.add_command(label="Ouvrir expérience",command=showinfo_desactive)
smenu1.add_command(label="Sulfate de cuivre anhydre (SCA)",command=sulfate_de_cuivre_anhydre)
menu.add_cascade(label="Expérience",menu=smenu1)
smenu2=Menu(menu,tearoff=0)
smenu2.add_command(label="À propos",command=ouvrir_propos)
menu.add_cascade(label="Aide",menu=smenu2)
E.config(menu=menu)

E.geometry("800x600") # Taille de la fenêtre : 800*600 pixels
print("Chargement terminé !")
E.mainloop()
