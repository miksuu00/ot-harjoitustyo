			## Vaatimusmäärittely - alustava


### Sovelluksen tarkoitus

Sovelluksen avulla käyttäjän on mahdollista tehdä erilaisia budjetointeja, käyttäen hyväksi 
syöttämäänsä dataa. Käyttäjä voi syöttää erilaisia tuloja ja menoja, ja ohjelman valmistuessa
saada tästä visuaalista palautetta erilaisten graafien tai raporttimuotoisten näkymien kautta.
Käyttäjää kiinnostaa mahdollisesti vaikka urakanbudjetointi ja laskelmien tekeminne, sekä kassan
riittäminen.

Myös käytännönläheisemmät kuten kotitalouden suunnittelu onnistuu ja vaikkapa sähkölaskun voi 
lisätä halutessaan. Ohjelma osaa päivittää kassan tilannetta eri ajankohtina näiden lisättyjen
tietojen avulla.
Myös erilaiset ulosviennit (exportit) olisi asiakkaan toiveissa jossain kohtaa.

#### Käyttäjät

Käyttäjäryhmiä luotaisiin alkuun vain yksi roolituksen muodossa, ohjelman toiminnan testauksessa
helpottaa kun itse toiminnot saadaan ensin kuntoon. Myöhemmässä vaiheessa lisätään pääkäyttäjä
oikeuksia jotka pääsevät näkemään myös muiden tekemiä raportteja sekä laskettuja budjetteja.

Arvioitu käyttöliittymäluonnos

![Näkymä hahmotelma](https://github.com/miksuu00/ot-harjoitustyo/blob/master/dokumentointi/kaava.png)

#### Perusversiosta saatavia toiminnallisuuksia

* Alkunäyttö
  * Luodaan oma käyttäjätunnus ja profiili
  * Alkunäytöllä voi myös kirjautua suoraan sisään
 
* Kirjautumisen jälkeen
  * Käyttäjä voi katsoa valita tekemänsä budjetin
  * Käyttäjän luoma budjetti näkyy vain hänelle sekä super-user oikeuksilla oleville
  * Käyttäjä voi merkitä budjetin onnistuneeksi, sekä mahdollisesti poistaa budjettiluonnoksen
  * Käyttäjä voi kirjautua ulos sovelluksesta

#### Jatkokehitysajatuksia

* Raporttien (budjettien) exporttaus eri tiedostomuotoja hyödyntäen
* ICS ulosvienti tärkeiden tapahtumien osalta budjetin sisältämien vaatimusten pohjalta
* Usean käyttäjän näkymä samaan budjettiin rajatuin/sallituin käyttöoikeuksin
* Graafisia kaavioita
* Ennusteita budjetoinnin pohjalta
* Tulevia hankintoja vapaalla mutta rajatulla aikavälillä ymmärtävä ominaisuus
* Omien suunnitelmien muokkaus
* Omien luomien budjettien poisto

