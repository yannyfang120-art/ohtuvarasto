import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_nollataan(self):
        v = Varasto(-1)
        self.assertAlmostEqual(v.tilavuus, 0)

    def test_negatiivinen_alkusaldo_nollataan(self):
        v = Varasto(10, -5)
        self.assertAlmostEqual(v.saldo, 0)

    def test_alkusaldo_yli_tilavuuden_rajataan(self):
        v = Varasto(10, 15)
        self.assertAlmostEqual(v.saldo, 10)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        v = Varasto(10, 5)
        v.lisaa_varastoon(-3)
        self.assertAlmostEqual(v.saldo, 5)

    def test_liian_suuri_lisays_tayttaa_varaston(self):
        v = Varasto(10, 5)
        v.lisaa_varastoon(20)
        self.assertAlmostEqual(v.saldo, 10)

    def test_negatiivinen_otto_palauttaa_nollan(self):
        v = Varasto(10, 5)
        self.assertAlmostEqual(v.ota_varastosta(-2), 0)
        self.assertAlmostEqual(v.saldo, 5)

    def test_liian_suuri_otto_palauttaa_kaiken_ja_tyhjentaa(self):
        v = Varasto(10, 5)
        self.assertAlmostEqual(v.ota_varastosta(20), 5)
        self.assertAlmostEqual(v.saldo, 0)

    def test_str(self):
        v = Varasto(10, 4)
        self.assertEqual(str(v), "saldo = 4, vielä tilaa 6")
