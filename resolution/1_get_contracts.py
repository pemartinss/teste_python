import os
import sys
sys.path.insert(1, os.getcwd())
from functions.Contracts import Contract,Contracts

#Passa os paramêtros necessários para a classe Orders (contracts,renegotiated,top_n)
c = Contracts([
    Contract(1, 1),
    Contract(2, 2),
    Contract(3, 3),
    Contract(4, 4),
    Contract(5, 5)
],[3],3)

#Lista de contratos que devem ser retornados pelo método
expected_open_contracts = [5, 4, 2]

actual_open_contracts = c.get_top_N_open_contracts()
assert expected_open_contracts == actual_open_contracts

