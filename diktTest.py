
class Test:
    def __init__(self, navn):
        self._navn = navn

    def _str_(self):
        linje = "Mitt navn: " + self._navn
        return linje

        
ordbok = {}
for i in range(5):
    test = Test("hei" + str(i))
    ordbok[test] = i



#_sanger = [object1, object2, object3] # objecter av type Sang
print(ordbok)
