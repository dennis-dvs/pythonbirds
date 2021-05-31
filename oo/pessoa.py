class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Renzo')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.idade)
    for filhos in luciano.filhos:
        print(filhos.nome)
    luciano.sobrenome = 'Ramalho'  # Não é uma boa prática fazer em tempo de execução
    del luciano.filhos  # Tanto criação e exclusão devido a dificuldade de entender o código
    luciano.olhos = 1
    del luciano.olhos  # Aqui será apagado o atributo do objeto mais o valor da classe retornará a aparecer
    print(luciano.__dict__)  # __dict__ Mantem apenas referencias para os atributos de instâncias...
    print(renzo.__dict__)  # ...não para atributos de classes por ex.: olhos. Se forem alterados ele aparece
    # print(Pessoa.nome)   # Neste caso não tem sentido já que tem várias classes referenciadas não pelo atributo
    # mais sim pelo seu conteúdo
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), luciano.nome_e_atributo_de_classe())
