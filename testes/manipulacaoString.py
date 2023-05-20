print("Tentativa")

# Nome: Allan
print("Nome: {}".format("Allan"))

# Nome: Allan, Idade: 25
print("Nome: {1}, Idade: {0}".format(25, "Allan"))

# R$ 1.34
print("R$ {}".format(1.34))

# R$ 1.340000
print("R$ {:f}".format(1.34))

# R$ 1.30
print("R$ {:.2f}".format(1.3))

# R$   1.30
print("R$ {:6.2f}".format(1.3))

# R$ 004.00
print("R$ {:06.2f}".format(4))

# Data 05/06
print("Data {:02d}/{:02d}".format(5, 6))