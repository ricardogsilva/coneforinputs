from sextante.core.AlgorithmProvider import AlgorithmProvider
from sextante.core.SextanteConfig import Setting, SextanteConfig

from sextanteconeforinputs import ConeforInputsProcessor
#from sextanteconefor import ConeforProcessor

class SextanteConeforProvider(AlgorithmProvider):

    _name = 'Conefor Provider'
    A_TESTING_SETTING = 'My_testing_setting'

    def __init__(self):
        super(SextanteConeforProvider, self).__init__()
        self.algList = [
            ConeforInputsProcessor(),
            #ConeforProcessor,
        ]
        for alg in self.algList:
            alg.provider = self

    def initializeSettings(self):
        '''
        '''

        super(SextanteConeforProvider, self).initializeSettings()
        SextanteConfig.addSetting(
            Setting('Something about the Conefor Provider',
                    self.A_TESTING_SETTING,
                    'Some text',
                    'And more text')
        )

    def unload(self):
        super(SextanteConeforProvider, self).unload()
        SextanteConfig.removeSetting(self.A_TESTING_SETTING)

    def getName(self):
        return self._name

    def getIcon(self):
        super(SextanteConeforProvider, self).getIcon()

    def loadAlgorithms(self):
        self.algs = self.algList
