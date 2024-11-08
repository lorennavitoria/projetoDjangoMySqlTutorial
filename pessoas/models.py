from django.db import models

class Pessoas(models.Model):
    #id = models.AutoField(primary_key=True)    O DJANGO CRIA AUTOMATICAMENTE O ID NO BANCO, A MENOS QUE QUEIRA PERSONALIZAR O NOME OU CONFIGURAÇÕES DA CHAVE PRIMÁRIA
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    dataNascimento = models.DateField()
    mae = models.CharField(max_length=100)


    '''Esse método retorna o nome e matrícula da pessoa quando o objeto for impresso ou exibido. Esse método é útil para representações legíveis no Django Admin ou quando um objeto é listado.'''
    def __str__(self):
        return f"{self.pessoa.nome} - {self.matricula}"  # Para a classe Alunos


'''
Relacionamento de muitos para um com a classe Pessoas, ou seja, um cliente é uma pessoa. A chave estrangeira (ForeignKey) mapeia esse relacionamento, com a ação on_delete=models.CASCADE, o que significa que se a pessoa for deletada, o cliente também será.

'''
class Clientes(models.Model):
    #id = models.AutoField(primary_key=True)
    #O valor default=1 atribuído nas chaves estrangeiras (pessoa) faz com que, caso não seja passado um valor explícito, a pessoa com id=1 seja associada.
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE, default=1)  # Usando um valor de ID de pessoa como padrão
    dataDeCadastro = models.DateField()
    status = models.CharField(max_length=10)


    def __str__(self):
        return self.id


class Alunos(models.Model):
    #id = models.AutoField(primary_key=True)
    #pessoa: Relacionamento de muitos para um com a classe Pessoas, indicando que um aluno é uma pessoa.
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE, default=1)  # Usando um valor de ID de pessoa como padrão
    matricula = models.IntegerField()
    anoIngresso = models.IntegerField()

    def __str__(self):
        return self.matricula


class Professores(models.Model):
    #id = models.AutoField(primary_key=True)
    #pessoa: Relacionamento de muitos para um com a classe Pessoas, indicando que um professor é uma pessoa.
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE, default=1)  # Usando um valor de ID de pessoa como padrão
    areaDeAtuacao = models.CharField(max_length=45)
    numeroDeRegistro = models.IntegerField()


    def __str__(self):
        return self.numeroDeRegistro



'''
- Todos os relacionamentos são feitos por meio da chave estrangeira ForeignKey, o que é correto e segue o diagrama de entidade e relacionamento.

-O uso de on_delete=models.CASCADE é uma escolha adequada quando a exclusão de uma pessoa deve resultar na exclusão de um cliente, aluno ou professor associado. Contudo, é importante revisar se em seu caso isso é realmente o desejado (se você quer excluir essas entidades quando uma pessoa for deletada ou se deseja que elas sejam mantidas com a pessoa em um estado nulo).


'''