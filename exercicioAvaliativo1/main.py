from MotoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI

motoristaDAO = MotoristaDAO()

motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()