**Budjetti sovellus**
### **Viikko1-3**
----------------------------------------------------------------------------------------------------------------
Ohjelmassa on tarkoitus saavuttaa budjetin laadinta ominaisuudet kurssinaikana.
Kurssin loppuunmennessä käyttäjä voi luoda itselleen käyttäjätunnuksen ja luoda omia budjetteja. 

Testattu vuoden 2020 fuksiläppärillä jossa kaikki asennettuna suht-uusimpiin versioihin.
Pythonista käytössä 3.8.5
Voi olla että erilaisilla kokoonpanoilla ilmenee ongelmia. 
Laitoksen etätyöpöydällä poetryä asennettaessa on hyvä seurata materiaalista löytyvää ohjeistusta 
[Tänne](https://python-poetry.org/docs/#installation)

Muista myös tämä terminaalissa  source $HOME/.poetry/env

Github [Release](https://github.com/miksuu00/ot-harjoitustyo/releases/tag/viikko5)
[Arkkitehtuuri.md](https://github.com/miksuu00/ot-harjoitustyo/blob/master/dokumentointi/Arkkitehtuuri.md)

Tämän jälkeen tulee suorittaa juuressa komento 'poetry install'
Sidenote: mikäli tulee virheilmoituksia usein poetry päivitys auttaa eli 'poetry update'ja tämän jälkeen 'poetry install' toimii.

Poetryn tulisi asentaa kaikki vaadittava, mikäli laitteistossa jotain häikkää. Saat asennetteua syöttämällä juuressa käskyn 'poetry add pytest' asennuksen jälkeen voit testailla vaikka poetry shellissä käyttämällä käskyä pytest src <- päivitetty pyproject.toml tiedosto ja asennuksen tulisi toimia suoraviivaisemmin.

Laitoksen koneella tämä toimii src-kansiosta ajettuna.

Lisättynä pylint ja tämän ajaminen juuressa onnistuu käskyllä poetry run invoke lint.
Luotu 2 luokkaa graafista näkymää varten.
Tietokannat työn alla.


Vaatimus määrittelyn löydät seuraamalla allaolevaa linkkiä

[Vaatimusmaarittely](https://github.com/miksuu00/ot-harjoitustyo/blob/master/dokumentointi/vaatimusaarittely.md)

Alta pääset seuraan tuntikirjanpitoa

[Tuntikirjanpito](https://github.com/miksuu00/ot-harjoitustyo/blob/master/dokumentointi/Tuntikirjanpito.md)

* Projektille tehtyjä asioita ja to-do-lista-budget-sovellukseen
  * Testit tehty
  * Tietokantojen lisääminen, ei tehty
  * Jonkinlainen järkevä salasana käsittely




### Omnia mea mecum porto



