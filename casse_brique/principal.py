from Brique import Brique
from brique_speciale import BriqueSpeciale
from CasseBriques import CasseBriques
from CasseBriquesGUI import CasseBriquesGUI

cb = CasseBriques()
cb.construire_rangee_briques("red", 1, 10, 13)
cb.construire_rangee_briques("blue", 1, 10, 10, 5, 2)
cb.construire_rangee_briques("green", 1, 10, 11, 5, 3)

gui = CasseBriquesGUI(cb)
gui.demarrer()