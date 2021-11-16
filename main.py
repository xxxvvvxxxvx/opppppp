class Transportlidzeklis:

  krasa= 'Melna'

  def __init__(self, nosaukums, max_atrums, nobraukums):
    self.nosaukums = nosaukums
    self.max_atrums = max_atrums
    self.nobraukums = nobraukums
  
  def sedvietu_skaits(self, skaits):
    self.skaits=skaits
    return f"sedvietu skaits {self.nosaukums} Ir {self.skaits}"

def.biletes(self):
  return self.skaits= 0.5


modelisx= Transportlidzeklis('Volkswagen',100, 5000)
print(modelisx.max_atrums, modelisx.nobraukums, modelisx.nosaukums)

class bus(Transportlidzeklis):
  def sedvietu_skaits(self, skaits = 2)
    return super().sedvietu_skaits(skaits)

  def biletes(self):
    return super().biletes()


modelisx= bus("Koeningsegg", 490, 126)
print(modelisx.max_atrums, modelisx.nobraukums, modelisx.nosaukums)

p_bus= bus('Acura', 250, 9000)
print(p_bus.sedvietu_skaits(6))
print(modelisx.max_atrums, modelisx.nobraukums, modelisx.nosaukums, modelisx.krasa)
print(modelisx.biletes())