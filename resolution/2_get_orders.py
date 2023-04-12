import os
import sys
sys.path.insert(1, os.getcwd())
from functions.Orders import Orders

#Passa os paramêtros necessários para a classe Orders (requests,n_max)
o = Orders([70, 30, 10],100)

#Número esperado de viagens a ser retornado pelo método
expected_orders = 2

how_many = o.combine_orders()
assert how_many == expected_orders




