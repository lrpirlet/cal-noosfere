ID_NAME = "nsfr_id"
url_list = ["https://www.noosfere.org/livres/niourf.asp?numlivre=2146634342",
            "https://www.noosfere.org/livres/niourf.asp?numlivre=2970",
            "https://www.noosfere.org/livres/niourf.asp?numlivre=2146610758",
            "https://www.noosfere.org/livres/niourf.asp?numlivre=-324700",
            "https://www.noosfere.org/livres/niourf.asp?NumLivre=2146572377",
            "https://www.noosfere.org/livres/niourf.asp?NumLivre=2146587399"]

for url in url_list:
    '''
    id_from_url : takes an URL and extracts the identifier details...
    '''
    idt=""
    if "https://www.noosfere.org/livres/niourf.asp?numlivre=" in url.lower():
        idt = url.lower().replace("https://www.noosfere.org/livres/niourf.asp?numlivre=","").strip()

    if idt:
        print(ID_NAME, "vl$" + idt)
    else:
        print("None")

