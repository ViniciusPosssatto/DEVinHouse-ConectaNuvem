class Media:

    def __init__(self, av1: float, av2: float ):
        self.__av1 = av1
        self.__av2 = av2
        self.__media = self.__calcular_media(self.__av1, self.__av2)

    @staticmethod
    def __calcular_media(av1: float, av2: float):
        return (av1 + av2) / 2

    @property
    def media(self):
        return self.media
