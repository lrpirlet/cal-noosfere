info = '''
 <html>
 <head>
  <script language="JavaScript">
   function popuphlp(page,nom,poption) {
var w=window.open(page, nom, poption);
w.focus();
}
  </script>
  <link href="/images/logos/favicon.jpg" rel="icon" type="image/jpg"/>
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
   Chroniques martiennes - Ray BRADBURY - Fiche livre -  Critiques - Adaptations - nooSFere
  </title>
  <meta content="Chroniques martiennes, Ray BRADBURY" property="og:title"/>
  <meta content="Chroniques martiennes, Ray BRADBURY" name="twitter:text:title"/>
  <meta content="Fiche livre, critiques, adaptations" property="og:description"/>
  <meta content="https://images.noosfere.org/couv/p/pdf001-1954.jpg" property="og:image"/>
  <meta content="@noosfere" name="twitter:site"/>
  <meta content="https://images.noosfere.org/couv/p/pdf001-1954.jpg" name="twitter:image"/>
  <meta content="summary_large_image" name="twitter:card"/>
  <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
  <meta content="nooSFere" name="description"/>
  <meta content="SF fantastique fantasy imaginaire" name="keywords"/>
  <meta content="noocontact@noosfere.com" name="author"/>
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
           <a href="#" onclick="afficherChoix('/modules/charte/choix/choix.asp?numlivre=-990755478&amp;Tri=3');return false">
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
                 Par auteur
                </a>
                /
                <a href="/livres/critiques.asp">
                 Par titre
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a border="0" href="/livres/critseries.asp">
                 Par série
                </a>
                /
                <a border="0" href="/livres/critrevues.asp">
                 Par revue
                </a>
               </span>
              </td>
             </tr>
             <tr>
              <td>
               <span class="sous_menu_gauche">
                <a href="/livres/critsign.asp">
                 Par chroniqueur
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
               <a href="https://images.noosfere.org/couv/p/pdf001-1954.jpg">
                <img border="0" height="350" name="couverture" src="https://images.noosfere.org/couv/p/pdf001-1954.jpg" title="Chroniques martiennes"/>
               </a>
               <br/>
               <a class="sousFicheNiourf" onclick="affichetout()" style="cursor:pointer">
                Afficher toutes les images (2)
               </a>
              </div>
              <div id="toutcouvs" style="display:none">
               <a href="https://images.noosfere.org/couv/p/pdf001-1954.jpg">
                <img border="0" height="350" name="couverture" src="https://images.noosfere.org/couv/p/pdf001-1954.jpg" title="Chroniques martiennes"/>
               </a>
               <a href="https://images.noosfere.org/couv/p/pdf001-1954-4e.jpg">
                <img border="0" height="350" name="couverture" src="https://images.noosfere.org/couv/p/pdf001-1954-4e.jpg" title="Chroniques martiennes"/>
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
               Chroniques martiennes
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
                The Martian Chronicles, 1950
               </i>
               <br/>
               Première parution :
               <i>
                New York, États-Unis : Doubleday, mai 1950
               </i>
               <a class="btn" href="http://www.isfdb.org/cgi-bin/se.cgi?arg=The Martian Chronicles&amp;type=Fiction+Titles" style="color:white" target="_blank">
                ISFDB
               </a>
               <br/>
               Traduction de
               <a href="/livres/auteur.asp?NumAuteur=1049">
                Henri ROBILLOT
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
               n° (1)
               <a href="/livres/niourf.asp?numlivre=-327081">
                <img <="" alt="suivant dans la collection" img="" src="/images/arrow_right.gif" title="suivant dans la collection"/>
               </a>
               <br/>
              </span>
              <span class="sousFicheNiourf">
               Dépôt légal :  1er trimestre 1954, Achevé d'imprimer : 1
               <a href="parutions.asp?interv=mois&amp;mois=3&amp;annee=1954" title="Accès aux parutions du même mois">
                mars 1954
               </a>
               <br/>
               Première édition
               <br/>
               Recueil de nouvelles, 270 pages, catégorie / prix : 450 F
               <br/>
               ISBN : néant
               <br/>
               Format : 14,0 x 20,5 cm
               <span style="padding-left:1em" title="Les informations concernant cet ouvrage sont fiables (il est passé entre les mains d'un adhérent de noosfere).">
                ✅
               </span>
               <br/>
               Genre : Science-Fiction
               <br/>
               <br/>
               Edition non numérotée.
               <br/>
              </span>
              <br/>
              <div id="AutresEdition">
               <span class="sousFicheNiourf">
                <a href="EditionsLivre.asp?numitem=752" title="Voir toutes les éditions">
                 Autres éditions
                </a>
               </span>
               <br/>
               <span class="ReuniNiourf">
                <a href="niourf.asp?NumLivre=-2128089650">
                 CAL (Culture, Arts, Loisir), 1973
                </a>
                <br/>
                <a href="niourf.asp?NumLivre=859852496">
                 CLUB DES AMIS DU LIVRE, 1964
                </a>
                <br/>
                <a href="niourf.asp?NumLivre=1948395602">
                 CLUB DU MEILLEUR LIVRE, 1955
                </a>
                <br/>
                <a href="niourf.asp?NumLivre=2146572442">
                 DENOËL, 1954
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146585835">
                 1960
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146586885">
                 1963
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146558042">
                 1966
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146557621">
                 1968
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146576086">
                 1970
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146575066">
                 1973
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146585540">
                 1974
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146582734">
                 1975
                </a>
                ,
                <a href="niourf.asp?NumLivre=-324401">
                 1976
                </a>
                ,
                <a href="niourf.asp?NumLivre=931865635">
                 1978
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146601962">
                 1978
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146573513">
                 1979
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146617211">
                 1979
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146557744">
                 1980
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146563300">
                 1980
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146585352">
                 1981
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146601933">
                 1981
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146558072">
                 1982
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146617208">
                 1982
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146558793">
                 1983
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146635217">
                 1983
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146631461">
                 1984
                </a>
                ,
                <a href="niourf.asp?NumLivre=-323196">
                 1986
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146589387">
                 1986
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146637918">
                 1987
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146589552">
                 1988
                </a>
                ,
                <a href="niourf.asp?NumLivre=-316272">
                 1989
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146574983">
                 1990
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146617449">
                 1991
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146631135">
                 1991
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146563195">
                 1993
                </a>
                ,
                <a href="niourf.asp?NumLivre=-327082">
                 1994
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146602032">
                 1995
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146640924">
                 1995
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146616732">
                 1996
                </a>
                ,
                <a href="niourf.asp?NumLivre=-1247726421">
                 1997
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146588363">
                 1999
                </a>
                <br/>
                <i>
                 in
                </i>
                Fahrenheit 451 - Chroniques martiennes - Les pommes d'or du soleil,
                <a href="niourf.asp?NumLivre=2146570818">
                 2007
                </a>
                <br/>
                <a href="niourf.asp?NumLivre=2146608057">
                 DENOËL, 2019
                </a>
                <br/>
                <a href="niourf.asp?NumLivre=1389089545">
                 FRANCE LOISIRS, 1982
                </a>
                <br/>
                <a href="niourf.asp?NumLivre=-325471">
                 GALLIMARD, 2001
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146617231">
                 2001
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146607404">
                 2002
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146600947">
                 2004
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146574404">
                 2008
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146617320">
                 2017
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146617230">
                 2018
                </a>
                <br/>
                <i>
                 in
                </i>
                D'un monde l'autre,
                <a href="niourf.asp?NumLivre=2146639482">
                 2024
                </a>
                <br/>
                <a href="niourf.asp?NumLivre=2146563182">
                 GALLIMARD Jeunesse, 1976
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146583391">
                 1980
                </a>
                ,
                <a href="niourf.asp?NumLivre=-319251">
                 1988
                </a>
                ,
                <a href="niourf.asp?NumLivre=2146598334">
                 1990
                </a>
                <br/>
                <a href="niourf.asp?NumLivre=2146618268">
                 Le GRAND LIVRE DU MOIS, 1991
                </a>
                <br/>
                <a href="niourf.asp?NumLivre=-1930751618">
                 LIVRE DE POCHE, 1968
                </a>
                <br/>
                sous le titre
                <i>
                 The Martian Chronicles
                </i>
                ,
                <a href="niourf.asp?NumLivre=2146559530">
                 2004
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
               <a class="undertag" href="/tags/tag_content.asp?tag=1" title="">
                science-fiction
               </a>
               <a class="undertag" href="/tags/tag_content.asp?tag=24" title="">
                utopie
               </a>
               <a class="undertag" href="/tags/tag_content.asp?tag=297" title="">
                martiens
               </a>
               <a class="undertag" href="/tags/tag_content.asp?tag=63" title="">
                colonisation
               </a>
               <a class="undertag" href="/tags/tag_content.asp?tag=139" title="">
                origine :  États-Unis
               </a>
               <a class="undertag" href="/tags/tag_content.asp?tag=118" title="">
                Mars
               </a>
               <a class="undertag" href="/tags/tag_content.asp?tag=135" title="">
                futur proche
               </a>
              </div>
              <script>
               autocomplete(document.getElementById("tag"), tags);
              </script>
             </div>
             <div style="clear:right">
              <br/>
              <div class="ficheNiourf" style="text-align:left;padding-left:1em">
               Pas de texte sur la quatrième de couverture.
              </div>
              <div class="sousbloc">
               <div style="padding-bottom:0.5em">
                <span class="AuteurNiourf">
                 Sommaire
                </span>
                <hr style="color:CCC;"/>
               </div>
               <span class="sousFicheNiourf" style="padding:1em">
                <a href="?numlivre=-990755478&amp;somcomplet=1#sommaire">
                 Afficher les différentes éditions des textes
                </a>
                <br/>
               </span>
               <div id="sommaire" style="padding-top:1em">
                <span class="ficheNiourf">
                 1 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=1747">
                  L'Été de la fusée
                 </a>
                 <i>
                  (Rocket Summer, 1947)
                 </i>
                 , pages 7 à 8, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 2 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=5340">
                  Ylla
                 </a>
                 <i>
                  (Ylla / I'll Not Look for Wine, 1950)
                 </i>
                 , pages 9 à 25, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 3 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=3402">
                  La Nuit d'été
                 </a>
                 <i>
                  (The Summer Night / The Spring Night, 1949)
                 </i>
                 , pages 26 à 28, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 4 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=2382">
                  Les Hommes de la Terre
                 </a>
                 <i>
                  (The Earth Men, 1948)
                 </i>
                 , pages 29 à 49, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 5 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=1061">
                  Le Contribuable
                 </a>
                 <i>
                  (The Taxpayer, 1950)
                 </i>
                 , pages 50 à 51, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 6 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=5033">
                  La Troisième expédition
                 </a>
                 <i>
                  (The Third Expedition / Mars Is Heaven!, 1948)
                 </i>
                 , pages 52 à 74, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 7 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=1720">
                  Et la lune toujours brillante
                 </a>
                 <i>
                  (And the Moon Be Still as Bright, 1948)
                 </i>
                 , pages 75 à 107, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 8 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=3789">
                  Les Pionniers
                 </a>
                 <i>
                  (The Settlers, 1950)
                 </i>
                 , pages 108 à 109, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 9 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=3017">
                  Le Matin vert
                 </a>
                 <i>
                  (The Green Morning, 1950)
                 </i>
                 , pages 110 à 116, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 10 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=4472">
                  Les Sauterelles
                 </a>
                 <i>
                  (The Locusts, 1950)
                 </i>
                 , pages 117 à 117, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 11 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=4228">
                  Rencontre nocturne
                 </a>
                 <i>
                  (Night Meeting, 1950)
                 </i>
                 , pages 118 à 128, extrait de nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 12 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=4353">
                  Le Rivage
                 </a>
                 <i>
                  (The Shore, 1950)
                 </i>
                 , pages 129 à 130, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 13 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=2510">
                  Intérim
                 </a>
                 <i>
                  (Interim, 1950)
                 </i>
                 , pages 131 à 131, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 14 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=3276">
                  Les Musiciens
                 </a>
                 <i>
                  (The Musicians, 1950)
                 </i>
                 , pages 132 à 134, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 15 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=97">
                  A travers les airs
                 </a>
                 <i>
                  (Way in the Middle of the Air, 1950)
                 </i>
                 , pages 135 à 152, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 16 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=3353">
                  Nommer les noms
                 </a>
                 <i>
                  (The Naming of Names, 1950)
                 </i>
                 , pages 153 à 154, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 17 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=5078">
                  Usher II
                 </a>
                 <i>
                  (Usher II, 1950)
                 </i>
                 , pages 155 à 175, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 18 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=5188">
                  Les Vieillards
                 </a>
                 <i>
                  (The Old Ones, 1950)
                 </i>
                 , pages 176 à 176, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 19 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=2996">
                  Le Martien
                 </a>
                 <i>
                  (The Martian / September 2005: The Martian / September 2036: The Martian / Impossible, 1949)
                 </i>
                 , pages 177 à 194, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 20 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=588">
                  La Boutique de bagages
                 </a>
                 <i>
                  (The Luggage Store, 1950)
                 </i>
                 , pages 195 à 196, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 21 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=3243">
                  La Morte-saison
                 </a>
                 <i>
                  (The Off Season, 1948)
                 </i>
                 , pages 197 à 212, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 22 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=4733">
                  Les Spectateurs
                 </a>
                 <i>
                  (The Watchers, 1950)
                 </i>
                 , pages 213 à 214, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 23 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=5218">
                  Les Villes muettes
                 </a>
                 <i>
                  (The Silent Towns, 1949)
                 </i>
                 , pages 215 à 228, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 24 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=2812">
                  Les Longues années
                 </a>
                 <i>
                  (The Long Years / Dwellers in Silence, 1949)
                 </i>
                 , pages 229 à 243, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 25 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=2453">
                  Il viendra des pluies douces
                 </a>
                 <i>
                  (There Will Come Soft Rains, 1950)
                 </i>
                 , pages 244 à 252, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
                 </a>
                </span>
                <br/>
                <span class="ficheNiourf">
                 26 -
                 <a href="./EditionsLivre.asp?ID_ItemSommaire=3791">
                  Le Pique-nique d'un million d'années
                 </a>
                 <i>
                  (The Million Year Picnic, 1946)
                 </i>
                 , pages 253 à 265, nouvelle, trad.
                 <a href="/livres/auteur.asp?NumAuteur=1049">
                  Henri ROBILLOT
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
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   [Critique des livres suivants :
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   -
                   <a href="https://www.noosfere.org/livres/niourf.asp?numlivre=-990755478">
                    <em>
                     <strong>
                      Chroniques martiennes
                     </strong>
                    </em>
                   </a>
                   de Ray Bradbury, Denoël Présence du futur n° 1
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   -
                   <a href="https://www.noosfere.org/livres/niourf.asp?numlivre=-326097">
                    <em>
                     <strong>
                      Une étoile m'a dit
                     </strong>
                    </em>
                   </a>
                   de Fredric Brown, Denoël Présence du futur n° 2
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   -
                   <a href="https://www.noosfere.org/livres/niourf.asp?numlivre=4123">
                    <em>
                     <strong>
                      Ceux de nulle part
                     </strong>
                    </em>
                   </a>
                   de Francis Carsac, Gallimard Rayon fantastique n° 23
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   -
                   <a href="https://www.noosfere.org/livres/niourf.asp?numlivre=5299">
                    <em>
                     <strong>
                      Fuite dans l'inconnu
                     </strong>
                    </em>
                   </a>
                   de Jean-Gaston Vandel, Fleuve Noir Anticipation n° 34
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   -
                   <a href="https://www.noosfere.org/livres/niourf.asp?numlivre=5682">
                    <strong>
                     <em>
                      Î
                     </em>
                    </strong>
                   </a>
                   <em>
                    <a href="https://www.noosfere.org/livres/niourf.asp?numlivre=5682">
                     <strong>
                      les de l’espace
                     </strong>
                    </a>
                   </em>
                   d'Arthur C. Clarke, Fleuve Noir Anticipation n° 35
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   -
                   <a href="https://www.noosfere.org/livres/niourf.asp?numlivre=5741">
                    <em>
                     <strong>
                      L'Invention de Morel
                     </strong>
                    </em>
                   </a>
                   d'Adolfo Bioy Casares, Robert Laffont]
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   Après Gallimard et le Fleuve Noir, les Éditions Denoël lancent, à leur tour, une collection d’anticipation scientifique romancée (pas uniquement S.-F., semble-t-il d’ailleurs, car le catalogue annonce pour paraître prochainement un ouvrage de H.-P. Lovecraft, un des maîtres britanniques du fantastique, de la sorcellerie et de la démonologie). Elle s’intitule « Présence du futur » et ses deux premiers-nés (Bradbury et Brown) sont l’un excellent, l’autre très bon.
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   <em>
                    «
                    <a href="https://www.noosfere.org/livres/niourf.asp?numlivre=-990755478">
                     <strong>
                      Chroniques martiennes
                     </strong>
                    </a>
                   </em>
                   », de Ray Bradbury, est de la qualité de «
                   <a href="https://www.noosfere.org/livres/niourf.asp?numlivre=-927993967">
                    <strong>
                     <em>
                      Demain les chiens
                     </em>
                    </strong>
                   </a>
                   », de Clifford D. Simak, dont j’ai rendu compte il y a quelques mois. C’est l’histoire de la colonisation, du dépeuplement, de l’abandon et de la recolonisation de la planète rouge par les hommes. Le roman se présente sous forme de vingt-six chroniques, les unes assez longues, d’autres fort brèves, la plupart rattachées les unes aux autres par des liens assez lâches. Certaines sont de purs chefs-d’œuvre d’humour («
                   <em>
                    Les Hommes de la Terre
                   </em>
                   », qui relate la façon étrange dont les Martiens accueillent les premiers Terriens), de terreur macabre
                   <em>
                    (« La Troisième expédition
                   </em>
                   », qui décrit le sort réservé à d’autres astronautes), de révolte contre la civilisation moderne («
                   <em>
                    Et la lune toujours brillante »,
                   </em>
                   où l’on voit un des conquérants de l’espace devenir l’allié des Martiens morts), de satire cruelle sur le sort des noirs américains («
                   <em>
                    À travers les airs
                   </em>
                   »), ou, enfin, d’horreur sardonique (« U
                   <em>
                    sher II
                   </em>
                   »). J’arrête là l’énumération, car il me faudrait citer presque tout le livre. Comme dans la plupart de ses ouvrages, Bradbury, écrivain amer, cingle vigoureusement la culture de notre siècle et s’élève avec force contre les « tabous » venant du sommet de la pyramide. (N’imagine-t-il pas, dans un chapitre, que le gouvernement américain de la fin du XXe siècle a interdit les œuvres de Poe, les contes de fées et même les populaires
                   <em>
                    nursery-rhymes ?)
                   </em>
                   Sous ce rapport, il est proche d’un George Orwell, ce qui lui a parfois valu des piques de la part de certains critiques orthodoxes d’outre-atlantique. C’est d’ailleurs « une forte tête », un non-conformiste intégral qui, dans un pays de dictature, connaîtrait le camp de concentration. En formulant l’espoir qu’il ne lui arrive rien de tel, je ne puis que vous recommander ces
                   <em>
                    « Chroniques martiennes
                   </em>
                   », spécimen parfait d’une S.-F. intelligente, imaginative et admirablement contée.
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   <em>
                    «
                    <a href="https://www.noosfere.org/livres/niourf.asp?numlivre=-326097">
                     <strong>
                      Une étoile m’a dit
                     </strong>
                    </a>
                   </em>
                   » (Space on my hands), de Fredric Brown, est un recueil de huit nouvelles allant du « bon » au « très bon ». (Une seule m’a paru plus faible, «
                   <em>
                    Mitkey
                   </em>
                   », conte à tendances philosophiques qui tombe un peu à plat. Quelle idée aussi de « vaire barler doud au long afec l’agzent » le herr professor-Oberburger, ce qui rend la lecture irritante ?) Deux ou trois sont teintées d’un humour agréable («
                   <em>
                    Les Myeups
                   </em>
                   », charmante ;
                   <em>
                    « Anarchie dans le ciel
                   </em>
                   », grandguignolesque ; «
                   <em>
                    Un coup à la porte
                   </em>
                   », spirituelle mais mélancolique, d’autres sont poignantes («
                   <em>
                    Quelque chose de vert
                   </em>
                   » et «
                   <em>
                    Tu seras fou »,
                   </em>
                   qui provoquera peut-être quelque colère chez les bonapartistes). Il n’y manque même pas un récit policier («
                   <em>
                    Tu n’as point tué »). « Cauchemar
                   </em>
                   » rappelle un peu un roman de Maurice Renard, mais ces rencontres, dans le domaine du fantastique, sont inévitables. Il me serait difficile de désigner celle ou celles des nouvelles que je préfère. En fait, à l’exception de «
                   <em>
                    M
                   </em>
                   <em>
                    itkey
                   </em>
                   », je les ai toutes aimées et il ne me reste qu’à souhaiter que les lecteurs de cette chronique partagent mon opinion.
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   Événement au « Rayon Fantastique » (Gallimard) : un roman français, «
                   <em>
                    <a href="https://www.noosfere.org/livres/niourf.asp?numlivre=4123">
                     <strong>
                      Ceux de nulle part
                     </strong>
                    </a>
                    »
                   </em>
                   de Francis Carsac. Disons tout de suite que l’ouvrage soutient la comparaison avec les meilleurs d’A. S. américains et britanniques et dépasse même bon nombre d’entre eux. C’est le récit d’une guerre intergalactique, intelligemment conçu, avec une base profondément philosophique : la lutte éternelle entre le Bien et le Mal. Pas de politique, pas d’agent de la 1.005e colonne – oui, tout ceci est bien frais et bien plaisant. Et très d’actualité aussi. (Le roman débute par l’arrivée d’une soucoupe volante et se termine sur un sujet qui a intrigué nos ancêtres autant que nos contemporains – les disparitions d’hommes et de femmes qu’on ne retrouve jamais – thème cher aux auteurs de S.-F.) Les mondes « extérieurs » sont décrits avec beaucoup d’imagination, mais de façon fort logique. Bref, un excellent roman que je vous recommande chaleureusement.
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   <em>
                    «
                    <a href="https://www.noosfere.org/livres/niourf.asp?numlivre=5299">
                     <strong>
                      Fuite dans l’inconnu
                     </strong>
                    </a>
                    »,
                   </em>
                   de Jean-Gaston Vandel (Fleuve Noir), n’a pas le fignolage, le fini de «
                   <strong>
                    <em>
                     Ceux de nulle part
                    </em>
                   </strong>
                   », mais il est bon et me semble promis à une fructueuse carrière. L’humanité se meurt d’un mal mystérieux, la cilicose. Un jeune savant, Dox Gavnor, émet alors une théorie révolutionnaire : comme de vulgaires ptérodactyles ou brontosaures, les hommes sont destinés à disparaître du fait d’une évolution normale. Un seul moyen de sauver la race : créer des êtres « concentrés ». Non sans difficulté, il parvient à implanter cette idée, mais l’expérience dépasse ses prévisions les plus optimistes et voilà les humains aux prises avec les « synthétiques » qui prétendent prendre possession du globe. Comme dans un roman policier, la fin ne se raconte pas – ce serait gâcher votre plaisir, car vous en aurez sûrement, du plaisir, à lire cette variante de l’histoire de
                   <em>
                    « l’Apprenti Sorcier ».
                   </em>
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   <em>
                    «
                   </em>
                   <a href="https://www.noosfere.org/livres/niourf.asp?numlivre=5682">
                    <strong>
                     <em>
                      Î
                     </em>
                     <em>
                      les de l’espace
                     </em>
                    </strong>
                   </a>
                   » (Islands in the sky) – chez le même éditeur, s’adresserait plutôt à des adolescents ou à des J3 s’il n’était signé d’Arthur C. Clarke, un des « as » de S.-F. américaine. C’est le récit d’un garçon de seize ans qui, lauréat d’un concours publicitaire, se voit offrir comme récompense un séjour dans une station-relais de l’espace, à 800 kilomètres de la Terre. Il n’y restera pas, bien sûr, et d’autres aventures le mèneront plus haut, beaucoup plus haut. L’intérêt majeur de ce roman réside, à mon avis, dans son aspect documentaire. Ingénieur spécialisé dans l’étude de l’astronautique, Clarke, espèce d’Ananoff américain, est en effet l’auteur d’un remarquable ouvrage technique :
                   <em>
                    « Exploration of space ».
                   </em>
                   Et, dans
                   <em>
                    «
                   </em>
                   <strong>
                    <em>
                     Î
                    </em>
                    <em>
                     les de l’espace
                    </em>
                   </strong>
                   », il nous décrit la vie d’une station-relais, telle qu’elle le sera vraisemblablement une fois que l’homme aura réussi à créer ces « îles flottantes ». Il n’y a pas de fantaisie là-dedans, mais l’humour n’en est pas absent (exemples : l’expédition cinématographique ou la rencontre avec des Terro-Martiens). En outre, voilà un volume que feraient bien d’étudier tous ceux qui veulent écrire de l’A. S., voire ceux qui en écrivent déjà. Sa lecture leur permettra d’éviter bien des erreurs.
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <!--StartFragment-->
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   «
                   <a href="https://www.noosfere.org/livres/niourf.asp?numlivre=5741">
                    <strong>
                     <em>
                      L’Invention de Morel
                     </em>
                    </strong>
                   </a>
                   », d’Adolfo Bioy Casares (Robert Laffont), se classe dans une catégorie à part. Ce n’est à proprement parler ni une œuvre de S.-F. ni un roman fantastique, et mériterait de porter en sous-titre le mot « cauchemar à quatre dimensions ». C’est l’histoire d’un condamné qui parvient à se réfugier dans une île déserte où l’on risque de contracter une espèce de peste. Seulement, déserte, l’est-elle vraiment cette île ? Il y trouve des gens, mais ceux-ci ne semblent ni le voir ni l’entendre. Peu à peu, il percera leur secret ; trop tard, hélas !… En réalité, le résumé succinct ci-dessus ne peut aucunement vous donner une idée même approximative de ce récit dû à un des plus grands auteurs argentins de notre génération, ami et collaborateur de Jorge Luis Borges, dont je vous ai souvent parlé ici même.
                  </span>
                 </span>
                </p>
                <p>
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   L’action passe du réel à l’irréel avec une aisance qu’on pourrait presque qualifier d’inquiétante. On en vient à se demander si le héros du drame n’est pas fou. Il ne l’est pas, pourtant, puisqu’il raisonne, puisqu’il cherche aux phénomènes dont il est le témoin, et qu’il ne comprend pas, des explications logiques, tel un homme qui, se réveillant au milieu de la nuit, se demande s’il a rêvé ou non. C’est également un roman d’amour (mais d’Amour avec un grand A), dont l’objet, lui aussi, est tout à tour réel et irréel. Tout cela nous vaut une œuvre curieuse, pleine de symboles, pas toujours facile à lire, mais hautement intéressante, dans une très belle traduction d’Armand Pierhal.
                  </span>
                 </span>
                </p>
                <p align="right">
                 <a href="critsign.asp?numauteur=-51559">
                  Igor B. MASLOWSKI
                 </a>
                 <br/>
                 Première parution : 1/5/1954 dans
                 <a href="/livres/niourf.asp?numlivre=2146569519">
                  Fiction 6
                 </a>
                 <br/>
                 Mise en ligne le : 27/2/2025
                 <br/>
                 <br/>
                </p>
               </div>
              </div>
              <div class="sousbloc">
               <span class="AuteurNiourf">
                Critiques des autres éditions ou de la série
               </span>
               <hr style="color:CCC;"/>
               <center>
                <a href="./niourf.asp?numlivre=2146574404">
                 Edition GALLIMARD, Folio SF
                </a>
                (2013)
               </center>
               <br/>
               <div id="critique">
                <p>
                 <span style="font-size:medium">
                  <span style="color:black">
                   Parmi les rares livres de science-fiction étudiés dans les établissements scolaires de France et de Navarre,
                  </span>
                  <em>
                   <span style="color:black">
                    Chroniques martiennes
                   </span>
                  </em>
                  <span style="color:black">
                   se taille la part du lion, aux côtés de
                  </span>
                  <em>
                   <span style="color:black">
                    1984
                   </span>
                  </em>
                  <span style="color:black">
                   et de quelques autres barjaveleries. Pour l’anecdote, le chroniqueur confesse avoir fait lui-même ses premières armes avec ce faux roman — on va y revenir — dont il garde par ailleurs un souvenir ému, ravivé ensuite par l’adaptation télé en trois parties de Michael Anderson (scénarisée par Richard Matheson, excusez du peu).
                  </span>
                 </span>
                </p>
                <p style="margin-left:0px; margin-right:0px; text-align:justify">
                 <span style="font-size:medium">
                  <span style="color:black">
                   On le voit, difficile d’échapper au registre de la nostalgie, et ce d’autant plus que
                  </span>
                  <em>
                   <span style="color:black">
                    Chroniques martiennes
                   </span>
                  </em>
                  <span style="color:black">
                   a inauguré la collection « Présence du futur » des éditions Denoël, chère au cœur des plus chenus parmi nous. Réédité en France en 1997 dans sa version intégrale, dite du quarantième anniversaire, l’ouvrage a bénéficié à cette occasion d’une révision de sa traduction par Jacques Chambon. Un toilettage bienvenu ayant permis de corriger quelques fâcheuses coquilles.
                  </span>
                 </span>
                </p>
                <p style="margin-left:0px; margin-right:0px; text-align:justify">
                 <span style="font-size:medium">
                  <span style="color:black">
                   Comme leur nom l’indique, ces chroniques se composent de vingt-huit courts récits indépendants, parus en magazines ou écrits pour leur édition en recueil. Ordonnées chronologiquement de manière à dessiner une histoire globale s’étendant de l’an 2030 à 2057, elles relatent l’arrivée et l’installation des premiers colons sur Mars. Les Terriens y côtoient les Martiens, dont la civilisation ne tarde pas à disparaître suite à une épidémie de varicelle. Un fait qui inspire les réflexions amères de Spender dans la nouvelle
                  </span>
                  <span style="color:black">
                   «
                   <em>
                    Et la lune qui luit
                   </em>
                   … »
                  </span>
                  <span style="color:black">
                   . Mais, la guerre sur Terre met un coup d’arrêt aux migrations, entraînant le reflux des pionniers, à l’exception d’une poignée d’entre eux, amenés à devenir les nouveaux Martiens.
                  </span>
                 </span>
                </p>
                <p style="margin-left:0px; margin-right:0px; text-align:justify">
                 <span style="font-size:medium">
                  <span style="color:black">
                   A l’instar de Cordwainer Smith ou de Clifford D. Simak, la science et la technologie ne rentrent pas dans les préoccupations de Ray Bradbury. A vrai dire, l’auteur ne se soucie guère de vraisemblance, préférant la poésie, l’émotion et le plaisir de la métaphore aux ébouriffantes spéculations sciences-fictives. Il ne cache d’ailleurs pas son aversion pour la bureaucratie et le rationalisme, en particulier dans la nouvelle
                  </span>
                  <span style="color:black">
                   «
                   <em>
                    Usher II
                   </em>
                   »
                  </span>
                  <span style="color:black">
                   , dont le propos anticipe celui de son roman
                  </span>
                  <em>
                   <span style="color:black">
                    Fahrenheit 451
                   </span>
                  </em>
                  <span style="color:black">
                   .
                  </span>
                  <strong>
                   <span style="color:black">
                   </span>
                  </strong>
                  <span style="color:black">
                   Le voyage spatial et les autres thèmes inhérents au genre apparaissent en conséquence comme des sources d’émerveillement. Une magie moderne utile pour narrer des histoires simples de petites gens, à la Sherwood Anderson, dont le charme suranné et le ton facétieux sont censés réveiller l’ingénuité de l’enfance. Mêlant pseudoscience — la télépathie —, motifs traditionnels du folklore américain et paysages inspirés des visions de Percival Lowell, Ray Bradbury s’acquitte de son tribut à la Barsoom d’Edgar Rice Burroughs. Il s’en détache toutefois, adoptant le ton du moraliste. Au fil des textes, on ne peut en effet s’empêcher d’établir un parallèle entre la colonisation de Mars et celle de l’Ouest américain. Les Terriens, laborieux et attachés à leur liberté, semblent animés par la même ambition que les pionniers du XIXe siècle. Mars apparaît à leurs yeux comme un espace vierge qu’il convient de peupler et de mettre en valeur. Les natifs font évidemment les frais de cette invasion, victimes d’un génocide bactériologique bien involontaire. Ray Bradbury ne se fait cependant guère d’illusion sur ses compatriotes. A la différence des Martiens, les colons cherchent surtout à adapter le milieu aux usages importés de la Terre, recréant sur place une multitude de petites Amériques et façonnant la toponymie selon leurs caprices. Nouvelle terre promise, Mars accueille leurs espoirs de recommencement. Un monde où éteindre leurs craintes ; un monde dégagé de toute contrainte. Des espoirs vite déçus… Au lieu de se fondre dans l’environnement, ils l’exploitent de manière mercantile, mettant à mal les équilibres écologiques. Leur nature industrieuse, leurs emportements violents et le matérialisme dont ils font montre s’opposent au mode de vie contemplatif, spirituel et respectueux de la nature qui prévalait avant leur arrivée.
                  </span>
                 </span>
                </p>
                <p style="margin-left:0px; margin-right:0px; text-align:justify">
                 <span style="font-size:medium">
                  <span style="color:black">
                   En cela,
                  </span>
                  <em>
                   <span style="color:black">
                    Chroniques martiennes
                   </span>
                  </em>
                  <span style="color:black">
                   , sous les apparences de la science-fiction, est un conte moral. Une utopie dont le dénouement se révèle au final optimiste, ou du moins beaucoup plus ouvert que ne le laisse présager son déroulement. Et sous la patine du classique, l’œuvre de Ray Bradbury ne perd rien de son charme et de son pouvoir d’évocation, à la différence de nombreux autres ouvrages de l’âge d’or.
                  </span>
                 </span>
                </p>
               </div>
               <p align="right" style="line-height: normal;margin-right: 20px;">
                <a href="critsign.asp?numauteur=2147185626">
                 Laurent LELEU
                </a>
                <br/>
                <font size="-1">
                 Première parution : 1/10/2013
                 <br/>
                 Bifrost 72
                 <br/>
                 Mise en ligne le : 17/2/2019
                 <br/>
                </font>
               </p>
               <hr style="color:CCC;"/>
               <p align="justify">
               </p>
               <center>
                <a href="./niourf.asp?numlivre=1948395602">
                 Edition CLUB DU MEILLEUR LIVRE,
                </a>
                (1955)
               </center>
               <br/>
               <div id="critique">
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   Avis aux amateurs de « science-fiction » et de beaux livres : ne manquez pas la superbe édition que vient de donner le Club du Meilleur Livre des «
                   <strong>
                    <em>
                     Chroniques martiennes
                    </em>
                   </strong>
                   », de Ray Bradbury. Après Simak, dont
                   <em>
                    «
                    <a href="https://www.noosfere.org/livres/niourf.asp?numlivre=-927993967">
                     <strong>
                      Demain, les chiens
                     </strong>
                    </a>
                   </em>
                   » parut en édition originale au Club Français du Livre, Bradbury est ainsi le second auteur de S.-F. à recevoir la consécration du tirage de luxe dans un grand club littéraire.
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   La présentation matérielle est impeccable et la couverture d’une sobriété d’excellent effet (une simple carte stylisée de Mars en blanc sur fond noir). Mais la meilleure idée de ce club toujours à l’avant-garde a été de prévoir une édition
                   <em>
                    illustrée !
                   </em>
                   Pour la première fois, donc, on est ici en présence d’un livre de S.-F. agrémenté de dessins autres que les habituels bariolages à base de monstres et de fusées ! C’est un jeune artiste, Jacques Noël, qui a eu la tâche difficile de « visualiser » le texte de Bradbury. Il en a tiré la matière d’une quarantaine d’images, dont la première qualité est d’être parfaitement inattendues !
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   Le seul moyen d’éviter les poncifs du dessin « science-fiction » était d’en prendre carrément le contre-pied. Bernard Noël l’a si bien compris qu’il a tenu cette gageure d’illustrer ces chroniques du futur en s’inspirant de la technique et de l’esprit du XIXe siècle ! Ses dessins au trait, avec leur fourmillement minutieux de lignes, évoquent, par le tracé, les gravures des éditions Hetzel de Jules Verne. Quant à leurs sujets, ni rutilants astronefs, ni hommes de l’espace dans leurs scaphandres, ni même Martiens dont l’immense vertu, chez Bradbury, est justement d’être sans cesse à
                   <em>
                    imaginer,
                   </em>
                   sous leur flux d’aspects multiformes. Mais des paysages – vides, morts – des objets, des automates.
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   Bernard Noël a inventé avec astuce une topographie et une architecture « extraterrestres ». Le foisonnement enchevêtré des « canaux », tels que l’astronomie les a vulgarisés, lui a fait concevoir ces panoramas inégaux, aux lignes bizarrement fuyantes, qui font penser aux labyrinthes de la grande muraille de Chine, et ces envolées de constructions étagées, pareilles à de fantastiques châteaux de sable à la géométrie nouvelle
                   <strong>
                    <a href="clbr://internal.sandbox/book/OEBPS/Text/book_0010.xhtml#amanuensis-note7" id="amanuensis-anchor7" style="color: rgb(0, 0, 128); text-decoration: underline;">
                     (7)
                    </a>
                   </strong>
                   .
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   Tournons d’autres pages et voici que surgissent, précis et inquiétants, détaillés comme sur des planches encyclopédiques, les « objets » martiens suggérés par Bradbury : le fusil à abeilles empoisonnées, les araignées d’or tissant leur fil, les bobines à musique, les livres à feuilles d’argent, les bas-reliefs des cités mortes, les fantomatiques sablonefs et aussi les fameux masques portés par les Martiens pour « cacher leurs sentiments » – masques de cristal, masques d’argent, masques de verre, masques de psychiatres aux trois sourires superposés. Un certain nombre de ces dessins sont réunis de façon originale à la fin du volume, en planches se rapportant à l’« archéologie » de Mars.
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   Enfin le thème des automates, cher à Bradbury, a inspiré à Bernard Noël quelques-unes de ses meilleures réussites, notamment pour l’extraordinaire
                   <em>
                    « Usher II
                   </em>
                   ». Les robots meurtriers ou familiers, « sexués mais sans sexe, dénommés mais sans nom », nous guettent au coin d’une page pour nous dédier leurs yeux de marbre et leurs visages souriants, et nous dévoiler impromptu leurs entrailles d’acier et de cuivre.
                  </span>
                 </span>
                </p>
                <p style="margin-left:0; margin-right:0; text-align:justify">
                 <span style="font-size:14px">
                  <span style="font-family:Arial,Helvetica,sans-serif">
                   Dans toutes ces œuvres, ce qui ressort en définitive, c’est la parfaite unité d’un
                   <em>
                    style
                   </em>
                   qui parvient à n’en imiter aucun autre. Et la réalisation s’adapte si bien après coup à l’objet qu’il semble impossible, maintenant, de dissocier le livre de Bradbury de ces visions insolites et du « climat » qu’elles lui ont conféré.
                  </span>
                 </span>
                </p>
               </div>
               <p align="right" style="line-height: normal;margin-right: 20px;">
                <a href="critsign.asp?numauteur=471">
                 Alain DORÉMIEUX
                </a>
                <br/>
                <font size="-1">
                 Première parution : 1/9/1955
                 <br/>
                 Fiction 22
                 <br/>
                 Mise en ligne le : 6/4/2025
                 <br/>
                </font>
               </p>
               <hr style="color:CCC;"/>
               <p align="justify">
               </p>
               <center>
                <a href="./niourf.asp?numlivre=-1247726421">
                 Edition DENOËL, Présence du futur
                </a>
                (1998)
               </center>
               <br/>
               <div id="critique">
                <div align="justify">
                 Depuis sa parution en 1950, le recueil
                 <i>
                  Chroniques martiennes
                 </i>
                 divise critiques et lecteurs, à l'intérieur et à l'extérieur du petit monde de la SF.
                 <br/>
                 <br/>
                 Pour les purs et durs, Bradbury se moque de la vraisemblance (pseudo)-scientifique et écrit de l'anti-SF. De l'autre côté des barbelés, on s'interroge sur cet apatride magnifique rédigeant de la SF comme on écrit de la littérature : ça de la SF ! Allons donc : trop bien écrit pour « en être ». En définitive, les sectaires des deux camps s'accordent sur un point : Ray Bradbury n'est pas un écrivain de SF. Ce qui — bien entendu — ne change en rien la vie de ceux qui, trop occupés à déguster, n'ont pas le temps de lire les étiquettes !
                 <br/>
                 <br/>
                 À deux années du cinquantenaire de cette œuvre fondatrice, un nouveau débat est lancé : les
                 <i>
                  Chroniques martiennes
                 </i>
                 ne seraient pas un recueil de nouvelles (comme chacun croyait le savoir) mais un roman.
                 <br/>
                 <br/>
                 Qu'en penser ? Que répondre ?
                 <br/>
                 <br/>
                 Rappeler que chaque pièce de ce recueil est une œuvre parfaitement autonome — écrite, publiée et lue en son temps comme telle ; ce qui ne contredit en rien l'évidence d'un projet global initial. Admettre que l'une s'enrichit par proximité avec les autres : bien sûr ! Que l'ensemble constitue désormais — mais pas systématiquement : des chroniques sont parfois reprises en anthologies, adaptées en BD ou en épisodes de séries TV — un tout cohérent dans son esthétique et sa thématique : autre évidence ! Penser que ce tout est supérieur à la somme de ses parts, pourquoi pas ?
                 <br/>
                 <br/>
                 Mais rien dans ce qui précède n'autorise à qualifier de « roman » les
                 <i>
                  Chroniques martiennes.
                 </i>
                 <br/>
                 <br/>
                 Passer outre, c'est à mon sens nier la spécificité même de la SF : une littérature dont le vecteur idéal est la « forme courte ». Constat historique mais aussi « technique » — le genre s'est développé dans des périodiques.
                 <br/>
                 <br/>
                 Certains auteurs souhaitant donner du souffle à leur œuvre (et la vendre deux fois...) ont inventé le
                 <i>
                  « fix-up »
                 </i>
                 : roman construit à partir de nouvelles autonomes mais exploitant un « fonds commun » (thématique, personnages, lieux) et suffisamment « ouvertes » pour être accrochées. Que l'on considère par exemple
                 <a href="EditionsLivre.asp?numitem=3320">
                  <i>
                   La Faune de l'espace
                  </i>
                 </a>
                 de
                 <a href="auteur.asp?numauteur=366">
                  van Vogt
                 </a>
                 comme un roman : oui. L'intégration des nouvelles originales a nécessité une réécriture partielle et un remaniement lourd. Mais décrire ces purs recueils de nouvelles que sont
                 <a href="EditionsLivre.asp?numitem=1150">
                  <i>
                   Demain les chiens
                  </i>
                 </a>
                 <i>
                  ,
                  <a href="EditionsLivre.asp?numitem=13090">
                   Fondation
                  </a>
                 </i>
                 ou les
                 <i>
                  Chroniques martiennes
                 </i>
                 comme étant des « romans » : c'est à mon sens confondre feuilleton et série.
                 <br/>
                 <br/>
                 Cette nouvelle édition des
                 <i>
                  Chroniques Martiennes,
                 </i>
                 on l'aura compris, est enrichie d'un copieux dossier à vocation pédagogique, réuni par Jacques Chambon. Si certaines de ses remarques et conclusions peuvent paraître contestables, son argumentation reste toujours très pointue, témoigne de son érudition et de la qualité de sa réflexion. Il s'agit là d'un travail éditorial remarquable et indispensable.
                </div>
               </div>
               <p align="right" style="line-height: normal;margin-right: 20px;">
                <a href="critsign.asp?numauteur=636">
                 Francis VALÉRY
                </a>
                <br/>
                <font size="-1">
                 Première parution : 1/3/1998
                 <br/>
                 dans
                 <a href="../../heberg/ericb33/Sommaire.asp?RevNum=888">
                  Galaxies 8
                 </a>
                 <br/>
                 Mise en ligne le : 13/4/2009
                 <br/>
                </font>
               </p>
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
               <div style="padding-bottom:0.5em">
                <span class="AuteurNiourf">
                 Cité dans les pages thématiques suivantes
                </span>
                <hr style="color:CCC;"/>
               </div>
               <span class="ficheNiourf">
                <a href="/articles/theme.asp?numtheme=33">
                 Contacts
                </a>
                <br/>
               </span>
               <br/>
              </div>
              <div class="sousbloc" style="clear:right">
               <span class="AuteurNiourf">
                Cité dans les Conseils de lecture / Bibliothèque idéale des oeuvres suivantes
               </span>
               <hr style="color:CCC;"/>
               <span class="ficheNiourf">
                Denoël : Catalogue analytique Denoël (
                <a href="/articles/listeoeuvres.asp?numliste=23">
                 liste
                </a>
                )
               </span>
               <br/>
               <span class="ficheNiourf">
                Annick Béguin : Les 100 principaux titres de la science-fiction (
                <a href="/articles/listeoeuvres.asp?numliste=22">
                 liste parue en 1981
                </a>
                )
               </span>
               <br/>
               <span class="ficheNiourf">
                Jacques Sadoul :
                <a href="./niourf.asp?numlivre=-322388">
                 Anthologie de la littérature de science-fiction
                </a>
                (
                <a href="/articles/listeoeuvres.asp?numliste=24">
                 liste parue en 1981
                </a>
                )
               </span>
               <br/>
               <span class="ficheNiourf">
                Jean Gattegno :
                <a href="./niourf.asp?numlivre=-324466">
                 Que sais-je ?
                </a>
                (
                <a href="/articles/listeoeuvres.asp?numliste=26">
                 liste parue en 1983
                </a>
                )
               </span>
               <br/>
               <span class="ficheNiourf">
                Jacques Goimard &amp; Claude Aziza :
                <a href="./niourf.asp?numlivre=-327254">
                 Encyclopédie de poche de la SF
                </a>
                (
                <a href="/articles/listeoeuvres.asp?numliste=3">
                 liste parue en 1986
                </a>
                )
               </span>
               <br/>
               <span class="ficheNiourf">
                Denis Guiot &amp; Jean-Pierre Andrevon &amp; George W. Barlow :
                <a href="./niourf.asp?numlivre=-1148195851">
                 Le Monde de la science-fiction
                </a>
                (
                <a href="/articles/listeoeuvres.asp?numliste=1">
                 liste parue en 1987
                </a>
                )
               </span>
               <br/>
               <span class="ficheNiourf">
                Albin Michel : La Bibliothèque idéale de SF (
                <a href="/articles/listeoeuvres.asp?numliste=21">
                 liste parue en 1988
                </a>
                )
               </span>
               <br/>
               <span class="ficheNiourf">
                Jean-Bernard Oms :
                <a href="./niourf.asp?numlivre=2146560650">
                 Top 100 Carnage Mondain
                </a>
                (
                <a href="/articles/listeoeuvres.asp?numliste=25">
                 liste parue en 1989
                </a>
                )
               </span>
               <br/>
               <span class="ficheNiourf">
                Lorris Murail :
                <a href="./niourf.asp?numlivre=-327253">
                 Les Maîtres de la science-fiction
                </a>
                (
                <a href="/articles/listeoeuvres.asp?numliste=27">
                 liste parue en 1993
                </a>
                )
               </span>
               <br/>
               <span class="ficheNiourf">
                Stan Barets :
                <a href="./niourf.asp?numlivre=1655">
                 Le Science-Fictionnaire - 2
                </a>
                (
                <a href="/articles/listeoeuvres.asp?numliste=9">
                 liste parue en 1994
                </a>
                )
               </span>
               <br/>
               <span class="ficheNiourf">
                Denis Guiot, Stéphane Nicot &amp; Alain Laurie :
                <a href="./niourf.asp?numlivre=-327587">
                 Dictionnaire de la science-fiction
                </a>
                (
                <a href="/articles/listeoeuvres.asp?numliste=11">
                 liste parue en 1998
                </a>
                )
               </span>
               <br/>
               <span class="ficheNiourf">
                Association Infini : Infini (1 - liste primaire) (
                <a href="/articles/listeoeuvres.asp?numliste=60">
                 liste parue en 1998
                </a>
                )
               </span>
               <br/>
               <span class="ficheNiourf">
                Francis Valéry :
                <a href="./niourf.asp?numlivre=-326509">
                 Passeport pour les étoiles
                </a>
                (
                <a href="/articles/listeoeuvres.asp?numliste=20">
                 liste parue en 2000
                </a>
                )
               </span>
               <br/>
               <span class="ficheNiourf">
                (pour la nouvelle&amp;nbp;:
                <a href="EditionsLivre.asp?ID_ItemSommaire=3791">
                 Le Pique-nique d'un million d'années
                </a>
                )Jean-Pierre Fontana : Sondage Fontana - Science-fiction (
                <a href="/articles/listeoeuvres.asp?numliste=4">
                 liste parue en 2002
                </a>
                )
               </span>
               <br/>
               <span class="ficheNiourf">
                François Rouiller :
                <a href="./niourf.asp?numlivre=2146567094">
                 100 mots pour voyager en science-fiction
                </a>
                (
                <a href="/articles/listeoeuvres.asp?numliste=59">
                 liste parue en 2006
                </a>
                )
               </span>
               <br/>
               <br/>
              </div>
              <div class="sousbloc">
               <span class="AuteurNiourf">
                Adaptations (cinéma, télévision, BD, théâtre, radio, jeu vidéo...)
               </span>
               <hr style="color:CCC;"/>
               <span class="ficheNiourf">
                <a href="FicheFilm.asp?idAdapt=2562">
                 Suspense ( Saison 4 - Episode 23 : Summer Night )
                </a>
                , 1952, Robert Stevens &amp; Robert Mulligan (d'après le texte :
                <a href="./EditionsLivre.asp?ID_ItemSommaire=3402">
                 La Nuit d'été
                </a>
                ),
                <i>
                 (Episode Série TV)
                </i>
               </span>
               <br/>
               <span class="ficheNiourf">
                <a href="FicheFilm.asp?idAdapt=2333">
                 Chroniques Martiennes
                </a>
                , 1974, Renée Kammerscheit
                <i>
                 (Téléfilm)
                </i>
               </span>
               <br/>
               <span class="ficheNiourf">
                <a href="FicheFilm.asp?idAdapt=47">
                 Les Chroniques Martiennes
                </a>
                , 1979, Michel Anderson
                <i>
                 (Série)
                </i>
               </span>
               <br/>
               <span class="ficheNiourf">
                <a href="FicheFilm.asp?idAdapt=3075">
                 There Will Come Soft Rains
                </a>
                , 1984 (d'après le texte :
                <a href="./EditionsLivre.asp?ID_ItemSommaire=2453">
                 Il viendra des pluies douces
                </a>
                ),
                <i>
                 (Court Métrage Animation)
                </i>
               </span>
               <br/>
               <span class="ficheNiourf">
                <a href="FicheFilm.asp?idAdapt=2897">
                 Ray Bradbury présente ( Saison 4 - Episode 05 : Usher II )
                </a>
                , 1990, Lee Tamahori (d'après le texte :
                <a href="./EditionsLivre.asp?ID_ItemSommaire=5078">
                 Usher II
                </a>
                ),
                <i>
                 (Episode Série TV)
                </i>
               </span>
               <br/>
               <span class="ficheNiourf">
                <a href="FicheFilm.asp?idAdapt=2893">
                 Ray Bradbury présente ( Saison 4 - Episode 01 : Le Paradis sur Mars )
                </a>
                , 1990, John Laing (d'après le texte :
                <a href="./EditionsLivre.asp?ID_ItemSommaire=5033">
                 La Troisième expédition
                </a>
                ),
                <i>
                 (Episode Série TV)
                </i>
               </span>
               <br/>
               <span class="ficheNiourf">
                <a href="FicheFilm.asp?idAdapt=2900">
                 Ray Bradbury présente ( Saison 4 - Episode 07 : Et la Lune brillera )
                </a>
                , 1990, Randy Bradshaw (d'après le texte :
                <a href="./EditionsLivre.asp?ID_ItemSommaire=1720">
                 Et la lune toujours brillante
                </a>
                ),
                <i>
                 (Episode Série TV)
                </i>
               </span>
               <br/>
               <span class="ficheNiourf">
                <a href="FicheFilm.asp?idAdapt=2904">
                 Ray Bradbury présente ( Saison 4 - Episode 11 : Les longues années )
                </a>
                , 1990, Paul Lynch (d'après le texte :
                <a href="./EditionsLivre.asp?ID_ItemSommaire=2812">
                 Les Longues années
                </a>
                ),
                <i>
                 (Episode Série TV)
                </i>
               </span>
               <br/>
               <span class="ficheNiourf">
                <a href="FicheFilm.asp?idAdapt=2916">
                 Ray Bradbury présente ( Saison 5 - Episode 08 : The Martian )
                </a>
                , 1992, Anne Wheeler (d'après le texte :
                <a href="./EditionsLivre.asp?ID_ItemSommaire=2996">
                 Le Martien
                </a>
                ),
                <i>
                 (Episode Série TV)
                </i>
               </span>
               <br/>
               <span class="ficheNiourf">
                <a href="FicheFilm.asp?idAdapt=2910">
                 Ray Bradbury présente ( Saison 5 - Episode 01 : The Earthmen )
                </a>
                , 1992, Graeme Campbell (d'après le texte :
                <a href="./EditionsLivre.asp?ID_ItemSommaire=2382">
                 Les Hommes de la Terre
                </a>
                ),
                <i>
                 (Episode Série TV)
                </i>
               </span>
               <br/>
               <span class="ficheNiourf">
                <a href="FicheFilm.asp?idAdapt=2926">
                 Ray Bradbury présente ( Saison 6 - Episode 09 : Silent Towns )
                </a>
                , 1992, Lee Tamahori (d'après le texte :
                <a href="./EditionsLivre.asp?ID_ItemSommaire=5218">
                 Les Villes muettes
                </a>
                ),
                <i>
                 (Episode Série TV)
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
           88098 livres, 113966 photos de couvertures, 84564 quatrièmes.
          </td>
         </tr>
         <tr>
          <td class="paragraphecentre">
           11146 critiques, 47555 intervenant·e·s, 2004 photographies, 3926 adaptations.
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
   (function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'9a428e869cdcb71a',t:'MTc2NDA4ODUwMA=='};var a=document.createElement('script');a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();
  </script>
 </body>
</html>
'''


# faut absolument créer une nouvelle entité de type BeautifulSoup pour éviter des conflits
# entre les deux analyses avant d'en extraire les undertags tels que je les veux...

from bs4 import BeautifulSoup as BS
soup = BS(info, "html5lib" )
soup_fiche_livre = soup.select_one("div[id='Fiche_livre']")

if True and soup.select_one("a[class='undertag']"):
  # if present, get all undertag links and add a separator ' | ' between them
    lts_soup = BS('<div style="padding-bottom:0.5em"><span class="AuteurNiourf"> Ouvrages avec une étiquette identique </span><hr style="color:CCC;"/></div>', "lxml")
    lts_soup.select_one("div").append(soup.select_one("a[class='undertag']").find_parent("div"))  # clear the div content to prepare for new content
    print("lts_soup:\n", lts_soup.select_one("div").prettify())
    for i in range(len(lts_soup.select('.undertag'))):
        print(f"i : {i}")
        tag = lts_soup.select('.undertag')[i]
        new_span = lts_soup.new_tag("span")
        new_span.string = " | "
        if i: tag = tag.wrap(new_span)      # add a separator ' | ' between tags except before the first one
        print("tag after:\n", tag)

    print("lts_soup after:\n", lts_soup.select_one("div").prettify())

