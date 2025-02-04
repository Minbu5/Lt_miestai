import turtle
from tkinter import *
import pandas as pd
from main_funk import bkiller, city_dot, city_title
from data_genee import d_genee

# ____________________________Konstantos_______________________________________________________________________________
SRIFTAS = ("Courier", 16, "bold")
MIESTO_SR = ("Courier", 12, "bold")
ZEMELAPIS = "Lietuva blank.gif"
PIRMAS_MIESTAS = "Motoriškės"
GELTONA_LT = "#FDB913"
ZALIA_LT = "#006A44"
RAUDONA_LT = "#C1272D"
# __________________________Pagrindinio ekrano-žemėlapio nustatymas___________________________________________________________

screen = turtle.Screen()
screen.setup(width=1330, height=950)
screen.title("Lietuvos miestai")
screen.addshape(ZEMELAPIS)
turtle.shape(ZEMELAPIS)

# __________________________Duomenu formavimas/atnaujinimas_______________________________________________________________________________
d_genee()


# ______________________________Lengvas variantas___________________________________________________________________
# todo 1 Lengvas

def lengvas():
    bkiller(mygt_lengvas, mygt_vidutinis, mygt_sunkus)

    # Migtukai ivestys
    uzr_zaid_salyga = Label(text="Spėkite gyvenvietes\nturinčias miesto statusą\n2019 m. duomenimis", font=SRIFTAS)
    uzr_zaid_salyga.place(x=100, y=525)

    ivestis = Entry(background=GELTONA_LT)
    ivestis.place(x=180, y=620)

    # Duomenys
    duom = pd.read_csv("103_miestai.csv", index_col=[0])
    visi_miestai = duom.Miestas.to_list()
    atsp_miestai = []

    # Mygtuko su žemėlapiu sąsaja
    def paspausk_spejimas():
        irasas = ivestis.get().title()
        uzr_ivesta.config(text=irasas)

        # žemėlapio valdymas
        if irasas in visi_miestai and irasas not in atsp_miestai:
            m_eil = duom[duom.Miestas == irasas]
            atsp_miestai.append(irasas)

            # miesto taškas
            # failo indeksai reiktu sugenerinti vienodus failus lengvo, vidutinio ir sunkaus!! pergeneruoti 103_miestai
            x = int(m_eil.iloc[0][1])
            y = int(m_eil.iloc[0][2])

            # miesto zenklų ansamblis
            city_dot(x, y)
            city_title(x, y, irasas, MIESTO_SR)

            uzr_atspeta = Label(text=f"Atspėta: {len(atsp_miestai)} iš {len(visi_miestai)}", font=SRIFTAS)
            uzr_atspeta.place(x=130, y=750)

        ivestis.delete(0, END)

    mygt_spejimas = Button(text="spėjimas", command=paspausk_spejimas, background=ZALIA_LT)
    mygt_spejimas.place(x=210, y=650)

    uzr_ivesta = Label(text=PIRMAS_MIESTAS, font=SRIFTAS, background=RAUDONA_LT)
    uzr_ivesta.place(x=190, y=685)


# ______________________________Vidutinis variantas___________________________________________________________________
# todo 2 Vidutinis
def vidutinis():
    bkiller(mygt_lengvas, mygt_vidutinis, mygt_sunkus)
    # Duomenys
    duom = pd.read_csv("50_maziausiu_pagal_gyv.csv", index_col=[0])
    visi_miestai = duom.Miestas.to_list()
    atsp_miestai = []

    # Migtukai ivestys
    uzr_zaid_salyga = Label(text=f"Spėkite {len(visi_miestai)} mažiausių\nmiestų pagal\n"
                                 "gyventojų skaičių"
                                 "\n2019 m. duomenimis", font=SRIFTAS)
    uzr_zaid_salyga.place(x=100, y=525)

    ivestis = Entry(background=GELTONA_LT)
    ivestis.place(x=180, y=620)

    # Mygtuko su žemėlapiu sąsaja
    def paspausk_spejimas():
        irasas = ivestis.get().title()
        uzr_ivesta.config(text=irasas)

        # žemėlapio valdymas
        if irasas in visi_miestai and irasas not in atsp_miestai:
            m_eil = duom[duom.Miestas == irasas]
            atsp_miestai.append(irasas)

            # miesto taškas
            x = int(m_eil.iloc[0][1])
            y = int(m_eil.iloc[0][2])

            # miesto zenklų ansamblis
            city_dot(x, y)
            city_title(x, y, irasas, MIESTO_SR)

            uzr_atspeta = Label(text=f"Atspėta: {len(atsp_miestai)} iš {len(visi_miestai)}", font=SRIFTAS)
            uzr_atspeta.place(x=130, y=750)

        ivestis.delete(0, END)

    mygt_spejimas = Button(text="spėjimas", command=paspausk_spejimas, background=ZALIA_LT)
    mygt_spejimas.place(x=210, y=650)

    uzr_ivesta = Label(text=PIRMAS_MIESTAS, font=SRIFTAS, background=RAUDONA_LT)
    uzr_ivesta.place(x=190, y=685)


# ______________________________Sunkus variantas___________________________________________________________________
# todo 3 Sunkus
def sunkus():
    bkiller(mygt_lengvas, mygt_vidutinis, mygt_sunkus)

    # Duomenys
    duom = pd.read_csv("20_maziausiu_pagal_gyv.csv", index_col=[0])
    visi_miestai = duom.Miestas.to_list()
    atsp_miestai = []

    # Migtukai ir ivestys
    uzr_zaid_salyga = Label(text=f"Spėkite {len(visi_miestai)} mažiausių\nmiestų pagal\n"
                                 "gyventojų skaičių"
                                 "\n2019 m. duomenimis", font=SRIFTAS)
    uzr_zaid_salyga.place(x=100, y=525)

    ivestis = Entry(background="yellow")
    ivestis.place(x=180, y=620)

    # Mygtuko su žemėlapiu sąsaja
    def paspausk_spejimas():
        irasas = ivestis.get().title()
        uzr_ivesta.config(text=irasas)

        # žemėlapio valdymas
        if irasas in visi_miestai and irasas not in atsp_miestai:
            m_eil = duom[duom.Miestas == irasas]
            atsp_miestai.append(irasas)

            # miesto taškas
            x = int(m_eil.iloc[0][1])
            y = int(m_eil.iloc[0][2])

            # miesto zenklų ansamblis
            city_dot(x, y)
            city_title(x, y, irasas, MIESTO_SR)

            uzr_atspeta = Label(text=f"Atspėta: {len(atsp_miestai)} iš {len(visi_miestai)}", font=SRIFTAS)
            uzr_atspeta.place(x=130, y=750)

        ivestis.delete(0, END)

    mygt_spejimas = Button(text="spėjimas", command=paspausk_spejimas, background=ZALIA_LT)
    mygt_spejimas.place(x=210, y=650)

    uzr_ivesta = Label(text=PIRMAS_MIESTAS, font=SRIFTAS, background=RAUDONA_LT)
    uzr_ivesta.place(x=190, y=685)


# mygtukai_veliava()
mygt_lengvas = Button(text="lengvas lygis", command=lengvas, width=20, background=GELTONA_LT)
mygt_lengvas.place(x=150, y=525)

mygt_vidutinis = Button(text="vidutinis lygis", command=vidutinis, width=20, background=ZALIA_LT)
mygt_vidutinis.place(x=150, y=550)

mygt_sunkus = Button(text="sunkus lygis", command=sunkus, width=20, background=RAUDONA_LT)
mygt_sunkus.place(x=150, y=575)

screen.mainloop()
