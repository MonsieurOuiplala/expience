version="ALPHA 0.0"
print("Chargement...") # Chargement
try:
    from tkinter.messagebox import * # Import tkinter.messagebox et tkinter
    from tkinter import *
except Exception as e: # En cas d'erreur pendant le chargement des bibliothèques
    try:showerror("Erreur fatale",e) # Essayer d'afficher une erreur avec tkinter.messagebox...
    except Exception:print("Erreur fatale lors du chargement de Expience : "+e) 

E=Tk()
E.title("Expience v" + version)
def showinfo_desactive():showinfo("Information","Cette option a été désactivée.") # messagebox d'information
Label(E,text="Expience v" + version).pack()

menu=Menu(E) # Barre d'outils
smenu0=Menu(menu,tearoff=0)
smenu0.add_command(label="Quitter",command=E.destroy)
menu.add_cascade(label="Fenêtre",menu=smenu0)
smenu1=Menu(menu,tearoff=0)
smenu1.add_command(label="Nouvelle expérience",command=showinfo_desactive)
smenu1.add_command(label="Ouvrir expérience",command=showinfo_desactive)
menu.add_cascade(label="Expérience",menu=smenu1)
E.config(menu=menu)
E.geometry("800x600") # Taille de la fenêtre : 800*600 pixels
print("Chargement terminé !")
E.mainloop()
