class Contract:
    '''
    Cria uma lista com os ids e os débitos dos clientes que possuem contratos em aberto.

    Attributes
    ----------
    id : int
        Identificador único de cada cliente.
    debt : int
        Valor total do débito de cada cliente.
    Returns
    -------
    Contract: string
        String contendo id e débito, no formato: (id,debt)
    '''
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)

class Contracts:
    '''
    Reúne propriedades que serão utilizadas pelo método.

    Attributes
    ----------
    contracts : list
            Lista contendo os identificadores dos clientes que possuem contratos em aberto.
    renegotiated : list
            Lista contendo os identificadores dos clientes que renegociaram seus contratos.
    top_n : int
            Número de contratos que devem ser retornados.
    '''

    def __init__(self,contracts, renegotiated, top_n):
        
        self.contracts = contracts
        self.renegotiated = renegotiated
        self.top_n = top_n

    def get_top_N_open_contracts(self):
        '''
        Retorna o número de contratos em aberto, ordenando do maior devedor para o menor.

        Parameters
        ----------
        contracts : list
            Lista contendo os identificadores dos clientes que possuem contratos em aberto.
        renegotiated : list
            Lista contendo os identificadores dos clientes que renegociaram seus contratos.
        top_n : int
            Número de contratos que devem ser retornados pelo método.

        Returns
        -------
        actual_open_contracts : List
            Lista contendo os ids dos clientes devedores, respeitando o número de contratos em top_n
        '''
        try:
           if not self.contracts:
             raise ValueError('Não há contratos em aberto na lista passada.')
           actual_open_contracts = []
           for contract in self.contracts:
                if contract.id not in self.renegotiated:
                    actual_open_contracts.append(tuple((contract.id,contract.debt)))
           actual_open_contracts.sort(key = lambda x:x[1], reverse = True)
           return [i[0] for i in actual_open_contracts][:self.top_n]
        except Exception as Argument:
            raise ValueError(f'Erro ao gerar os contratos em aberto. Erro: {str(Argument)}')
