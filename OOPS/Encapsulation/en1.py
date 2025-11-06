class Students:
    def __init__(self,name,rank,points):
        self.name =name
        self.rank =rank
        self.points = points

    def demofuc(self):
        print("I am "+self.name)
        print("I got rank",+self.rank)

st1 = Students("kishore",1,100)
st2 = Students("Ram",2,90)

st1.demofuc()
st2.demofuc()