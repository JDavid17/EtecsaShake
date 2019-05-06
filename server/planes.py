class Plan:
    def __init__(self, p=0, v=0, s=0, d=0):
        self.Price = p
        self.Voice = v
        self.Sms = s
        self.Data = d

    def __str__(self):
        if self.Voice + self.Sms + self.Data == self.Voice:
            return f'Plan de Voz de {self.Voice} mnts a {self.Price} cuc'
        elif self.Voice + self.Sms + self.Data== self.Sms:
            return f'Plan de SMS de {self.Sms} sms a {self.Price} cuc'
        elif self.Voice + self.Sms + self.Data== self.Data:
            return f'Plan de Datos de {self.Data} MGs a {self.Price} cuc'
        return f'Plan de {self.Voice} mnts, {self.Sms} sms y {self.Data} MGs a {self.Price} cuc'

planes = [
    Plan(7.0, d=600), 
    Plan(10.0, d=1000),
    Plan(20.0, d=2500), 
    Plan(30.0, d=4000),
    Plan(1.5, v=5), 
    Plan(2.9, v=10),
    Plan(4.2, v=15), 
    Plan(6.5, v=25),
    Plan(10.0, v=40), 
    Plan(.7, s=10),
    Plan(1.3, s=20), 
    Plan(2.1, s=35),
    Plan(2.5, s=45)
]

cnt_planes = len(planes)