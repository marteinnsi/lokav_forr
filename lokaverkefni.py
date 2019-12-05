# Marteinn Hugi Sigurgeirsson (2907022160)
# Lokaverkefni
# 26. nóvember 2019

import random
import time
from enum import Enum

nofn = [
    "Ari",
    "Jón",
    "Sigurður",
    "Alexander",
    "Ingvar",
    "Daníel",
    "Benedikt",
    "Einar",
    "Gunnar",
    "Guðmundur",
    "Ólafur",
    "Kristján",
    "Stefán",
    "Jóhann",
    "Björn",
    "Arnar",
    "Árni",
    "Bjarni",
    "Helgi",
    "Halldór",
    "Pétur",
    "Kristinn",
    "Ragnar",
    "Gísli",
    "Þorsteinn",
    "Guðjón",
    "Aron",
    "Sveinn",
    "Róbert",
    "Páll",
    "Óskar",
    "Birgir",
    "Davíð",
    "Andri",
    "Viktor",
    "Bjarki",
    "Tómas",
    "Haukur",
    "Jóhannes",
    "Ágúst",
    "Karl",
    "Ásgeir",
    "Brynjar",
    "Haraldur",
    "Atli",
    "Kjartan",
    "Baldur",
    "Þórður",
    "Hilmar",
    "Kristófer",
    "Kári",
    "Hörður",
    "Rúnar",
    "Jónas",
    "Egill",
    "Eiríkur",
    "Sindri",
    "Björgvin",
    "Sævar",
    "Guðni",
    "Elvar",
    "Elfar",
    "Hlynur",
    "Sverrir",
    "Örn",
    "Ómar",
    "Ísak",
    "Jakob",
    "Snorri",
    "Dagur",
    "Reynir",
    "Ingólfur",
    "Mattías",
    "Ívar",
    "Arnór",
    "Anton",
    "Hafsteinn",
    "Birkir",
    "Garðar",
    "Þórarinn",
    "Eyþór",
    "Axel",
    "Þórir",
    "Grétar",
    "Tryggvi",
    "Emil",
    "Steinar",
    "Valdimar",
    "Vilhjálmur",
    "Mikael",
    "Ingi",
    "Hjalti",
    "Hákon",
    "Adam",
    "Hermann",
    "Hjörtur",
    "Aðalsteinn"
]


def smida_hermann(aettbalkur, super):
    nafn = random.choice(nofn)
    lif = random.randint(10, 15) if super else random.randint(1, 5)
    afl = random.randint(4, 9) if super else random.randint(1, 5)
    vopn = random.choice(list(Vopn))
    return Hermadur(aettbalkur, nafn, lif, afl, vopn, super)


def smida_hermenn(aettbalkur, venjulegir, super):
    hermenn = []
    for n in range(venjulegir):
        hermenn.append(smida_hermann(aettbalkur, False))
    for n in range(super):
        hermenn.append(smida_hermann(aettbalkur, True))
    return hermenn


def prenta_og_bida(prenta):
    print(prenta)
    time.sleep(0.5)


class Aettbalkur(Enum):
    PESSAR = 0
    HETTIR = 1
    DREYRAR = 2

    def __str__(self):
        return self.name.lower()


class Vopn(Enum):
    SVERD = 0
    SPJOT = 1
    EXI = 2

    def __str__(self):
        if self == Vopn.SVERD:
            return "sverð"
        elif self == Vopn.SPJOT:
            return "spjót"
        elif self == Vopn.EXI:
            return "exi"
        else:
            return "óþekkt vopn"


class Hermadur:
    aettbalkur = None
    lid = None
    nafn = None
    lif = None
    afl = None
    vopn = None
    super = None

    def __init__(self, aettbalkur, nafn, lif, afl, vopn, super):
        self.aettbalkur = aettbalkur
        self.nafn = nafn
        self.lif = lif
        self.afl = afl
        self.vopn = vopn
        self.super = super

    def __str__(self):
        out = ""
        if self.lif < 1:
            out += "dauður "
        if self.super:
            out += "ofur"
        return out + f"hermaður að nafni {self.nafn} með {self.afl} afl og {self.vopn} og {self.lif} líf"


pessar = smida_hermenn(Aettbalkur.PESSAR, 7, 3)
hettir = smida_hermenn(Aettbalkur.HETTIR, 7, 3)
dreyrar = smida_hermenn(Aettbalkur.DREYRAR, 7, 3)
aettbalkar = [pessar, hettir, dreyrar]
lota = 1

while True:
    print("=" * 90)
    print(f"LOTA {lota}... ")
    print("-" * 90)

    # velja ættbálkana sem verjast
    aettbalkurEitt = random.choice(aettbalkar)
    aettbalkurTvo = None

    while not aettbalkurTvo or aettbalkurTvo == aettbalkurEitt:
        aettbalkurTvo = random.choice(aettbalkar)

    hermadurEitt = random.choice(aettbalkurEitt)
    hermadurTvo = random.choice(aettbalkurTvo)
    sigurvegari = None
    tapari = None

    prenta_og_bida(f"{hermadurEitt.aettbalkur.__str__().capitalize()} setja út: {hermadurEitt}.")
    prenta_og_bida(f"{hermadurTvo.aettbalkur.__str__().capitalize()} setja út: {hermadurTvo}.")

    if hermadurEitt.afl == hermadurTvo.afl:
        prenta_og_bida(f"{hermadurEitt.nafn} og {hermadurTvo.nafn} hafa jafnt afl.")
        if hermadurEitt.vopn == Vopn.SPJOT and hermadurTvo.vopn != Vopn.SPJOT:
            prenta_og_bida(f"... en {hermadurEitt.nafn} hefur spjót.")
            sigurvegari = hermadurEitt

        elif hermadurTvo == Vopn.SPJOT and hermadurEitt.vopn != Vopn.SPJOT:
            prenta_og_bida(f"... en {hermadurTvo.nafn} hefur spjót.")
            sigurvegari = hermadurTvo
        else:
            sigurvegari = random.choice([hermadurEitt, hermadurTvo])
            prenta_og_bida(f"...en af hæfileikum einum sigrar {sigurvegari.nafn}.")

    elif hermadurEitt.afl > hermadurTvo.afl:
        prenta_og_bida(f"{hermadurEitt.nafn} hefur meira afl og {hermadurTvo.nafn} endist ekki lengi.")
        sigurvegari = hermadurEitt

    elif hermadurTvo.afl > hermadurEitt.afl:
        prenta_og_bida(f"{hermadurTvo.nafn} hefur meira afl og {hermadurEitt.nafn} endist ekki lengi.")
        sigurvegari = hermadurTvo

    tapari = hermadurEitt if sigurvegari == hermadurTvo else hermadurTvo
    tapari.lif -= 1
    tapariDeyr = tapari.lif < 1

    # gera leikinn aðeins merkilegri, útskýra hvað gerðist
    if sigurvegari.vopn == Vopn.SVERD:
        if tapariDeyr:
            prenta_og_bida(f"{sigurvegari.nafn} veitir {tapari.nafn} banahöggi með sverði sínu.")
        else:
            prenta_og_bida(f"{sigurvegari.nafn} særir {tapari.nafn} með sverði sínu.")

    elif sigurvegari.vopn == Vopn.SPJOT:
        if tapariDeyr:
            prenta_og_bida(f"{sigurvegari.nafn} gatar {tapari.nafn} með spjóti sínu.")
        else:
            prenta_og_bida(f"{sigurvegari.nafn} særir {tapari.nafn} með spjóti sínu.")

    elif sigurvegari.vopn == Vopn.EXI:
        if tapariDeyr:
            prenta_og_bida(f"{sigurvegari.nafn} hálsheggur {tapari.nafn} með exi sinni.")
        else:
            prenta_og_bida(f"{sigurvegari.nafn} særir {tapari.nafn} með exi sinni.")

    prenta_og_bida(f"{sigurvegari.nafn} sigrar bardagann á móti {tapari.nafn}. (-1)")

    # taka burt líf af ofurhermönnum
    if sigurvegari.super:
        prenta_og_bida(f"{sigurvegari.nafn} skaðast af bölvun ofur-hermannsins. (-1)")
        sigurvegari.lif -= 1

    if tapari.super:
        prenta_og_bida(f"{tapari.nafn} skaðast af bölvun ofur-hermannsins. (-1)")
        tapari.lif -= 1

    # eyða dauðum hermönnum
    if sigurvegari.lif < 1:
        prenta_og_bida(f"{sigurvegari.nafn} deyr.")
        if sigurvegari in dreyrar:
            dreyrar.remove(sigurvegari)
        if sigurvegari in pessar:
            pessar.remove(sigurvegari)
        if sigurvegari in hettir:
            hettir.remove(sigurvegari)
    else:
        prenta_og_bida(f"{sigurvegari.nafn} hefur nú {sigurvegari.lif} líf.")

    if tapariDeyr:
        prenta_og_bida(f"{tapari.nafn} deyr.")
        if tapari in dreyrar:
            dreyrar.remove(tapari)
        if tapari in pessar:
            pessar.remove(tapari)
        if tapari in hettir:
            hettir.remove(tapari)
    else:
        prenta_og_bida(f"{tapari.nafn} hefur nú {tapari.lif} líf.")

    # eyða út liðum sem hafa enga hermenn
    if len(aettbalkurEitt) == 0:
        prenta_og_bida(f"{hermadurTvo.aettbalkur.__str__().capitalize()} útrýma {hermadurEitt.aettbalkur.__str__().capitalize()}.")
        aettbalkar.remove(aettbalkurEitt)
    if len(aettbalkurTvo) == 0:
        prenta_og_bida(f"{hermadurEitt.aettbalkur.__str__().capitalize()} útrýma {hermadurTvo.aettbalkur.__str__().capitalize()}.")
        aettbalkar.remove(aettbalkurTvo)

    # ef það er 1 lið eftir þá hefur það sigrað
    # ef það eru 0 lið eftir þá hafa allir tapað.
    if len(aettbalkar) == 1:
        sigurvegarar = aettbalkar[0]
        prenta_og_bida(f"{sigurvegari.aettbalkur.__str__().capitalize()} hafa útrýmt öllum öðrum ættbálkum og sigra orustuna. Til hamingju!")
        exit()
    elif len(aettbalkar) == 0:
        prenta_og_bida(f"{hermadurEitt.aettbalkur.__str__().capitalize()} og {hermadurTvo.aettbalkur.__str__().capitalize()} hafa útrýmt hvor öðrum og enginn stendur eftir.")
        prenta_og_bida("Enginn er sigurvegari.")
        exit()

    lota += 1
