version="ALPHA 0.2"
print("Chargement...") # Chargement
try:
    from tkinter.messagebox import * # Imports
    from tkinter import *
    import webbrowser as web
    from time import *
except Exception as e: # En cas d'erreur pendant le chargement des bibliothèques
    try:showerror("Erreur fatale",e) # Essayer d'afficher une erreur avec tkinter.messagebox...
    except Exception:print("Erreur fatale lors du chargement de Expience : "+e) 

E=Tk()
TEXTES=["Expience v"+version] # Liste des textes renseignés plusieurs fois
E.title("Expience v" + version)
COULEUR_FOND="#CECECE" # Couleur des fonds de canvas
def showinfo_desactive():showinfo("Information","Cette option a été désactivée.") # messagebox d'information : option désactivées
def ouvrir_propos():web.open("https://github.com/MonsieurOuiplala/expience/")
def fermer_experience():E
class tube_a_essai: # Classe pour les tubes à essai
    def __init__(self,x,y,contenu=None,contenu_noms=None,regles=None,afficher_melanger=False):
        if contenu==None:self.contenu=[COULEUR_FOND]*5
        if contenu_noms==None:self.contenu_noms=["Air"]*5
        self.regles = regles if regles is not None else []
        if afficher_melanger:canvas.create_window(x+15,y+240,window=Button(E,text="Mélanger",command=self.melanger))
        
        self.partie0=canvas.create_polygon(x,y+20,x,y+60,x+30,y+60,x+30,y+20,fill=self.contenu[0],outline="black")
        self.partie1=canvas.create_polygon(x,y+60,x,y+100,x+30,y+100,x+30,y+60,fill=self.contenu[1],outline="black")
        self.partie2=canvas.create_polygon(x,y+100,x,y+140,x+30,y+140,x+30,y+100,fill=self.contenu[2],outline="black")
        self.partie3=canvas.create_polygon(x,y+140,x,y+180,x+30,y+180,x+30,y+140,fill=self.contenu[3],outline="black")
        self.partie4=canvas.create_polygon(x,y+180,x,y+220,x+30,y+220,x+30,y+180,fill=self.contenu[4],outline="black")
        self.ligne0=canvas.create_line(x,y,x,y+20)
        self.ligne1=canvas.create_line(x,y+20,x+30,y+20)
        self.ligne2=canvas.create_line(x+30,y+20,x+30,y)
    def maj(self):
        try:
            for j in range(len(self.contenu)):canvas.itemconfig(eval("self.partie"+str(len(self.contenu)-1-j)),fill=self.contenu[j])
        except Exception as e:showerror("Erreur dans le code",e)
    def ajouter(self,couleur,nom):
        for i in range(len(self.contenu)):
            if self.contenu[i]==COULEUR_FOND:
                self.contenu[i]=couleur
                self.contenu_noms[i]=nom
                self.maj()
                break
    def definir(self,nouveau_contenu,nouveaux_noms):
        self.contenu=nouveau_contenu
        self.contenu_noms=nouveaux_noms
    def melanger(self):
        if not self.regles:return
        for conditions, resultats in self.regles:
            if all(elem in self.contenu_noms for elem in conditions):
                couleur_resultat, nom_resultat = resultats
                for i in range(len(self.contenu_noms)):
                    if self.contenu_noms[i] in conditions:
                        self.contenu[i] = couleur_resultat
                        self.contenu_noms[i] = nom_resultat
                self.maj()

Label(E,text=TEXTES[0]).pack()
print("Chargement des expériences...")
def sulfate_de_cuivre_anhydre():
    global canvas
    sca_label=Label(E,text="Le test au sulfate de cuivre anhydre permet de déterminer la présence d'eau :\nsi le sulfate devient bleu, cela indique que la substance testée contient de l'eau, tandis que l'absence de changement de couleur\nsignifie qu'il n'y a pas d'eau ou en quantité trop faible pour être détectée.")
    sca_label.pack()
    canvas=Canvas(E, width=750, height=500, background=COULEUR_FOND) # Canvas
    canvas.pack()
    sca_ligne0=canvas.create_line(120,0,120,502) # Séparation liste réactifs/zone d'expérience
    sca_coupelle = canvas.create_polygon(325,325,350,350,500,350,525,325,fill='white',outline='white',width=0)
    sca_ligne1=canvas.create_line(300,300,350,350) # Coupelle
    sca_ligne2=canvas.create_line(350,350,500,350)
    sca_ligne3=canvas.create_line(500,350,550,300)
    sca_texte_resultat=canvas.create_text(425,380,text="En attente d'un premier test...")
    sca_reactifs={"Eau":True,"Lait":True,"Pétrole":False,"Vinaigre":True,"Huile":False,"Pomme de terre":True,"Tomate":True,"Papier":False} # Réactifs
    def sca_reaction(reactif:str):
        sca_resultat=sca_reactifs[reactif]
        if sca_resultat:
            for i in range(256):
                couleur = f"#{255 - i:02x}{255 - i:02x}ff"
                canvas.itemconfig(sca_coupelle,fill=couleur,outline=couleur)
                E.update()
                sleep(0.004)
            canvas.itemconfig(sca_texte_resultat,text="Résultat du test au sulfate de cuivre anhydre : positif",fill="blue")
            print("Résultat positif au test au sulfate de cuivre anhydre avec pour réactif : "+reactif)
            sleep(5)
            canvas.itemconfig(sca_coupelle,fill="white",outline="white")
        elif not sca_resultat:
            sleep(3)
            canvas.itemconfig(sca_texte_resultat,text="Résultat du test au sulfate de cuivre anhydre : négatif",fill="black")
            print("Résultat négatif au test au sulfate de cuivre anhydre avec pour réactif : "+reactif)
    canvas.create_window(60, 20, window=Button(E,text="Eau",command=lambda:sca_reaction("Eau")))
    canvas.create_window(60, 50, window=Button(E,text="Lait",command=lambda:sca_reaction("Lait")))
    canvas.create_window(60, 80, window=Button(E,text="Pétrole",command=lambda:sca_reaction("Pétrole")))
    canvas.create_window(60, 110, window=Button(E,text="Vinaigre",command=lambda:sca_reaction("Vinaigre")))
    canvas.create_window(60, 140, window=Button(E,text="Huile",command=lambda:sca_reaction("Huile")))
    canvas.create_window(60, 170, window=Button(E,text="Pomme de terre",command=lambda:sca_reaction("Pomme de terre")))
    canvas.create_window(60, 200, window=Button(E,text="Tomate",command=lambda:sca_reaction("Tomate")))
    canvas.create_window(60, 230, window=Button(E,text="Papier",command=lambda:sca_reaction("Papier")))

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
