#Facilidades
Faci = 'A', 'B', 'C', 'D'
#Clientes
Client  = range(1, 10)

#custo para abrir a facilidade
FixCost = dict(A=500, B=600, C=700, D=800)

# Capacidade de uma instalação em cada local
Capacity = dict(A=40, B=55, C=73, D=90)

#Demanda de cada cliente
Demand = {1:10, 2:14, 3:17, 4:8, 5:9, 6:12, 7:11, 8:15, 9:16}

# custo de transporte de cada facilidade para cada cliente 
Transportation = dict(
  A = {1:55, 2: 4, 3:17, 4:33, 5:47, 6:98, 7:19, 8:10, 9: 6},
  B = {1:42, 2:12, 3: 4, 4:23, 5:16, 6:78, 7:47, 8: 9, 9:82}, 
  C = {1:17, 2:34, 3:65, 4:25, 5: 7, 6:67, 7:45, 8:13, 9:54},
  D = {1:60, 2: 8, 3:79, 4:24, 5:28, 6:19, 7:62, 8:18, 9:45}
)
