# =============================================================================
# Preiskovanje dreves
#
# Dan je razred `Drevo`, ki predstavlja dvojiško drevo. Konstruktor je že
# implementiran; prav tako metodi `__repr__` in `__eq__`. Drevo na spodnji
# (ASCII art) sliki:
# 
#          5
#        /   \
#       3     2
#      /     / \
#     1     6   9
# 
# sestavimo takole:
# 
#     >>> d = Drevo(5,
#                   levo=Drevo(3, levo=Drevo(1)),
#                   desno=Drevo(2, levo=Drevo(6), desno=Drevo(9)))
# =====================================================================@005912=
# 1. podnaloga
# Razredu dodajte metodo `vsota(self)`, ki vrne vsoto vseh števil v
# drevesu. Zgled (kjer je `d` kot zgoraj):
# 
#     >>> d.vsota()
#     26
# =============================================================================
class Drevo:

    def __init__(self, *args, **kwargs):
        if args:
            self.prazno = False
            self.vsebina = args[0]
            self.levo = kwargs.get('levo', Drevo())
            self.desno = kwargs.get('desno', Drevo())
        else:
            self.prazno = True

    def __repr__(self, zamik=''):
        if self.prazno:
          return 'Drevo()'.format(zamik)
        elif self.levo.prazno and self.desno.prazno:
          return 'Drevo({1})'.format(zamik, self.vsebina)
        else:
          return 'Drevo({1},\n{0}      levo = {2},\n{0}      desno = {3})'.\
            format(
              zamik,
              self.vsebina,
              self.levo.__repr__(zamik + '             '),
              self.desno.__repr__(zamik + '              ')
            )

    def __eq__(self, other):
        return ((self.prazno and other.prazno) or
                (not self.prazno and not other.prazno and
                 self.vsebina == other.vsebina and
                 self.levo == other.levo and
                 self.desno == other.desno))

    def obhod(self):
        """Generator, ki naredi obhod LKD"""
        if not self.prazno:
            for i in self.levo.obhod():
                yield i
            yield self.vsebina
            for i in self.desno.obhod():
                yield i
    # def vsota(self):
    #     return sum(self.obhod())
    def vsota(self):
        if self.prazno:
            return 0
        else:
            return self.vsebina + self.desno.vsota() + self.levo.vsota()
# =====================================================================@005913=
# 2. podnaloga
# Dodajte metodo `stevilo_listov(self)`, ki vrne število listov v drevesu.
# Zgled (kjer je `d` kot zgoraj):
# 
#     >>> d.stevilo_listov()
#     3
# =============================================================================
    def stevilo_listov(self):
           if self.prazno:
               return 0
           elif self.levo.prazno and self.desno.prazno:
               return 1
           else:
               return self.levo.stevilo_listov() + self.desno.stevilo_listov()
# =====================================================================@005914=
# 3. podnaloga
# Dodajte metodo `minimum(self)`, ki vrne najmanjše število v drevesu.
# Če je drevo prazno, naj metoda vrne `None`. Zgled (kjer je `d` kot
# zgoraj):
# 
#     >>> d.minimum()
#     1
#     >>> Drevo().minimum()
#     None
# =============================================================================
    def minimum(self):
        return min(self.obhod()) if not self.prazno else None
# =====================================================================@005915=
# 4. podnaloga
# Sestavite metodo `premi_pregled(self)`, ki vrne generator, ki vrača
# _vsebino_ vozlišč drevesa v _premem vrstnem redu_ (pre-order). To pomeni,
# da najprej obiščemo koren drevesa, nato levo poddrevo in na koncu še
# desno poddrevo. Vozlišča poddreves obiskujemo po enakem pravilu. Zgled:
# 
#     >>> [x for x in d.premi_pregled()]
#     [5, 3, 1, 2, 6, 9]
# 
# Opomba: Za več podrobnosti o pregledovanju dreves si lahko ogledate
# članek [Tree traversal](http://en.wikipedia.org/wiki/Tree_traversal)
# na Wikipediji.
# =============================================================================
    def premi_pregled(self):
        """Pregled KLD"""
        if not self.prazno:
            yield self.vsebina
            for i in self.levo.premi_pregled():
                yield i
            for i in self.desno.premi_pregled():
                yield i
# =====================================================================@005916=
# 5. podnaloga
# Sestavite metodo `vmesni_pregled(self)`, ki vrne generator, ki vrača
# _vsebino_ vozlišč drevesa v _vmesnem vrstnem redu_ (in-order). To pomeni,
# da najprej obiščemo levo poddrevo, nato koren drevesa in na koncu še
# desno poddrevo. Vozlišča poddreves obiskujemo po enakem pravilu. Zgled:
# 
#     >>> [x for x in d.vmesni_pregled()]
#     [1, 3, 5, 6, 2, 9]
# =============================================================================
    def vmesni_pregled(self):
        """LKD obhod"""
        if not self.prazno:
            for i in self.levo.vmesni_pregled():
                yield i
            yield self.vsebina
            for i in self.desno.vmesni_pregled():
                yield i
# =====================================================================@005917=
# 6. podnaloga
# Sestavite metodo `po_nivojih(self)`, ki vrne generator, ki vrača
# _vsebino_ vozlišč drevesa _po nivojih_ (level-order). To pomeni, da
# najprej obiščemo koren, nato vsa vozlišča, ki so na globini 1, nato
# vsa vozlišča, ki so na globini 2 itn. Vsa vozlišča na isti globini
# naštejemo od leve proti desni. Zgled:
# 
#     >>> [x for x in d.po_nivojih()]
#     [5, 3, 2, 1, 6, 9]
# =============================================================================
    def po_nivojih(self, vrsta = []):
        """BFS generator"""
        if not self.prazno:
            yield self.vsebina
            vrsta += [self.levo, self.desno]
        if vrsta:
            drevo = vrsta.pop(0)
            for x in drevo.po_nivojih(vrsta=vrsta):
                yield x
    
    def po_nivojih(self):
        vrsta = [self]
        while vrsta:
            drevo = vrsta.pop(0)
            if not drevo.prazno:
                yield drevo.vsebina
                vrsta.append(drevo.levo)
                vrsta.append(drevo.desno)
