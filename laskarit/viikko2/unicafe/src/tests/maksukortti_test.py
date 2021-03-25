import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(50)
        self.assertEqual(self.maksukortti.saldo, 60)
    
    def test_ota_rahaa_yksi_euro(self):
        
        self.assertTrue(self.maksukortti.ota_rahaa(1))

    def test_ota_enempi_kuin_saldoa_piisaa_ja_saldo_ei_muutu(self):
        self.saldoa = self.maksukortti.saldo 
        self.maksukortti.ota_rahaa(15)
        self.assertEqual(self.saldoa, self.maksukortti.saldo)
    
    def test_saldo_vahenee_oikein_kun_saldo_riittaa(self):
        self.maksukortti.ota_rahaa(7)
        self.assertEqual(3, self.maksukortti.saldo)
    def test_metodi_palauttaa_true_jos_alles_klar(self):
        self.assertTrue(self.maksukortti.ota_rahaa(5))
    def test_metodi_palauttaa_false_jos_alles_inte_klar(self):
        self.assertFalse(self.maksukortti.ota_rahaa(100))
    def test_saldo_ilmoitetaan_vekkulisti(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")