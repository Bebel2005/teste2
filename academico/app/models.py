from django.db import models

class Ocupacao(models.Model):
    nome = models.CharField(max_length=70)
    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    def __str__(self):
        return f"{self.nome}, {self.uf}"

class Pessoa(models.Model):
    nome = models.CharField(max_length=70)
    pai = models.CharField(max_length=60)
    mae = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11, unique=True)
    data_nasc = models.DateField()
    email = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11, unique=True)
    def __str__(self):
     return self.nome

class Area(models.Model):
    nome = models.CharField(max_length=70)
    def __str__(self):
     return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    def __str__(self):
     return self.nome

class Semestre(models.Model):
    periodo = models.IntegerField()
    def __str__(self):
     return self.periodo

class Disciplina(models.Model):
    nome = models.CharField(max_length=70)
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE)
    def __str__(self):
     return self.nome

class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()
    def __str__(self):
     return self.pessoa

class Tipo_avaliacao(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
     return self.nome
 
class Avaliacao(models.Model):
    descricao = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tipo_avaliacao = models.ForeignKey(Tipo_avaliacao, on_delete=models.CASCADE)
    def __str__(self):
     return self.tipo_avaliacao

class Frequencia(models.Model):
 curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
 disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
numero_faltas = models.IntegerField()
def __str__(self):
 return self.numero_faltas

class Turma(models.Model):
    nome = models.CharField(max_length=70)
    periodo_semestre = models.CharField(max_length=70)
    def __str__(self):
     return self.nome

class Advertencia(models.Model):
    descricao = models.CharField(max_length=200)
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    def __str__(self):
     return self.descricao

class Disciplina_curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    def __str__(self):
     return self.nome

