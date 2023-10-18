from L027_Module_test import square, greet

# Det går att testa sin kod själv, genom att koda olika scenarion. 
# Men går även att automatisera, "Unit-testing" kommer in här.
# Man testar för att se att resultat av kod är det man förväntar sig.

# Finns något i Python som heter Assert / Påstår/hävdar

# print("start")   # Denna del var bara för att påvisa de koder mellan start och end

# assert 1 > 0           # inget händer om de stämmer

#  assert 1 < 0           # Kod krashar om det inte stämmer

# Går också att fånga med try-except
# try: 
#     assert 1 > 0
# except AssertionError:
#     print("1 is not less than zero")

# Men det finns också bibliotek för testning i Python, pytest som vi ska titta närmare på. Unittest är den andra.
# IPytest - fångar upp mina asserts i koden och kan göra saker med den.
# Först installeras det: pipenv install pytest, den letar var pipfiler ligger i någon av undermapparna - och sedan installerar där
# pipfilen finns. Så därför, så länge man är i rätt ställe så hittar den. 

# print("end")  # Denna del var bara för att påvisa de koder mellan start och end



# Här är testet för att en funktion funkar som den ska, om nedan går igenom. 
# Tänk dig att du t.ex. gör sådana testfunktioner och sedan kör dom, för att 
# jämföra om resultatet blev som du ville. MEN
# Pytest gör det dock automatiskt och enklare
# Man kör den via terminalen (eller extension) och 
# Den går igenom nedan funktioner och sammanställer resultat.

def test_positive_square():
    assert square(2) == 4
    assert square(5) == 25 , "Square of 5 is not 25"

def test_negative_square():
    assert square(-2) == 4
    assert square(-5) == 25, "Square of 5 is not 25"

def test_zero_square():
    assert square(0) == 0

def test_greet_default():
     assert greet() == "Hello, World"

def test_greet_argument():
     assert greet("Fredrik") == "Hello, Fredrik"


# Mer OM HUR PYTEST FUNKAR:
# Den kollar på vilket värde MAN FÅR UT, vid en viss INPUT,
# MEd detta så ska det vara enklare kod för att se VAD man vill få ut, än HUR man ska få ut det.
# VILKA FILER OCH FUNKTIONER TESTAR DEN?
# När man skriver pytest i terminalen, så letar den upp alla filer i dess root directory 
# eller mappar under (sub directory). Filer som antingen börjar eller slutar på test letar den efter.
# I dessa filer kommer den LETA UPP ALLA FUNKTIONER SOM BÖRJAR PÅ TEST_ och antar att detta är vad den ska testa.
        # Viktigt att hålla sig till detta då - att kalla varje funktion som ska testas för test_något.
        # Rött F  betyder failed, grön punkt betyder gick igenom. För varje funktion med test fås ett F eller grön punkt.
        # Bara för att testerna går igenom betyder inte att koden funkar som den ska 
# Vid refaktoring (cleanande av kod utan att funktion påverkas), är såna tester särskilt bra. Då kan man upptäcka om en funktionalitet försvann i samband med det.
# Varje "enhet"/funktion testas för sig - FÅR INTE HA SIDE-effects om det ska gå att testa ("lös kod")

