import pandas as pd

WEB_SALTINIS = "https://lt.wikipedia.org/wiki/S%C4%85ra%C5%A1as:Lietuvos_miestai"
KORD_SALTINIS = "cord_hunt_stack.csv"
MAZIAUSIU_TOP_50 = 50
MAZIAUSIU_TOP_20 = 20


def d_genee():
    # __________________103_miestai.csv generavimas____________________________________
    miestu_duomenys = pd.read_html(WEB_SALTINIS)

    m_sarasas = miestu_duomenys[1]["Miestas"]
    kord_duomenys = pd.read_csv(KORD_SALTINIS, index_col=[0])
    gyv_sk = miestu_duomenys[1]["Gyventojų skaičius (2019 m.)"]

    bendras = pd.concat([m_sarasas, kord_duomenys, gyv_sk], axis=1)

    # bendras.to_csv("103_miestai_abc.csv") # miestai pagal abecelę

    # ____________________nauju csv vidutinis(50) ir sunkus(20) zaidimui gavimas______________________________________
    rusiuotas = bendras.sort_values(by=["Gyventojų skaičius (2019 m.)"])
    rusiuotas.to_csv("103_miestai.csv")
    rusiuotas.head(MAZIAUSIU_TOP_50).to_csv("50_maziausiu_pagal_gyv.csv")
    rusiuotas.head(MAZIAUSIU_TOP_20).to_csv("20_maziausiu_pagal_gyv.csv")
d_genee()
