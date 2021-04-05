import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_saldo_uudessa_kassassa(self):
        self.kassassa = self.kassapaate.kassassa_rahaa

        self.assertEqual(self.kassassa, 100000)
    def test_maukkaat_lounaat_nolla_uudessa_kassassa(self):
        self.assertIs(self.kassapaate.maukkaat,0)
    
    def test_edulliset_lounaat_nolla_uudessa_kassassa(self):
        self.assertIs(self.kassapaate.edulliset, 0)

    def test_maukkaasti_kateisella(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400),0)
    
    def test_maukkaasti_kateisella_ja_saa_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500),100)  

    def test_edullisesti_kateisella(self):

        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240),0)  

    def test_edullisesti_kateisella_ja_saa_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500),260)

    def test_lounas_laskuri_kasvaa_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertIs(self.kassapaate.edulliset, 1)

    def test_lounas_laskuri_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertIs(self.kassapaate.maukkaat,2)
    
    def test_raha_ei_riita_edulliseen_lounaaseen_lounas_laskuri_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(1);
        self.assertIs(self.kassapaate.edulliset, 0)

    def test_raha_ei_riita_maukkaaseen_lounaaseen_lounas_laskuri_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(1);
        self.assertIs(self.kassapaate.maukkaat, 0)

    def test_raha_ei_riita_edulliseen_luonaaseen_raha_palautetaan_oikein(self):
        
        self.assertIs(self.kassapaate.syo_edullisesti_kateisella(2),2)

    def test_raha_ei_riita_maukkaaseen_luonaaseen_raha_palautetaan_oikein(self):
        
        self.assertIs(self.kassapaate.syo_maukkaasti_kateisella(2),2)
    
    
    def test_raha_ei_riita_maukkaaseen_lounaaseen_kassan_saldo_ei_kasva(self):
        self.kassan_saldo = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_maukkaasti_kateisella(30)
        self.assertEqual(self.kassan_saldo, self.kassapaate.kassassa_rahaa)

    def test_raha_ei_riita_edulliseen_lounaaseen_kassan_saldo_ei_kasva(self):
        self.kassan_saldo = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kateisella(30)
        self.assertEqual(self.kassan_saldo, self.kassapaate.kassassa_rahaa)
    
    def test_kortti_osto_maukas_toimii(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)) 

    def test_kortti_osto_maukas_laskuri_kasvaa(self):
        
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertIs(self.kassapaate.maukkaat, 2)
       
    def test_kortti_osto_edullisesti_toimii(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))     

    def test_kortti_osto_edullisesti_laskuri_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertIs(self.kassapaate.edulliset, 1)

    def test_kortti_ei_riitä_maukas(self):
        self.maksukortti.ota_rahaa(800)
        saldo =self.maksukortti.saldo
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(saldo, 200)

    def test_kortti_ei_riitä_edullinen(self):
        self.maksukortti.ota_rahaa(820)
        
        self.kassapaate.syo_edullisesti_kortilla
        self.assertEqual(self.maksukortti.saldo, 180)
        
    def test_kortti_ei_riitä_maukas_laskuri_ei_kasva(self):
        self.maksukortti.ota_rahaa(800)
      
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortti_ei_riitä_edullinen_laskuri_ei_kasva(self):
        self.maksukortti.ota_rahaa(800)
      
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortti_ei_riita_maukas_palauta_false(self):
        self.maksukortti.ota_rahaa(900)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_kortti_ei_riita_edullinen_palauta_false(self):
        self.maksukortti.ota_rahaa(900)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
    
    def test_kortti_ei_riita_maukas_kortin_raha_ei_muutu(self):
        self.maksukortti.ota_rahaa(800)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 200)

    def test_kortti_ei_riita_edullinen_kortin_raha_ei_muutu(self):
        self.maksukortti.ota_rahaa(800)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 200)

    def test_kassan_rahamaara_ei_muutu_kortti_maukas(self):
        
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(100000, self.kassapaate.kassassa_rahaa)

    def testaa_kassan_rahamaara_ei_muutu_kortti_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(100000, self.kassapaate.kassassa_rahaa)

    def test_ladataan_rahaa_kortille_kortin_saldo_kasvaa(self):
        
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 5000)
        self.assertEqual(6000,self.maksukortti.saldo)

    def test_ladataan_rahaa_kortille_kassan_saldo_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertNotEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_ladataan_negatiivinen_summa_kortille_kassan_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -56)
        self.assertEqual(100000, self.kassapaate.kassassa_rahaa)
