info = '''<html>
 <head>
  <script language="JavaScript">
   function popuphlp(page,nom,poption) {
var w=window.open(page, nom, poption);
w.focus();
}
  </script>
  <link href="/images/favicon.ico" rel="shortcut icon" type="image/x-icon"/>
  <script>
   function montre(div)
{
var item=document.getElementById(div);
var img=document.getElementById('img_' + div);
var expDate = new Date();
expDate.setTime(expDate.getTime() + (7 * 24 * 3600 * 1000));
if(item.style.display =='none') {
  item.style.visibility='visible';
  item.style.display='block';
  img.src = '/images/minus_L.gif';
  // document.cookie = div + '.visible=OUI;expires=' + expDate.toGMTString();
  }
  else {
  item.style.visibility='hidden';
  item.style.display='none';
  img.src = '/images/plusik_l.gif';
  // document.cookie = div + '.visible=NON;expires=' + expDate.toGMTString();
  }
}
  </script>
  <title>
   Bien après minuit - Ray BRADBURY - Fiche livre -  Critiques - Adaptations - nooSFere
  </title>
  <meta content="Bien après minuit, Ray BRADBURY" property="og:title"/>
  <meta content="Bien après minuit, Ray BRADBURY" name="twitter:text:title"/>
  <meta content="Fiche livre, critiques, adaptations" property="og:description"/>
  <meta content="https://images.noosfere.org/couv/p/pdf248-1977.jpg" property="og:image"/>
  <meta content="@noosfere" name="twitter:site"/>
  <meta content="https://images.noosfere.org/couv/p/pdf248-1977.jpg" name="twitter:image"/>
  <meta content="summary_large_image" name="twitter:card"/>
  <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
  <meta content="nooSFere" name="description"/>
  <meta content="SF fantastique fantasy imaginaire" name="keywords"/>
  <meta content="noocontact@noosfere.com" name="author"/>
  <link href="favicon.ico" rel="icon"/>
  <!-- Inclure la charte -->
  <script language="JavaScript">
   //MENU AT START
startmenu = 'noo3'; //Encyclopédie
  </script>
 </head>
 <body>
  <table align="center" width="100%">
   <tbody>
    <tr>
     <td>
      <link href="/images/charte1/noostyle.css?vers=49" rel="StyleSheet" type="text/css"/>
      <link href="/modules/charte/choix/modal-message.css" rel="stylesheet" type="text/css"/>
      <script src="/modules/charte/choix/ajax.js" type="text/javascript">
      </script>
      <script src="/modules/charte/choix/modal-message.js" type="text/javascript">
      </script>
      <script src="/modules/charte/choix/ajax-dynamic-content.js" type="text/javascript">
      </script>
      <script type="text/javascript">
       messageObj = new DHTML_modalMessage();	// We only create one object of this class
messageObj.setShadowOffset(5);	// Large shadow

function afficherChoix(url)
{
	messageObj.setSource(url);
	messageObj.setCssClassMessageBox(false);
	messageObj.setSize(300,350);
	messageObj.setShadowDivVisible(true);	// Enable shadow for these boxes
	messageObj.display();
}

function cacherChoix()
{
	messageObj.close();
}
      </script>
      <script>
       function afficher_cacher(id,id2)
{
    if(document.getElementById(id).style.display=="none") {
        document.getElementById(id).style.display="inline";
        document.getElementById(id2).style.marginLeft="200px";
		document.cookie="menugauche=inline";
    }
    else {
        document.getElementById(id).style.display="none";
        document.getElementById(id2).style.marginLeft="5px";
		document.cookie="menugauche=none";
    }
    return true;
}
      </script>
      <div class="mainnav">
       <table>
        <tbody>
         <tr>
          <td class="logo" rowspan="2">
           <a href="/" title="accueil">
            <img id="Logo" src="/images/logos/logo-noir-200x143.png"/>
           </a>
          </td>
          <td class="mainitem">
           <a href="/livres/livres.asp" title="Littérature">
            Littérature
           </a>
          </td>
          <td class="mainitem">
           <a href="/articles/default.asp" title="Encyclopédie">
            Encyclopédie
           </a>
          </td>
          <td class="mainitem">
           <a href="/noosfere/heberges.asp" title="Sites hébergés">
            Sites hébergés
           </a>
          </td>
          <td class="mainitem">
           <a href="/actu/evenements.asp" title="Infos">
            Infos &amp; actus
           </a>
          </td>
          <td class="mainitem">
           <a href="/noosfere/assoc/nous_rejoindre.asp" title="Association">
            Association
           </a>
          </td>
          <td align="center">
           <br/>
           <form action="/noosearch_simple.asp" method="post" name="simplesearch">
            <input align="center" class="input_search" name="Mots" onchange="this.submit()" placeholder="recherche..." size="16" type="text"/>
            <br/>
            <a href="/livres/noosearch.asp">
             recherche avancée
            </a>
            |
            <a href="/tags/search_tags.asp">
             par tags
            </a>
           </form>
          </td>
          <td>
           <a href="https://www.facebook.com/nooSFere" target="_Blank">
            <img height="30" src="/images/facebook.png"/>
           </a>
           <!-- <a href="https://twitter.com/noosfere" target="_Blank"><img src="/images/twitter.png" height=30></a>
							&nbsp; -->
           <a href="https://www.instagram.com/noosfere_sf" target="_Blank">
            <img height="30" src="/images/instagram.png"/>
           </a>
           <a href="https://bsky.app/profile/noosfere.bsky.social" target="_Blank">
            <img height="30" src="/images/bluesky-social-logo-png_seeklogo-514621.png"/>
           </a>
          </td>
         </tr>
        </tbody>
       </table>
      </div>
      <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%">
       <tbody>
        <tr>
         <td width="30">
          <div class="bouton" id="bouton_texte" onclick="javascript:afficher_cacher('divmenugauche','divfenetrecentrale');" style="padding-top:1em;padding-left:1em">
           <img height="40" src="/images/menu.png" style="border:2px solid grey;border-radius:5px;" width="40"/>
          </div>
         </td>
         <td class="ficheNiourf" valign="bottom">
         </td>
         <td style="text-align:right;vertical-align:bottom;">
          <span class="ficheNiourf">
           Site clair
				(
           <a href="#" onclick="afficherChoix('/modules/charte/choix/choix.asp?numlivre=2146557876&amp;Tri=3');return false">
            Changer
           </a>
           )
          </span>
         </td>
        </tr>
        <tr>
         <td>
         </td>
        </tr>
       </tbody>
      </table>
      <div id="divmenugauche" style="float:left;width:200px">
       <table border="0" cellpadding="0" cellspacing="0" width="195">
        <tbody>
         <tr>
          <td align="left">
           <table border="0" cellpadding="0" cellspacing="0">
            <tbody>
             <tr>
              <td class="onglet_bleu_bg">
              </td>
              <td class="onglet_bleu">
               Livres
              </td>
              <td class="onglet_bleu_bd">
              </td>
             </tr>
            </tbody>
           </table>
          </td>
         </tr>
         <tr>
          <td>
           <table class="menu_gauche" width="100%">
            <tbody>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/parutions.asp?interv=mois">
                 Parutions mois
                </a>
                /
                <a href="/livres/parutions.asp">
                 année
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/parutions_univ.asp">
                 Parutions universitaires
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/editeurs.asp?Lettre=A">
                 Editeurs
                </a>
                /
                <a href="/livres/actu_coll.asp">
                 Collections
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/series.asp?lettre=A">
                 Séries
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/couv_annees.asp">
                 Couvertures
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/revues.asp">
                 Revues
                </a>
                /
                <a href="/livres/revues.asp?ID_TypeItem=1">
                 Fanzines
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/cyborg_nouvelle.asp">
                 Nouvelles (recherche)
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/tags/search_tags.asp">
                 tags (recherche)
                </a>
               </span>
              </td>
             </tr>
            </tbody>
           </table>
          </td>
         </tr>
         <tr>
          <td>
          </td>
         </tr>
         <tr>
          <td align="left">
           <table border="0" cellpadding="0" cellspacing="0">
            <tbody>
             <tr>
              <td class="onglet_bleu_bg">
              </td>
              <td class="onglet_bleu">
               Critiques
              </td>
              <td class="onglet_bleu_bd">
              </td>
             </tr>
            </tbody>
           </table>
          </td>
         </tr>
         <tr>
          <td>
           <table class="menu_gauche" width="100%">
            <tbody>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/actu_crit.asp">
                 Récentes
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a border="0" href="/livres/auteurscrit.asp">
                 Par auteur
                </a>
                /
                <a href="/livres/critiques.asp">
                 Par titre
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a border="0" href="/livres/critseries.asp">
                 Par série
                </a>
                /
                <a border="0" href="/livres/critrevues.asp">
                 Par revue
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/critsign.asp">
                 Par chroniqueur
                </a>
               </span>
              </td>
             </tr>
            </tbody>
           </table>
          </td>
         </tr>
         <tr>
          <td>
          </td>
         </tr>
         <tr>
          <td align="left">
           <table border="0" cellpadding="0" cellspacing="0">
            <tbody>
             <tr>
              <td class="onglet_bleu_bg">
              </td>
              <td class="onglet_bleu">
               Intervenants
              </td>
              <td class="onglet_bleu_bd">
              </td>
             </tr>
            </tbody>
           </table>
          </td>
         </tr>
         <tr>
          <td>
           <table class="menu_gauche" width="100%">
            <tbody>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/auteurs.asp?Lettre=A&amp;Intervention=1">
                 Auteurs
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/Pays.asp">
                 Auteurs par pays
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/auteurs.asp?Lettre=A&amp;Intervention=2">
                 Traducteurs
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/auteurs.asp?Lettre=A&amp;Intervention=3">
                 Illustrateurs
                </a>
               </span>
              </td>
             </tr>
            </tbody>
           </table>
          </td>
         </tr>
         <tr>
          <td>
          </td>
         </tr>
         <tr>
          <td align="left">
           <table border="0" cellpadding="0" cellspacing="0">
            <tbody>
             <tr>
              <td class="onglet_bleu_bg">
              </td>
              <td class="onglet_bleu">
               Prix littéraires
              </td>
              <td class="onglet_bleu_bd">
              </td>
             </tr>
            </tbody>
           </table>
          </td>
         </tr>
         <tr>
          <td>
           <table class="menu_gauche" width="100%">
            <tbody>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/ListePrix.asp">
                 Liste
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/cyborg_prix.asp">
                 Recherche
                </a>
               </span>
              </td>
             </tr>
            </tbody>
           </table>
          </td>
         </tr>
         <tr>
          <td>
          </td>
         </tr>
         <tr>
          <td align="left">
           <table border="0" cellpadding="0" cellspacing="0">
            <tbody>
             <tr>
              <td class="onglet_bleu_bg">
              </td>
              <td class="onglet_bleu">
               Adaptations
              </td>
              <td class="onglet_bleu_bd">
              </td>
             </tr>
            </tbody>
           </table>
          </td>
         </tr>
         <tr>
          <td>
           <table class="menu_gauche" width="100%">
            <tbody>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/adaptations.asp">
                 Liste
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/rechercheadaptations.asp">
                 Recherche
                </a>
               </span>
              </td>
             </tr>
            </tbody>
           </table>
          </td>
         </tr>
        </tbody>
       </table>
      </div>
      <div id="divfenetrecentrale" style="margin-left:200px;margin-right:10px;">
       <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <tbody>
         <tr>
          <td class="onglet_bleu_bg">
          </td>
          <td class="onglet_bleu">
           Fiche livre
          </td>
          <td class="onglet_bleu_bd">
          </td>
          <td align="right" class="ficheNiourf" width="70%">
           <a href="/membres/login.asp">
            Connexion adhérent
           </a>
          </td>
         </tr>
        </tbody>
       </table>
       <div id="Fiche_livre" style="display:block; visibility:visible;">
        <table class="corps_page" width="100%">
         <tbody>
          <tr>
           <td valign="top">
            <script>
             function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
if (getCookie("menugauche")=="none") {
    document.getElementById("divmenugauche").style.display="none";
    document.getElementById("divfenetrecentrale").style.marginLeft="5px";
}
            </script>
            <div align="center">
             <!-- Corps de la page -->
             <div style="float:right;padding:1em;">
              <script>
               function affichecouv() {
  document.getElementById('couvseule').style.display = 'inline';
  document.getElementById('toutcouvs').style.display = 'none';
  document.cookie="nbimages=1";
}
function affichetout() {
  document.getElementById('couvseule').style.display = 'none';
  document.getElementById('toutcouvs').style.display = 'inline';
  document.cookie="nbimages=2";
}
              </script>
              <!-- 1 : 1, 2 : 2-->
              <div id="couvseule" style="display:inline">
               <a href="https://images.noosfere.org/couv/p/pdf248-1977.jpg">
                <img border="0" height="350" name="couverture" src="https://images.noosfere.org/couv/p/pdf248-1977.jpg" title="Bien après minuit"/>
               </a>
               <br/>
               <a class="sousFicheNiourf" onclick="affichetout()" style="cursor:pointer">
                Afficher toutes les images (2)
               </a>
              </div>
              <div id="toutcouvs" style="display:none">
               <a href="https://images.noosfere.org/couv/p/pdf248-1977.jpg">
                <img border="0" height="350" name="couverture" src="https://images.noosfere.org/couv/p/pdf248-1977.jpg" title="Bien après minuit"/>
               </a>
               <a href="https://images.noosfere.org/couv/p/pdf248-1977-4e.jpg">
                <img border="0" height="350" name="couverture" src="https://images.noosfere.org/couv/p/pdf248-1977-4e.jpg" title="Bien après minuit"/>
               </a>
               <br/>
               <a class="sousFicheNiourf" onclick="affichecouv()" style="cursor:pointer">
                Afficher seulement la couverture
               </a>
              </div>
             </div>
             <div class="sousbloc">
              <style type="text/css">
               .btn {
  background: #3498db;
  background-image: -webkit-linear-gradient(top, #3498db, #2980b9);
  background-image: -moz-linear-gradient(top, #3498db, #2980b9);
  background-image: -ms-linear-gradient(top, #3498db, #2980b9);
  background-image: -o-linear-gradient(top, #3498db, #2980b9);
  background-image: linear-gradient(to bottom, #3498db, #2980b9);
  -webkit-border-radius: 5;
  -moz-border-radius: 5;
  border-radius: 5px;
  font-family: Arial;
  color: #ffffff;
  font-size: 10px;
  padding: 2px;
  text-decoration: none;
}

.btn:visited,link {
  color: #ffffff;
}
              </style>
              <span class="TitreNiourf">
               Bien après minuit
              </span>
              <br/>
              <br/>
              <span class="AuteurNiourf">
               <a href="/livres/auteur.asp?NumAuteur=86">
                Ray BRADBURY
               </a>
               <br/>
              </span>
              <span class="ficheNiourf">
               <br/>
               Titre original :
               <i>
                Long After Midnight, 1976
               </i>
               <br/>
               Première parution :
               <i>
                New York, USA : Alfred A. Knopf, septembre 1976
               </i>
               <a class="btn" href="http://www.isfdb.org/cgi-bin/se.cgi?arg=Long After Midnight&amp;type=Fiction+Titles" style="color:white" target="_blank">
                ISFDB
               </a>
               <br/>
               Traduction de
               <a href="/livres/auteur.asp?NumAuteur=1592">
                Roland DELOUYA
               </a>
               <br/>
               Illustration de
               <a href="/livres/auteur.asp?NumAuteur=1129">
                Stéphane DUMONT
               </a>
               <br/>
               <br/>
               <a href="editeur.asp?numediteur=3521">
                DENOËL
               </a>
               (Paris, France), coll.
               <a href="collection.asp?NumCollection=31&amp;numediteur=3521">
                Présence du futur
               </a>
               <a href="/livres/niourf.asp?numlivre=3461">
                <img <="" alt="précédent dans la collection" img="" src="/images/arrow_left.gif" title="précédent dans la collection"/>
               </a>
               n° 248
               <a href="/livres/niourf.asp?numlivre=3220">
                <img <="" alt="suivant dans la collection" img="" src="/images/arrow_right.gif" title="suivant dans la collection"/>
               </a>
               <br/>
              </span>
              <span class="sousFicheNiourf">
               Dépôt légal :  4ème trimestre 1977
               <br/>
               Première édition
               <br/>
               Recueil de nouvelles, 254 pages, catégorie / prix : 2
               <br/>
               ISBN : néant
               <br/>
               Format : 11,0 x 18,0 cm
               <span style="padding-left:1em" title="Les informations concernant cet ouvrage sont fiables (il est passé entre les mains d'un adhérent de noosfere).">
                ✅
               </span>
               <br/>
               Genre : Imaginaire
              </span>
              <br/>
              <div id="AutresEdition">
               <span class="sousFicheNiourf">
                <a href="EditionsLivre.asp?numitem=464" title="Voir toutes les éditions">
                 Autres éditions
                </a>
               </span>
               <br/>
               <span class="ReuniNiourf">
                <a href="niourf.asp?NumLivre=2146585225">
                 DENOËL, 1979
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146600365">
                 1985
                </a>
                ,
                <a href="niourf.asp?NumLivre=8">
                 1998
                </a>
               </span>
              </div>
              <script>
               function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*for each item in the array...*/
      for (i = 0; i < arr.length; i++) {
        /*check if the item starts with the same letters as the text field value:*/
        /* if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {*/
		if (arr[i].toUpperCase().includes(val.toUpperCase()))	 {
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          /*make the matching letters bold:*/
          // b.innerHTML = "<strong>" + arr[i].substr(, val.length) + "</strong>";
          // b.innerHTML += arr[i].substr(val.length);
          b.innerHTML = arr[i];
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
          /*execute a function when someone clicks on the item value (DIV element):*/
          b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
          });
          a.appendChild(b);
        }
      }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed, prevent the form from being submitted,*/
        e.preventDefault();
        if (currentFocus > -1) {
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
  });
}

/*An array containing all the country names in the world:*/
var countries = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua & Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia & Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Cayman Islands","Central Arfrican Republic","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cuba","Curacao","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kiribati","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Myanmar","Namibia","Nauro","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","North Korea","Norway","Oman","Pakistan","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre & Miquelon","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Korea","South Sudan","Spain","Sri Lanka","St Kitts & Nevis","St Lucia","St Vincent","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad & Tobago","Tunisia","Turkey","Turkmenistan","Turks & Caicos","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States of America","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"];
              </script>
              <script>
               var tags = [ "origine : Afrique du sud", "origine : Albanie", "origine : Algérie", "origine : Allemagne", "origine : Angleterre", "origine : Angola", "origine : Argentine", "origine : Arménie", "origine : Australie", "origine : Autriche", "origine : Bangladesh", "origine : Barbade", "origine : Belgique", "origine : Bolivie", "origine : Bosnie Herzégovine", "origine : Brésil", "origine : Bulgarie", "origine : Cameroun", "origine : Canada", "origine : Chili", "origine : Chine", "origine : Chypre", "origine : Colombie", "origine : Congo", "origine : Corée du sud", "origine : Côte d'Ivoire", "origine : Croatie", "origine : Cuba", "origine : Danemark", "origine : Djibouti", "origine : Écosse", "origine : Égypte", "origine : El Salvador", "origine : Espagne", "origine : Estonie", "origine : États-Unis", "origine : Fidji", "origine : Finlande", "origine : France", "origine : Géorgie", "origine : Grèce", "origine : Grèce antique", "origine : Guatemala", "origine : Guinée", "origine : Guyane", "origine : Haïti", "origine : Hollande", "origine : Hongrie", "origine : Île Maurice", "origine : Inde", "origine : Irak", "origine : Iran", "origine : Irlande", "origine : Islande", "origine : Israel", "origine : Italie", "origine : Jamaïque", "origine : Japon", "origine : Kirghizistan", "origine : Lesotho", "origine : Lettonie", "origine : Liban", "origine : Lituanie", "origine : Luxembourg", "origine : Madagascar", "origine : Malaisie", "origine : Mali", "origine : Maroc", "origine : Mauritanie", "origine : Mexique", "origine : Nigeria", "origine : Norvège", "origine : Nouvelle-Zélande", "origine : Pakistan", "origine : Pays de Galles", "origine : Pays-Bas", "origine : Pérou", "origine : Pologne", "origine : Portugal", "origine : République Dominicaine", "origine : République tchèque", "origine : Rome antique", "origine : Roumanie", "origine : Royaume-Uni", "origine : Russie (U.R.S.S.)", "origine : Sénégal", "origine : Slovénie", "origine : Sri lanka", "origine : Suède", "origine : Suisse", "origine : Taïwan", "origine : Tchécoslovaquie", "origine : Thaïlande", "origine : Trinidad et Tobago", "origine : Tunisie", "origine : Turquie", "origine : Ukraine", "origine : Uruguay", "origine : Vénézuela", "origine : Vietnam", "origine : Yougoslavie", "origine : Zambie", "18e siècle", "19e siècle", "1ère guerre mondiale", "20e siècle", "21e siècle", "2ème guerre mondiale", "abominations lovecraftiennes", "Afrique", "alchimie", "alimentation/cuisine", "Allemagne", "altération de la réalité", "Amérique latine", "amitié", "Amour", "anarchisme", "androïdes", "Angleterre", "animaux", "anneau magique", "ansible", "antiquité", "araignées", "arme", "art", "arthurien", "ascenseur spatial", "Asie", "Australie", "avion", "Belgique", "big dumb objects (bdo)", "biographie", "bit lit", "body horror", "Canada", "capitalisme", "centrale nucléaire", "céphalopodes", "chats", "chiens", "Chine", "climat", "clonage", "colonisation", "Comète", "communisme", "conte", "contemporain", "cosy fantasy", "créatures magiques", "cyberpunk", "dark academia", "dark fantasy", "démocratie", "diables/démons", "dictature", "dieux/déesses", "dinosaures", "dragons", "drogue", "dystopie", "écologie", "Écosse", "Égypte", "elfes", "emprise", "encyclopédie Planète", "enfants", "enfer", "épée magique", "épopée", "espace", "Espagne", "essai", "États-Unis", "ethno-fiction", "étoile à neutrons", "eugénisme", "Europe", "exploration spatiale", "extra-terrestres", "famille", "fantastique", "fantasy", "fantasy urbaine", "fantômes", "fascisme", "fées", "féminisme", "fiction climatique", "film/cinéma", "finalistes du prix Rosny aîné", "folk horror", "France", "futur lointain", "futur proche", "galaxie", "gore", "gothique", "Grèce", "guerre", "habitat/architecture", "hard SF", "heroic fantasy", "high fantasy", "histoire", "histoire du futur", "hopepunk", "horreur", "horreur psychologique", "hors genre", "humain augmenté/cyborg", "humour", "Île", "imaginaire", "immortalité", "Inde", "informatique/internet", "intelligence artificielle", "invasion extraterrestre", "Irak", "Irlande", "Italie", "Japon", "jeu", "jeunesse", "jeux vidéo", "Jupiter", "langage", "licornes", "light fantasy", "litrpg", "littérature/livre", "loups-garous", "low fantasy", "Lune", "lutte des classes", "Machine possédée", "magie", "maison hantée", "maladie mentale/trouble psychique", "maladie/pandémie", "manipulation génétique", "maritime", "Mars", "martiens", "merveilleux scientifique", "métamorphes", "Mexique", "militaire", "monde imaginaire", "mondes virtuels", "Mort", "moyen-âge", "multivers", "musique", "mutants", "mythe", "nains", "Neptune", "new weird", "objet magique", "ours", "pacifisme", "Paradoxe des jumeaux", "piraterie", "planet opera", "Pluton", "pôles", "policier/noir", "portail de téléportation", "post-apocalyptique", "post-exotisme", "pouvoirs psy", "préhistoire", "premier contact", "racisme", "rat", "réalisme magique", "Relativité restreinte", "religion", "relique", "renaissance", "résistance/révolte", "révolution", "robots", "romance", "romantasy", "Russie", "Saturne", "savant fou", "science fantasy", "science-fiction", "sciences", "secte", "sélénites", "serpent", "sexualité", "simulation informatique", "Singe", "singularité", "Sirène", "slasher", "société de surveillance", "solarpunk", "Soleil", "sorciers/sorcières", "sous l'eau", "sous terre", "sous-marin", "space opera", "sphère de Dyson", "spiritisme", "sport", "station spatiale", "steampunk", "supraluminique", "surpopulation", "survivalisme", "système extrasolaire", "système solaire", "technothriller", "télépathie", "temps", "terraformation", "Terre", "terre creuse", "théorie de l'évolution", "train", "transhumanisme", "trou de ver", "uchronie", "univers", "univers parallèles", "utopie", "vaisseau générationnel", "vaisseau spatial", "vampires", "vengeance", "Vénus", "victorien", "ville", "voyage dans le temps", "voyage spatial", "voyage/quête initiatique", "western", "zombies" ];
              </script>
              <style>
               .pad {
	font-size: 12px;
	padding-left:1em;
	padding-right:1em;
}
              </style>
              <script>
               function afficherequete() {
  document.getElementById('historique').style.display = 'inline';
}
              </script>
              <style>
               /*the container must be positioned relative:*/
.autocomplete {
  position: relative;
  display: inline-block;
}

.autocomplete-items {
  position: absolute;
  border: 1px solid #d4d4d4;
  border-bottom: none;
  border-top: none;
  z-index: 99;
  /*position the autocomplete items to be the same width as the container:*/
  top: 100%;
  left: 0;
  right: 0;
}

.autocomplete-items div {
  padding: 2px;
  cursor: pointer;
  background-color: #fff;
  border-bottom: 1px solid #d4d4d4;
}

/*when hovering an item:*/
.autocomplete-items div:hover {
  background-color: #e9e9e9;
}

/*when navigating through the items using the arrow keys:*/
.autocomplete-active {
  background-color: DodgerBlue !important;
  color: #ffffff;
}


.btntag {
  background: #3498db;
  background-image: -webkit-linear-gradient(top, #3498db, #2980b9);
  background-image: -moz-linear-gradient(top, #3498db, #2980b9);
  background-image: -ms-linear-gradient(top, #3498db, #2980b9);
  background-image: -o-linear-gradient(top, #3498db, #2980b9);
  background-image: linear-gradient(to bottom, #3498db, #2980b9);
  -webkit-border-radius: 5;
  -moz-border-radius: 5;
  border-radius: 5px;
  font-family: Arial;
  color: #ffffff;
  font-size: 10px;
  padding: 2px;
  text-decoration: none;
}

.btntag:visited,link {
  color: #ffffff;
}
              </style>
              <link href="/tags/tags.css" rel="stylesheet" type="text/css"/>
              <div>
               <br/>
               <a class="undertag" href="/tags/tag_content.asp?tag=4" title="">
                imaginaire
               </a>
               <a class="undertag" href="/tags/tag_content.asp?tag=139" title="">
                origine :  États-Unis
               </a>
              </div>
              <script>
               autocomplete(document.getElementById("tag"), tags);
              </script>
             </div>
             <div style="clear:right">
              <br/>
              <div class="sousbloc">
               <div style="padding-bottom:0.5em">
                <span class="AuteurNiourf">
                 Quatrième de couverture
                </span>
                <hr style="color:CCC;"/>
               </div>
               <div id="quatrieme">
                <div style="text-align:center">
                 Deux aventuriers, épaves de l'espace, fouillent les villes mortes de Mars en quête du flacon bleu où ils boiront leur destin...
                </div>
                <div style="text-align:center">
                 Dans un quartier miteux de New York, en pleine canicule, un employé de bureau rencontre une sorcière qui lui propose l'échange classique, le bonheur ici-bas contre son âme. Sera-t-il assez fou pour refuser... ?
                </div>
                <div style="text-align:center">
                 Un magnat de l'avenir cherche un écrivain au souffle assez puissant pourr décrire la grande épopée des voyages interstellaires.
                </div>
                <div style="text-align:center">
                 Il le trouve au XX
                 <sup>
                  e
                 </sup>
                 siècle et l'arrache à son lit de mort, mais il faut bien que Thomas Wolfe meure un jour...
                </div>
                <div style="text-align:center">
                 De la tendresse et de la nostalgie qui faisaient le charme des
                 <u>
                  Chroniques martiennes
                 </u>
                 à la satire brillante, tout l'univers de Ray Bradbury dans ce recueil de nouvelles, le premier depuis six ans.
                </div>
                <div style="text-align:center">
                </div>
                <div style="text-align:center">
                 <u>
                  L'auteur
                 </u>
                </div>
                <div style="text-align:center">
                 Né en 1920, à Waukegan. Sa famille émigre à Los Angeles en 1934. Après avoir terminé ses études en 1938, il gagne sa vie en vendant des journaux tout en commençant à écrire. Publie son premier conte en 1940. A également écrit des scénarios pour le cinéma, dont celui de
                 <u>
                  Moby Dick
                 </u>
                 d'après l'œuvre de Herman Melville, et des pièces de théâtres. François Truffaut a porté avec succès à l'écran
                 <u>
                  Fahrenheit 451
                 </u>
                 .
                </div>
               </div>
              </div>
              <div class="sousbloc">
               <div style="padding-bottom:0.5em">
                <span class="AuteurNiourf">
                 Sommaire
                </span>
                <hr style="color:CCC;"/>
               </div>
               <span class="sousFicheNiourf" style="padding:1em">
                <a href="?numlivre=2146557876&amp;somcomplet=1#sommaire">
                 Afficher les différentes éditions des textes
                </a>
                <br/>
               </span>
               <div id="sommaire" style="padding-top:1em">
                <span class="ficheNiourf">
                 1 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=1951">
                  Le Flacon bleu
                 </a>
                 <i>
                  (The Blue Bottle / Death Wish, 1950)
                 </i>
                 , pages 11 à 25, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1592">
                  Roland DELOUYA
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 2 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=3980">
                  Un printemps hors du temps
                 </a>
                 <i>
                  (One Timeless Spring, 1946)
                 </i>
                 , pages 27 à 38, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1592">
                  Roland DELOUYA
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 3 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=3700">
                  Le Perroquet qui avait connu papa
                 </a>
                 <i>
                  (The Parrot Who Met Papa, 1972)
                 </i>
                 , pages 39 à 59, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1592">
                  Roland DELOUYA
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 4 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=2296">
                  L'Homme brûlant
                 </a>
                 <i>
                  (The Burning Man, 1975)
                 </i>
                 , pages 61 à 71, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1592">
                  Roland DELOUYA
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 5 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=3213">
                  Un morceau de bois
                 </a>
                 <i>
                  (A Piece of Wood, 1952)
                 </i>
                 , pages 73 à 80, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1592">
                  Roland DELOUYA
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 6 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=26731">
                  Le Messie
                 </a>
                 <i>
                  (The Messiah, 1973)
                 </i>
                 , pages 81 à 95, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1592">
                  Roland DELOUYA
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 7 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=2034">
                  G.B.S. modèle V
                 </a>
                 <i>
                  (G.B.S. - Mark V, 1976)
                 </i>
                 , pages 97 à 112, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1592">
                  Roland DELOUYA
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 8 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=554">
                  Boire en une fois : contre la fureur des foules
                 </a>
                 <i>
                  (Drink Entire: Against the Madness of Crowds, 1976)
                 </i>
                 , pages 113 à 131, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1592">
                  Roland DELOUYA
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 9 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=2511">
                  Intermède au soleil
                 </a>
                 <i>
                  (Interval in Sunlight, 1954)
                 </i>
                 , pages 133 à 171, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1592">
                  Roland DELOUYA
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 10 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=51">
                  A jamais la Terre
                 </a>
                 <i>
                  (Forever and the Earth, 1950)
                 </i>
                 , pages 173 à 197, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1592">
                  Roland DELOUYA
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 11 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=3112">
                  Les Miracles de Jamie
                 </a>
                 <i>
                  (The Miracles of Jamie, 1946)
                 </i>
                 , pages 199 à 211, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1592">
                  Roland DELOUYA
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 12 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=2587">
                  Le Jeu d'octobre
                 </a>
                 <i>
                  (The October Game, 1948)
                 </i>
                 , pages 213 à 224, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1592">
                  Roland DELOUYA
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 13 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=526">
                  Bien après minuit
                 </a>
                 <i>
                  (Long After Midnight, 1976)
                 </i>
                 , pages 225 à 233, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1592">
                  Roland DELOUYA
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 14 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=4819">
                  La Tablette de chocolat
                 </a>
                 <i>
                  (Have I Got a Chocolate Bar for You!, 1973)
                 </i>
                 , pages 235 à 251, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1592">
                  Roland DELOUYA
                 </a>
                </span>
                <br/>
               </div>
              </div>
              <div class="sousbloc">
               <div style="padding-bottom:0.5em">
                <span class="AuteurNiourf">
                 Critiques
                </span>
                <hr style="color:CCC;"/>
               </div>
               <div id="critique">
                <div align="right">
                 [critique des livres suivants :
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=3461">
                  Philip Goy - Vers la révolution
                 </a>
                 ;
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=2146557881">
                  A. et B. Strougatski - Un gars de l'enfer
                 </a>
                 ;
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=137">
                  F. et G. Hoyle - Au plus profond de l'espace
                 </a>
                 ;
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=2146557876">
                  Ray Bradbury - Bien après minuit
                 </a>
                 ;
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=601416355">
                  Yves frémion - Octobre, Octobres
                 </a>
                 ;
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=-320880">
                  Thomas Disch - Génocides
                 </a>
                 ]
                </div>
                <div align="right">
                 Note nooSFere
                </div>
                <br/>
                <br/>
                <div align="justify">
                 <b>
                  KIERKEGAARD ET PAPA SUR 27 MEGAHERTZ
                 </b>
                </div>
                <div align="justify">
                 <b>
                  (et nos invités étrangers)
                 </b>
                </div>
                <br/>
                <div align="justify">
                 27 mégahertz, c'est la fréquence des radioamateurs. « Nos Bouvard et Pécuchet transistorisés », comme les appelle Philip Goy. Ce n'est pas vraiment une nouvelle, mais une sorte de pièce radiophonique en 5 scènes,
                 <i>
                  QSO sur 27 mégahertz
                 </i>
                 . Avec
                 <i>
                  Larzac
                 </i>
                 , le meilleur texte du recueil de Philip Goy,
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=3461">
                  <i>
                   Vers la révolution
                  </i>
                 </a>
                 .
                </div>
                <div align="justify">
                 Kierkegaard, Je ne vous le présenterai pas, chers amis. Votre culture vaut bien la mienne (ce qui n'est pas forcément une référence). C'est à son plus célèbre livre,
                 <i>
                  Traité du désespoir
                 </i>
                 , que Frémion fait allusion dans une nouvelle admirable,
                 <i>
                  Toréador prends garde à l'œil noir de Kierkegaard !
                 </i>
                 ... la meilleure d'un recueil intéressant et riche,
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=601416355">
                  <i>
                   Octobre, octobres
                  </i>
                 </a>
                 .
                </div>
                <div align="justify">
                 Papa, tout le monde le sait (votre culture, etc.), c'est Hemingway, héros posthume de la nouvelle
                 <i>
                  Le perroquet qui avait connu Papa
                 </i>
                 , dans le recueil de Ray Bradbury,
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=2146557876">
                  <i>
                   Bien après minuit
                  </i>
                 </a>
                 Recueil de bric et de broc avec quelques traces de brac...
                </div>
                <div align="justify">
                 Nos autres invités étrangers sont les frères Strougatski pour l'Union dite soviétique, papa Hoyle bon pied bon œil et son fiston, pour l'Angleterre et la hard science réunies, et Thomas Disch, qui est un peu à l'Amérique ce que les Strougatski sont à la Russie.
                </div>
                <div align="justify">
                 Et maintenant QSO !
                </div>
                <br/>
                <div align="justify">
                 Grosse offensive de la nouvelle, chez les Français en particulier. Chefs de V, Elisabeth Gille et Bernard Blanc (les écrivains de science-fiction, comme les grues et les canards sauvages, volent en formation triangulaire...). Et on dit que Jacques Goimard est en train de rassembler quelques beaux volatiles. Après avoir lu Goy, Frémion et les Frenchies de
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=1254108530">
                  <i>
                   Retour à la Terre 3
                  </i>
                 </a>
                 (surtout J.-P. Andrevon, Christine Renard et Daniel Phi), J'avoue que je trouve les Anglo-saxophones un peu pâlichons, en ce moment. (Mais je sais bien que pour beaucoup de lecteurs, la science-fiction est un liquide incolore et inodore !)
                </div>
                <div align="justify">
                 Daniel Riche écrivait dans son éditorial de FICTION n° 284, à propos du film
                 <i>
                  La guerre des étoiles
                 </i>
                 : «
                 <i>
                  Lucas semble avoir compris la vanité de l'allégorie. Son film n'est porteur d'aucun message. C'est de la S.F. pour la S.F., un voyage aux confins de l'imaginaire, sans autre prétention que le plaisir du spectateur. Avec lui, la science-fiction cinématographique entre dans l'Age adulte, celui où elle peut enfin s'assumer seule.
                 </i>
                 » Mon vieux, ça c'est un manifeste, hé, hé. Pourquoi ? Pourquoi pas ?
                </div>
                <div align="justify">
                 Dans le numéro
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=1626711732">
                  1 d'
                  <i>
                   ALERTE !
                  </i>
                 </a>
                 <i>
                 </i>
                 — la revue de Kesselring et Bernard Blanc — Yves Frémion annonce carrément sa couleur : «
                 <i>
                  Je ne suis pas de la SF (j'ai pas ma carte). Je ne fais pas de LA SF. Je me SERS de la SF, parce que c'est à la mode et que ça marche. La SF, je n'en ai rien à foutre, rien de plus que la BD ou du bouddhisme zen...
                 </i>
                 » Hé bé, ça serait un autre manifeste que ça ne m'étonnerait pas ! Pourquoi donc ? Pourquoi pas ?
                </div>
                <div align="justify">
                 Chacun occupe son terrain. Les deux thèses sont plus conciliables qu'on le croit. Je pense avec Daniel Riche que la SF a sa spécificité et que l'imaginaire a sa fonction (mais qu'est-ce que l'imaginaire ?). Avec Frémion, je crois aussi qu'elle est un outil, et je m'en sers. En tout cas, il y a place (même dans une seule tête) pour une SF d'imagination pure et pour une politique-fiction, plus ou moins engagée.
                </div>
                <div align="justify">
                 Et l'essentiel, c'est qu'on ait de bons livres.
                </div>
                <div align="justify">
                 Philip Goy écrit dans
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=-68692034">
                  Opus n° 64 (spécial science-fiction)
                 </a>
                 : «
                 <i>
                  La science est à la science-fiction ce que la photo est à la peinture.
                 </i>
                 » Philip Goy est sûrement un bon photographe. C'est aussi un excellent peintre qui manie habilement tous les genres.
                 <i>
                  Larzac
                 </i>
                 appartient presque au réalisme socialiste.
                 <i>
                  QSO sur 27 mégahertz
                 </i>
                 , c'est de la bande dessinée avec beaucoup de bulles. Un peu comme Lauzier. Un but dans l'existence relève du fantastique moderne, psychologique et onirique.
                 <i>
                  Camés
                 </i>
                 est de l'affiche et
                 <i>
                  Vers la révolution
                 </i>
                 de l'illustration satirique...
                </div>
                <div align="justify">
                 L'auteur jette sur la couverture (d'un beau rouge brun de sang séché, plus claire en bas : une croûte fraîche sur la plaie d'un vieux guerrier...) son propre manifeste. «
                 <i>
                  Une maladie : La SF est souvent un véhicule de la domination culturelle anglo-américaine. Un remède : Ce livre. Un manifeste pour une nouvelle SF — Feu sur les OVNI ! — Extraterrestres go home ! — Mort aux Grands Initiés ! — Les fusées au cimetière !
                 </i>
                 »
                </div>
                <div align="justify">
                 La plus étonnante manifestation du manifeste est manifestement
                 <i>
                  QSO
                 </i>
                 , une conversation hilarante de quelques radios amateurs sur... les OVNI, les Extraterrestres, les civilisations disparues, les grands initiés, etc. Philip Goy connaît admirablement la technique, les mœurs et le langage de ces braves gens. Il en tire une grande crédibilité, un impact satirique inégalé dans le genre. Je n'ai jamais lu une charge plus drôle contre la philosophie de bazar qui enveloppe beaucoup d'énigmes à quatre sous (et peut-être en même temps quelques vrais mystères). L'effet d'exotisme provoqué par le langage des radios — langage codé mais bien réel et bien actuel — fait passer la pilule tout en créant une sorte de tension, d'excitation mentale qui est bien celle de la science-fiction. C'est amusant, c'est instructif, c'est presque... ah, génial ? H.l. ! H.l. trois fois !
                </div>
                <div align="justify">
                 <i>
                  Larzac
                 </i>
                 raconte l'aventure d'une bergère et d'un polytechnicien sur un plateau célèbre. En fait, les vraies vedettes de cette histoire sont les brebis et les béliers. Avec l'insémination artificielle pour la hard science (ne pas confondre Central Intelligence Agency et Centre d'insémination artificielle !). Révélation : la nouvelle SF que souhaite Philip Goy, on la connaissait déjà, et on l'aimait bien. C'est la littérature générale, que Frémion égratigne aussi bien dans son article d'Alerte ! (mais Frémion est méchant, et il n'avait pas lu Goy à ce moment).
                </div>
                <div align="justify">
                 En fait, la seule nouvelle de
                 <i>
                  Vers la révolution
                 </i>
                 qui se rattache un peu à la science-fiction, avec un « second degré » très barry-malzbergien, c'est
                 <i>
                  Un but dans l'existence
                 </i>
                 . Un bon texte, mais pour moi ça ne vaut pas
                 <i>
                  Larzac
                 </i>
                 . Mea culpa : je suis de ceux qui s'intéressent plus au Larzac qu'aux voyages dans l'espace.
                </div>
                <div align="justify">
                 En tout cas. Je ne suis pas du tout gêné par cette quasi absence de la SF dans un livre de la collection Présence du futur. De toute façon, le futur est terriblement présent dans le présent que nous décrit Philip Goy. On ne peut même pas accuser l'auteur de « se servir » de la SF, ce qui est un crime sans nom aux yeux des fans-fans. Il se sert de la réalité, comme la science-fiction sait le faire, parfois, dans ses rares réussites. Naturellement, s'il veut toucher un jour le grand public qu'il mérite et connaître la notoriété dont il se fout (mais enfin), il sera peut-être obligé de quitter l'étiquette dont il joue avec art et humour.
                </div>
                <div align="justify">
                 Deux réserves mineures : la farce est parfois grosse et un coup d'estompe serait alors bienvenu. Et les points d'exclamation n'ajoutent rien à une réalité qui crie d'elle-même. Surtout quand ils vont trois par trois. Yves Frémion, lui, n'hésite pas à plonger corps et âme dans cette science-fiction qu'il vomit. Et le résultat est souvent très bon. C'est la vie. On pourrait faire la même remarque à propos de Frémion et de la littérature générale (qui tombe rarement, Yves, dans ce que tu appelles le « bigeardisme » !). Autrement dit, ce diable d'homme réussit deux fois son coup. Ce n'est pas courant. Et si Frémion n'a « rien à foutre de la SF », on peut dire après avoir lu
                 <i>
                  Toréador prends garde A l'œil noir de Kierkegaard
                 </i>
                 que la SF a besoin de Frémion. La littérature aussi — Bigeard me pardonne.
                </div>
                <div align="justify">
                 <i>
                  Octobre, octobres
                 </i>
                 , avec une très belle couverture de Jean-François Jamoul, sur laquelle l'œil noir de Kierkegaard vous regarde du fond du ciel bleu. Tant qu'il y a du ciel bleu, il y a de l'espoir : allez donc vous en acheter quelques kilomètres carrés avec vos indemnités de chômage ! La palette de Frémion est aussi large que celle de Goy. Et il y a d'ailleurs une incontestable parenté spirituelle entre ces deux auteurs. On trouve dans Octobre plusieurs contes fantastiques et/ou érotiques, des satires politiques et/ou sociales, un poème en prose et quelques autres choses. Notamment, une préface de Marcel B. Cachin-Blanc, en provenance d'un univers parallèle. Et puis, et surtout cette très belle nouvelle que j'ai déjà mentionnée :
                 <i>
                  Toréador...
                 </i>
                 Pour les fanatiques de la SF anglo-américaine, disons que ce texte ne déparerait pas un recueil comme
                 <i>
                  Espaces Inhabitables
                 </i>
                 (anthologie d'Alain Dorémieux, aux Editions Casterman). Norman Spinrad aurait bien aimé l'écrire. Le thème est classique, c'est celui de
                 <i>
                  Farenheit 451
                 </i>
                 , mais renouvelé de façon admirable. L'imaginaire se suffit-il à lui-même ? Peut-être. Il ne manque pas ici, mais il est mis au service de la réalité, ce qui me semble la définition de toute littérature (digne de ce nom).
                </div>
                <div align="justify">
                 A côté — c'est purement subjectif, d'accord — l'imaginaire suspendu dans le vide, comme ce vaisseau spatial qui fait rigoler Philip Goy, ne pèse pas tellement lourd, sauf en dollars. Mais enfin, on ne va pas se battre pour ça. Et j'aime aussi la SF de pur divertissement.
                </div>
                <div align="justify">
                 <i>
                  Petite mort petite amie
                 </i>
                 est un conte de science-fiction doux-amer.
                 <i>
                  Il est plus de midi et le boulanger n'est pas encore passé
                 </i>
                 est une fin du monde en douceur, autre spécialité anglo-saxonne. La sensibilité de Frémion apporte une note personnelle assez rare. L'ambiguïté de la fin nourrit une angoisse à long terme. Une nouvelle de SF qui aurait pu être écrite par un grand auteur de littérature générale (pas Bigeard !) : c'est rare aussi.
                 <i>
                  Vivre s'entend, mort... Jouir sans entrailles
                 </i>
                 est un beau conte cruel, Accoutumance une nouvelle presque classique.
                 <i>
                  L'Humanité, dimanche
                 </i>
                 relève de la politique-fiction satirique, avec un ton très « nouveau philosophe » (c'est un compliment, eh !). Le recueil s'achève sur une histoire brève, inclassable, qui lui donne son titre. En quelques pages, un souffle passe, épique et chargé d'un nouvel espoir, froid et sec, au-delà du désespoir à l'œil noir. Politique ? Pas au sens où l'on entend, d'ordinaire, le mot : poétique et populiste.
                </div>
                <div align="justify">
                 Une autre vole. «
                 <i>
                  C'est nous qui allons créer ce vent d'octobre. C'est nous qui serons le vent
                 </i>
                 , » (p. 171).
                </div>
                <div align="justify">
                 Frémion, êtes-vous un violent ? Non, c'est un journaliste qui a posé la question à Michel Le Bris, l'ancien animateur de la Gauche prolétarienne et l'admirable écrivain de
                 <i>
                  L'homme aux semelles de vent
                 </i>
                 Et Michel Le Bris a répondu : Je suis un tendre poussé par une grande colère. Ou quelque chose comme ça. Tout le portrait de Frémion.
                </div>
                <div align="justify">
                 <i>
                  Octobre, octobres
                 </i>
                 est le troisième livre de la collection de Bernard Blanc, après
                 <i>
                  Ciel lourd béton froid
                 </i>
                 , anthologie du jeune chef en personne,
                 <i>
                  Planète socialiste
                 </i>
                 (la plus critiquée, ah, ah !), de votre humble serviteur. Le quatrième volume, c'est
                 <i>
                  Alerte !
                 </i>
                 Frémion, Walther et même Jeury y fulminent sur deux cent mille mégahertz. Et il y a des nouvelles de Joëlle Wintrebert, Pelot, Durand, Hubert, Benoît-Jeannin... j'en oublie sûrement. Mais pas d'anglo-saxophones !
                </div>
                <div align="justify">
                 Et bientôt :
                 <i>
                  Quatre milliards de soldats
                 </i>
                 , de B.B., puis
                 <i>
                  Paranopolis
                 </i>
                 , de Jean Bonnefoy.
                </div>
                <div align="justify">
                 Honnêtement, je souhaite de tout cœur que les lecteurs suivent. Afin que Goy ne soit pas le seul remède contre la domination culturelle de la bande à Carter. Go !
                </div>
                <div align="justify">
                 Je reviens à Yves Frémion pour citer le titre d'une de ces nouvelles (en fait, une sorte de poème, difficile et beau) :
                 <i>
                  Elizabeth qui me parle et rit et s'effondre sur mon épaule...
                 </i>
                 Je ne pense pas qu'il s'agisse d'Elisabeth Gille, mais je dédie ce texte à la directrice de Présence du futur, puisque les choix de Daniel Riche, ou n'importe quel autre hasard, me vouent largement à cette collection. La dernière livraison Denoël n'était pas mauvaise du tout. Pour moi, certes, le grand livre de l'été (même s'il est paru au printemps), et tout compte fait et refait, le grand livre de l'année, c'est
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=-317522">
                  <i>
                   Le désert du monde
                  </i>
                 </a>
                 , de Jean-Pierre Andrevon. En refaisant mes comptes, je m'aperçois aussi que
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=2146557579">
                  <i>
                   Noo
                  </i>
                 </a>
                 , le double roman de Stefan Wul, qui m'avait agacé à première lecture, est un livre riche, merveilleusement écrit : une réussite de la collection (et, bon, ça marche très fort). A signaler aussi, toujours en Présence du futur, la très belle anthologie de Maxim Jakubowski,
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=-327050">
                  <i>
                   Galaxies intérieures
                  </i>
                 </a>
                 , un roman excitant et drôle de Michael Moorcock,
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=-326094">
                  <i>
                   Les terres creuses
                  </i>
                 </a>
                 ... Et, naturellement,
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=1254108530">
                  <i>
                   Retour à la Terre 3
                  </i>
                 </a>
                 <i>
                 </i>
                 du Grand Drevon.
                </div>
                <div align="justify">
                 Parmi les livres à venir, un très grand roman dans lequel Dominique Douay donne toute sa mesure :
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=3220">
                  <i>
                   Strates
                  </i>
                 </a>
                 .
                </div>
                <div align="justify">
                 Au menu du jour : Bradbury, Strougatski A et B et la Hoyle's family.
                </div>
                <div align="justify">
                 Bradbury, c'est Bradbury. Je n'ai jamais été très emballé par cet écrivain. Lorsque Gérard Klein a publié
                 <i>
                  Les perles du temps
                 </i>
                 , on a signalé -c'est une manie des amateurs français de SF — une similitude d'inspiration avec les nouvelles de Bradbury. J'ai tout de suite pensé que Gérard Klein était bien meilleur. Et c'est vrai. C'est même vrai des toutes premières nouvelles du jeune Klein. Quelques années plus tard, G.K. a prouvé, notamment dans
                 <i>
                  La loi du talion
                 </i>
                 , un talent très supérieur è celui de Ray Bradbury.
                </div>
                <div align="justify">
                 Je parle de science-fiction. Car Bradbury, s'il est souvent médiocre à l'intérieur du genre, est parfois admirable quand il en sort. Dans le présent recueil,
                 <i>
                  Bien après minuit
                 </i>
                 il en sort souvent, et c'est une chance. Dommage quand même que des écrivains comme Disch ou Bradbury soient (ou se croient) obligés de faire de la SF. Enfin, c'est la vie. Faut la gagner.
                </div>
                <div align="justify">
                 Je préfère, et de loin, la troisième de ces quatorze nouvelles.
                 <i>
                  Le perroquet qui avait connu Papa
                 </i>
                 . J'en ai déjà parlé. En quelques lignes, Bradbury crée une atmosphère très « Hemingway », très « avant-garde culturelle » américaine, séduisante par sa xénophilie qui s'oppose fortement à la rugosité xénophobe des auteurs de SF américains... J'ai écrit « de très loin » ? Non, j'aime aussi beaucoup
                 <i>
                  Un printemps hors du temps
                 </i>
                 , texte mince mais génial et poignant.
                </div>
                <div align="justify">
                 Mon choix parmi les nouvelles fantastiques :
                 <i>
                  L'homme brûlant
                 </i>
                 . Parmi les nouvelles de science-fiction (plutôt faibles dans l'ensemble) :
                 <i>
                  A jamais la Terre
                 </i>
                 , où l'on voit des voyageurs temporels aller quérir un
                 <i>
                  Maître du passé
                 </i>
                 , Thomas Wolfe, pour lui faire écrire l'épopée interstellaire du XXII
                 <sup>
                  e
                 </sup>
                 siècle. Epopée, mon œil noir ! comme dirait Frémion. Bradbury n'y croit pas plus que nous ; enfin, ça se lit.
                </div>
                <div align="justify">
                 La variété du recueil lui donne finalement une bonne part de son intérêt. C'est de la littérature générale vivante et bien faite, avec une forte touche de fantastique et un peu de science-fiction. Agréable, dans le genre livre de chevet pour quelque temps. A raison d'une nouvelle par soirée, on peut en venir à bout en une quinzaine de jours. On éprouve alors un vague regret d'avoir déjà fini.
                </div>
                <div align="justify">
                 Les Hoyle, c'est de la hard science. Le genre est une chasse gardée anglo-américaine. Une de plus. Un roman extraordinaire
                 <i>
                  Quand les deux soleils se coucheront
                 </i>
                 , de Jan de Fast (Fleuve Noir) est passé complètement inaperçu, parce qu'il était signé par un Français. Ma méfiance vis-à-vis de cette hard science vient surtout de ce fait : plus que toute autre forme de science-fiction, elle est « le véhicule de la domination culturelle anglo-américaine » (comme il est froidement écrit, c'est pas moi qui le dis, sur la jaquette au livre de Philip Goy,
                 <i>
                  Vers la révolution
                 </i>
                 ). A part ça, je ne suis pas contre de temps en temps.
                </div>
                <div align="justify">
                 Ces livres sont souvent très distrayants. C'est le cas du roman de Fred et Geoffroy Hoyle,
                 <i>
                  Au plus profond de l'espace
                 </i>
                 . Il y a une guerre entre la Terre et les Yéla. Cette guerre, il faut la dire, apparaît seulement en toile de fond. Elle est pour ainsi dire finie quand l'histoire commence. Ce roman n'est pas un space-opera belliqueux... Les Yéla ont été repoussés. Les Terriens les poursuivent. Le héros, Dick Warboy, part à la chasse en compagnie de ses amis extraterrestres, Rigel, Alcyone et Achernard, Ils rencontrent un vaisseau yéla qui semble en perdition et ils le prennent en remorque. Mais tel est remorqué qui croyait remorquer. C'est assez drôle et superbement amené et décrit. Tout le récit est basé sur l'affrontement de la nature hostile, ô combien, sous forme du vide sidéral, et la présence constante du mystère. Que font les Yéla ? Où vont-ils ? Que se passe-t-il à l'extérieur ? Où sommes-nous ? Tension, suspense : la hard science fonctionne comme le policier. Les Hoyle dosent habilement l'action, l'énigme et l'atmosphère, comme peu d'auteurs policiers y parviennent. Le décor extérieur, c'est-à-dire l'espace, est décrit avec précision et lyrisme. «
                 <i>
                  Nous flottions maintenant dans un monde de lumière vive, une lumière qui brillait à faire mal et qui couvrait la portion du ciel dans laquelle s'était trouvé le vaisseau yéla. La tache lumineuse s'étendit rapidement jusqu'à couvrir tout la ciel en direction de notre propre navire. Puis elle fut partout Nous continuâmes à flotter et à tourner sur nous-mêmes au sain d'une luminescence totale. Je réalisai que j'étais plongé dans un immense fleuve de gaz en mouvement et je compris enfin que las Yéla avaient été désintégrés,
                 </i>
                 » (p. 158). Qui a fait le coup ? On ne le saura jamais. C'est assez émouvant : on commençait à les aimer, ces Yéla.
                </div>
                <div align="justify">
                 En tout cas, Fred et Geoffroy Hoyle, astronomes connus, sont de bons auteurs de science-fiction. Leurs connaissances scientifiques pimentent la sauce et scellent la crédibilité. On a vraiment confiance. On n'hésiterait pas à monter dans le métro de Londres avec eux s'ils affirmaient que c'est sans danger. Ce n'est pas vraiment de leur faute si la fin merde un peu. D'ailleurs, c'est plutôt sympathique de se retrouver dans un univers dickien, avec tant de physique et tant d'astronomie.
                </div>
                <div align="justify">
                 J'ai lu le roman des frères Strougatski le jour où l'on donnait le Goncourt à Didier Decoin.
                 <i>
                  John l'Enfer
                 </i>
                 , un très beau livre qui frôle parfois la science-fiction.
                 <i>
                  Un gars de l'enfer
                 </i>
                 : un court roman, agréable et intéressant, jamais ennuyeux, à la fois très clair, très simple et très hermétique. Très clair et très simple : c'est l'histoire d'un brave soldat d'une lointaine planète. Pris dans un combat atroce, perdu, et déjà pour ainsi dire mort, il est sauvé par les grands galactiques ou leurs proches cousins, bref les classiques représentants de la « technologie avancée ». Gag — c'en est pas un, c'est un prénom russe, quelque chose comme un diminutif de Gagarine — se voit installé dans un monde merveilleux par son sauveur, Korneï. Un monde merveilleux, tel qu'Albert Ducrocq pourrait l'imaginer chez nous. Impossible de dire si les Strougatski se moquent prudemment ou y croient un peu. Quoi qu'il en soit, Gag ne peut s'adapter au paradis et, à force d'insistance, il réussit à se faire reconduire dans son enfer.
                </div>
                <div align="justify">
                 Gag est un personnage abominable, un « chat guerrier ». tueur, tortionnaire et j'en passe. L'exploit des auteurs est d'avoir rendu crédible et sympathique — ou presque — quelqu'un qui se situe de toute évidence aux antipodes de leur sensibilité. Un tour de force d'ailleurs typique de la littérature russe. Mais les Strougatski sa servent ici de la science-fiction dans un but mystérieux. C'est leur propos qui est hermétique. Sachant qui ils sont et d'où ils sont, ces gars, on ne peut s'empocher de penser que Gag rime avec goulag et de se poser quelques questions.
                </div>
                <div align="justify">
                 Une préface nous aurait peut-être aidés. La traductrice, Bernadette du Crest, qui a fait du bon boulot, a peut-être des nouvelles fraîches de par là-bas ?
                </div>
                <div align="justify">
                 <i>
                  Génocides
                 </i>
                 , importante réédition, dans Ailleurs et demain classiques, nous est livrée avec une passionnante postface de Philippe Curval. Une postface se lit toujours avant le livre : c'est pour ça qu'on la met à la fin. C'est une préface qui tire au lieu d'être une préface qui pousse. Celle de Philippe Curval tire bien (d'ailleurs tout le monde sait que Curval est une locomotive de la science-fiction !) et le roman a presque de la peine à suivre. Voici, présentée en deux phrases, sur la jaquette, cette histoire d'une belle simplicité : «
                 <i>
                  Un jour, la Terre devint un champ pour des semences venues d'ailleurs. Et les humains se trouvèrent réduits, presque le temps d'une saison, à l'état d'insectes invisibles.
                 </i>
                 » Et l'on suit, le temps d'une saison, c'est classique, les derniers survivants de l'espace américaine (euh, humaine), la famille Anderson, Orville, Blossom, Buddy et quelques autres. Le ton et l'atmosphère sont très faulknériens. Parfois presque bibliques... Et la fameuse plante, que les envahisseurs terrestres utilisent comme arme de conquête, ressemble beaucoup à une malédiction divine. C'est particulièrement frappant dans un long dialogue (p. 63-65) au cours duquel la jeune Blossom décrit au rescapé Orville la situation et la vie de la communauté. On se prend parfois à rêver au roman que Disch aurait pu écrire sans les Extraterrestres. Ces Extraterrestres que l'on oublie souvent, d'ailleurs, durant de longues pages...
                </div>
                <div align="justify">
                 Biblique et faulknérienne aussi, la scène de cannibalisme domestique, p. 76 a 80. Et voici la vache Gracie en train de vêler (p. 90) : «
                 <i>
                  Elle émettait de petits grognements porcins. Elle se roulait et se tordait sur le sol. C'était son premier veau, et elle n'était pas tellement large. Ce ne serait pas facile. Neil fit un nœud coulant à une corde et la lui passa autour du cou. Mais elle ruait tellement qu'il ne put lui attacher las panes, et il la laissa comme ça. Alice vint à son secours, mais il aurait préféré que son père fût là. Gracie beuglait comme un taureau maintenant.
                 </i>
                 »
                </div>
                <div align="justify">
                 Belle simplicité, ton chrétien. Les références religieuses abondent, explicites ou non. Thomas l'Incrédule est en réalité un chrétien qui a perdu l'espérance. Chrétien est son pessimisme froid. Ce n'est pas une exploitation, c'est une constatation.
                </div>
                <div align="justify">
                 La science-fiction, dans
                 <i>
                  Génocides
                 </i>
                 , c'est la Plante.
                </div>
                <div align="justify">
                 «
                 <i>
                  La plante était admirable d'efficacité. En fait de végétal, elle était imbattable. (...) Prenez ses racines, par exemple. Elles étaient creuses
                 </i>
                 », (p. 127).
                </div>
                <div align="justify">
                 «
                 <i>
                  Mais l'efficacité véritable de la Plante résidait surtout dans le fait qu'elle constituait un organisme unique. (...) Le mécanisme par lequel avait eu lieu la collectivisation des Plantes individuelles était d'une très grande simplicité. Dés que les racines principales se ramifiaient en racines secondaires, celles ci étaient attirées, par une sorte de tropisme réciproque, vers les racines sœurs les plus proches. Lorsqu'elles se rencontraient, elles opéraient la jonction,
                 </i>
                 » (p. 128).
                </div>
                <div align="justify">
                 On l'a compris, la Plante, c'est le glaive de Dieu. Les Extraterrestres ne sont là que pour faire semblant. D'ailleurs, ils y sont à peine.
                 <i>
                  Génocides
                 </i>
                 n'est pas écrit comme un récit de science-fiction, mais comme n'importe quelle grande œuvre classique du mainstream américain. On pourrait évoquer à ce propos les plus grands noms.
                </div>
                <div align="justify">
                 En réalité, donc, les hommes ne sont pas exterminés par des envahisseurs. C'est le légitime propriétaire de la Terre qui reprend possession de son bien. L'humanité mauvaise le lui avait arraché : elle n'a que ce qu'elle mérite. Et c'est cette conviction profonde — peut-être inconsciente — qui explique le ton extraordinairement serein de Disch. Il n'arrive que ce qui devait arriver, et qui était écrit de toute éternité.
                </div>
                <div align="justify">
                 Naturellement, le livre s'achève sur une citation biblique. «
                 <i>
                  Voyez, la lune même n'est pas brillante, et les étoiles ne sont pas pures à ses yeux. Combien moins l'homme, qui n'est qu'un ver, et le fils de l'homme qui n'est qu'un vermisseau !
                 </i>
                 »
                </div>
                <div align="justify">
                 C'était quand même une belle histoire de vermisseaux...
                </div>
                <div align="justify">
                 Rendez-vous au Jugement dernier... je veux dire au mois prochain. Ce n'est pas moi qui vous parlerai de l'anthologie de Denis Guiot,
                 <a href="http://www.noosfere.com/icarus/livres/niourf.asp?numlivre=2926">
                  <i>
                   Pardonnez-nous vos enfances
                  </i>
                 </a>
                 , car je figure (honorablement) dans ce prochain volume de Présence du futur.
                </div>
                <p align="right">
                 <a href="critsign.asp?numauteur=36">
                  Michel JEURY
                 </a>
                 <br/>
                 Première parution : 1/1/1978 dans
                 <a href="/livres/niourf.asp?numlivre=2146569800">
                  Fiction 287
                 </a>
                 <br/>
                 Mise en ligne le : 12/2/2011
                 <br/>
                 <br/>
                </p>
               </div>
              </div>
              <style>
               .sedna {
     background : url(/images/charte/sedna.png) no-repeat;
     background-position: top left;
     padding-top : 1px;
        border: none;
     }
    .sedna-ul {
     background-image: url(/images/collec2.jpg);
     border: 1px solid #F0F8FF;
     border-top-color: #bfc7e4;
     border-right-color: #6f9dcf;
     border-bottom-color: #6f9dcf;
     border-left-color: #bfc7e4;
     padding-top: 1em;
     padding-bottom: 1em;
     padding-left: 0em;
     margin-left:0px;
     margin-right:0px;
     list-style: none;
     }
   .sedna-li {
     border-top-color : #F0F8FF;
     padding-left: 2em;

   }
              </style>
              <div class="sousbloc">
               <span class="AuteurNiourf">
                Adaptations (cinéma, télévision, BD, théâtre, radio, jeu vidéo...)
               </span>
               <hr style="color:CCC;"/>
               <span class="ficheNiourf">
                <a href="FicheFilm.asp?idAdapt=2525">
                 La Cinquième dimension ( Saison 1 - Episode 19 : Le mal génétique )
                </a>
                , 1985, J.D. Feigelson (d'après le texte :
                <a href="./EditionsLivre.asp?ID_ItemSommaire=2296">
                 L'Homme brûlant
                </a>
                ),
                <i>
                 (Episode Série TV)
                </i>
               </span>
               <br/>
               <span class="ficheNiourf">
                <a href="FicheFilm.asp?idAdapt=2860">
                 Ray Bradbury présente ( Saison 3 - Episode 02 : A Miracle of Rare Device )
                </a>
                , 1989, Roger Tompkins (d'après le texte :
                <a href="./EditionsLivre.asp?ID_ItemSommaire=3112">
                 Les Miracles de Jamie
                </a>
                ),
                <i>
                 (Episode Série TV)
                </i>
               </span>
               <br/>
               <span class="ficheNiourf">
                <a href="FicheFilm.asp?idAdapt=2723">
                 A Piece of Wood
                </a>
                , 2005, Tony Baez Milan (d'après le texte :
                <a href="./EditionsLivre.asp?ID_ItemSommaire=3213">
                 Un morceau de bois
                </a>
                ),
                <i>
                 (Court Métrage)
                </i>
               </span>
               <br/>
               <br/>
              </div>
              <script type="text/javascript">
               function plus() {var compteur = document.getElementById("cptpapiervf");compteur.value++;}
function moins() {var comp = document.getElementById("cptpapiervf");comp.value--;}
function plusnum() {var compteur = document.getElementById("cptnumvf");compteur.value++;}
function moinsnum() {var comp = document.getElementById("cptnumvf");comp.value--;}
function plusVO() {var compteur = document.getElementById("cptpapiervo");compteur.value++;}
function moinsVO() {var comp = document.getElementById("cptpapiervo");comp.value--;}
function plusnumVO() {var compteur = document.getElementById("cptnumvo");compteur.value++;}
function moinsnumVO() {var comp = document.getElementById("cptnumvo");comp.value--;}
              </script>
             </div>
             <div class="sousbloc">
              <span class="sousFicheNiourf">
              </span>
             </div>
            </div>
           </td>
          </tr>
         </tbody>
        </table>
       </div>
      </div>
      <div style="text-align:center;">
       <a href="#">
        retour en haut de page
       </a>
      </div>
      <div>
       <script language="JavaScript">
        function Form_validator(theForm) {

if (theForm.LinkDesc.value=="")
  {
     alert("Vous devez choisir une page thème !");
     theForm.LinkDesc.focus();
     return(false);
  }
return (true);
}

function showLayer(id) {
   if(document.getElementById(id).style.visibility == "hidden"){
      document.getElementById(id).style.visibility = "visible";
      document.getElementById(id).style.display = "block";
   }
   else{
   document.getElementById(id).style.visibility = "hidden";
   document.getElementById(id).style.display = "none";
   }
}
       </script>
       <!-- Piwik -->
       <script type="text/javascript">
        var _paq = _paq || [];
  _paq.push([function() {
var self = this;
function getOriginalVisitorCookieTimeout() {
 var now = new Date(),
 nowTs = Math.round(now.getTime() / 1000),
 visitorInfo = self.getVisitorInfo();
 var createTs = parseInt(visitorInfo[2]);
 var cookieTimeout = 33696000; // 13 mois en secondes
 var originalTimeout = createTs + cookieTimeout - nowTs;
 return originalTimeout;
}
this.setVisitorCookieTimeout( getOriginalVisitorCookieTimeout() );
}]);
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="//matomo.noosfere.org/";
    _paq.push(['setTrackerUrl', u+'piwik.php']);
    _paq.push(['setSiteId', 1]);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);
  })();
       </script>
       <noscript>
        <p>
         <img alt="" src="//matomo.noosfere.org/piwik.php?idsite=1" style="border:0;"/>
        </p>
       </noscript>
       <!-- End Piwik Code -->
       <br/>
       <table class="piedpage" width="100%">
        <tbody>
         <tr>
          <td class="paragraphecentre">
           <b>
            Dans la nooSFere :
           </b>
           88017 livres, 113839 photos de couvertures, 84475 quatrièmes.
          </td>
         </tr>
         <tr>
          <td class="paragraphecentre">
           11124 critiques, 47520 intervenant·e·s, 2003 photographies, 3925 adaptations.
          </td>
         </tr>
         <tr>
          <td>
           <br/>
          </td>
         </tr>
         <tr>
          <td class="paragraphecentre">
           NooSFere est une encyclopédie et une base de données bibliographique.
           <br/>
           <span style="font-variant:small-caps; font-weight:bold;">
            Nous ne sommes ni libraire ni éditeur, nous ne vendons pas de livres et ne publions pas de textes.
           </span>
           <a href="/actu/librairies.asp">
            Trouver une librairie !
           </a>
           <br/>
           <a href="/noosfere/assoc/nous_rejoindre.asp">
            A propos de l'association
           </a>
           -
           <a href="/vieprivee.asp">
            Vie privée et cookies/RGPD
           </a>
           <br/>
           <br/>
          </td>
         </tr>
         <tr>
          <td>
          </td>
         </tr>
        </tbody>
       </table>
       <br/>
      </div>
     </td>
    </tr>
   </tbody>
  </table>
  <script>
   (function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'9a0a2c06fa2d7b7c',t:'MTc2MzQ5NzI2Mw=='};var a=document.createElement('script');a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();
  </script>
 </body>
</html>
'''
from bs4 import BeautifulSoup as BS
import datetime

soup = BS(info, "html5lib" )
soup_fiche_livre = soup.select_one("div[id='Fiche_livre']")

      # get generic comments
comment_generic=None
comment_generic = soup_fiche_livre.select_one("span[class='ficheNiourf']")   #[0]
new_div=soup.new_tag('div')
comment_generic = comment_generic.wrap(new_div)

print( comment_generic.prettify())

  # other editions
comment_AutresEdition=None
if soup.select_one("#AutresEdition"):
        comment_AutresEdition = soup.select_one("#AutresEdition")
        # if debug: self.log.info(self.who,"comment_AutresEdition processed : ")
        # if debug: self.log.info(self.who,"comment_AutresEdition soup :\n", type(comment_AutresEdition),"\n", comment_AutresEdition)              # a bit long I guess

print(comment_AutresEdition.prettify())