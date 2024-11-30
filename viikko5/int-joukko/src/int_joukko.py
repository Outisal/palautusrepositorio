KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin tulee olla positiivinen kokonaisluku")
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Kasvatuskoon tulee olla positiivinen kokonaisluku")
        
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.alkiot = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, numero):
        return numero in self.alkiot[:self.alkioiden_lkm]

    def lisaa(self, numero):
        if self.kuuluu(numero):
            return False
        if self.alkioiden_lkm >= (self.kapasiteetti - 1):
            self.laajenna_lista()
        self.alkiot[self.alkioiden_lkm] = numero
        self.alkioiden_lkm += 1
        return True
    
    def laajenna_lista(self):
        uusi_lista = self._luo_lista(len(self.alkiot) + self.kasvatuskoko)
        for i in range(self.alkioiden_lkm):
            uusi_lista[i] = self.alkiot[i]
        self.alkiot = uusi_lista
    
    def poista(self, numero):
        for i in range(self.alkioiden_lkm):
            if self.alkiot[i] == numero:
                for j in range(i, self.alkioiden_lkm):
                    self.alkiot[j] = self.alkiot[j + 1]
                self.alkioiden_lkm -= 1
                self.alkiot[self.alkioiden_lkm] = 0
                return True
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.alkiot[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(lista1, lista2):
        tulos = IntJoukko()
        for numero in lista1.to_int_list() + lista2.to_int_list():
            tulos.lisaa(numero)
        return tulos

    @staticmethod
    def leikkaus(lista1, lista2):
        tulos = IntJoukko()
        for numero in lista1.to_int_list():
            if lista2.kuuluu(numero):
                tulos.lisaa(numero)
        return tulos

    @staticmethod
    def erotus(lista1, lista2):
        tulos = IntJoukko()
        for numero in lista1.to_int_list():
            if not lista2.kuuluu(numero):
                tulos.lisaa(numero)
        return tulos

    def __str__(self):
        alkiot_merkkijonona = ", ".join(map(str, self.to_int_list()))
        return f"{{{alkiot_merkkijonona}}}"
