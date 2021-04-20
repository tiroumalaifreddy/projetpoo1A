class Jointure_vertical():
    def __init__(self, data_un, data_deux):
        self.data_un = data_un
        self.data_deux = data_deux

    def fusion_v(self):
        data_fusion=[]
        if len(self.data_deux) == len(self.data_un):
            for i in range(len(self.data_un)):
                data_fusion.append(self.data_un[i] + self.data_deux[i])
        return data_fusion