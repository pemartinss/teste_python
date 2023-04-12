class Orders:
    '''
    Reúne propriedades que serão utilizadas pelo método.

    Attributes
    ----------
    requests : list
            Lista contendo os valores requisitados.
    n_max : list
            Valor máximo que pode ser levado por viagem.
    '''

    def __init__(self,requests,n_max):
        self.requests = requests
        self.n_max = n_max

    def combine_orders(self):
        '''
        Retorna o número mínimo de viagens necessário para atender todas as requisições.

        Attributes
        ----------
        requests : list
            Lista contendo o valor requisitado por agências próximas.
        n_max : int
            Valor máximo que pode ser levado por viagem.

        Returns
        -------
        num_viagens : int
            Número inteiro indicando o número mínimo de viagens que deve ser realizado para atender todas as requisições.
        '''
        try:
            num_viagens = 0
            qtd_soma = 0
            #Indices que serão utilizados para percorrer toda a lista
            i = 0
            j = len(self.requests) - 1
            while i <= j:
                if self.requests[i] + self.requests[j] <= self.n_max and qtd_soma == 0:
                    i += 1
                    j -= 1
                    qtd_soma += 1
                else:
                    j -= 1
                num_viagens += 1
            return num_viagens
        except Exception as Argument:
            raise ValueError(f'Erro ao calcular o número minímo de viagens. Erro: {str(Argument)}')