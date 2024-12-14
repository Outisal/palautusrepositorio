from kps import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self._siirto = ["k", "p", "s"]
        self._indeksi = 0

    def _toisen_siirto(self, ekan_siirto):
        self._indeksi = self._indeksi + 1
        self._indeksi = self._indeksi % 3

        tokan_siirto = self._siirto[self._indeksi]
        print(f"Tietokone valitsi: {tokan_siirto}")
        
        return tokan_siirto