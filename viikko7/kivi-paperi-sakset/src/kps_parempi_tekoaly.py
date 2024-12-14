from kps import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self, muistin_koko = 10):
        self.tekoaly = TekoalyParannettu(muistin_koko)

    def _toisen_siirto(self, ekan_siirto):

        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self.tekoaly.aseta_siirto(ekan_siirto)
        
        return tokan_siirto