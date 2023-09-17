class TaifaStar:
    def __init__(self, country, type, gender):
        self.country = country
        self.type = type
        self.gender = gender
    
    def compete(self):
        print('Today is world cup qualifier')


class FirstTeam(TaifaStar):
    print('This is the best Team')
        

SerengetiGirls = FirstTeam('Tanzania' , 'Youth', 'F')
NgorongoroHeros = FirstTeam('Uganda', 'YOUTh', 'M')


SerengetiGirls.compete()