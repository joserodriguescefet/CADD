# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aluno(models.Model):
    id = models.BigAutoField(primary_key=True)
    matricula = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=255, blank=True, null=True)
    datanascimento = models.DateTimeField(db_column='dataNascimento', blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(max_length=255, blank=True, null=True)
    uf = models.CharField(db_column='UF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=255, blank=True, null=True)
    rua = models.CharField(max_length=255, blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    historico = models.ForeignKey('Historicoescolar', models.DO_NOTHING, blank=True, null=True)
    versaocurso = models.ForeignKey('Versaocurso', models.DO_NOTHING, db_column='versaoCurso_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aluno'


class Blocoequivalencia(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'blocoequivalencia'


class Curso(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    sigla = models.CharField(max_length=255, blank=True, null=True)
    coordenador = models.ForeignKey('Professor', models.DO_NOTHING, blank=True, null=True)
    coordenadoratividadescomplementares = models.ForeignKey('Professor', models.DO_NOTHING, db_column='coordenadorAtividadesComplementares_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curso'


class CursoDisciplina(models.Model):
    curso = models.ForeignKey(Curso, models.DO_NOTHING)
    disciplinas = models.ForeignKey('Disciplina', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'curso_disciplina'


class Departamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    sigla = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'


class DepartamentoDisciplina(models.Model):
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING, primary_key=True)
    disciplinas = models.ForeignKey('Disciplina', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'departamento_disciplina'
        unique_together = (('departamento', 'disciplinas'),)


class DepartamentoProfessor(models.Model):
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING, primary_key=True)
    professores = models.ForeignKey('Professor', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'departamento_professor'
        unique_together = (('departamento', 'professores'),)


class Disciplina(models.Model):
    id = models.BigAutoField(primary_key=True)
    cargahoraria = models.IntegerField(db_column='cargaHoraria')  # Field name made lowercase.
    codigo = models.CharField(max_length=255, blank=True, null=True)
    ehoptativa = models.TextField(db_column='ehOptativa', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nome = models.CharField(max_length=255, blank=True, null=True)
    quantidadecreditos = models.IntegerField(db_column='quantidadeCreditos', blank=True, null=True)  # Field name made lowercase.
    versaocurso = models.ForeignKey('Versaocurso', models.DO_NOTHING, db_column='versaoCurso_id', blank=True, null=True)  # Field name made lowercase.
    alocacao_depto = models.ForeignKey(Departamento, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplina'


class DisciplinaPrereqs(models.Model):
    grade = models.ForeignKey('Gradedisponibilidade', models.DO_NOTHING, primary_key=True)
    disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'disciplina_prereqs'
        unique_together = (('grade', 'disciplina'),)


class DisciplinasEquivalentes(models.Model):
    bloco = models.ForeignKey(Blocoequivalencia, models.DO_NOTHING, primary_key=True)
    disciplinasequivalentes = models.ForeignKey(Disciplina, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'disciplinas_equivalentes'
        unique_together = (('bloco', 'disciplinasequivalentes'),)


class DisciplinasOriginais(models.Model):
    bloco = models.ForeignKey(Blocoequivalencia, models.DO_NOTHING, primary_key=True)
    disciplinasoriginais = models.ForeignKey(Disciplina, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'disciplinas_originais'
        unique_together = (('bloco', 'disciplinasoriginais'),)


class Historicoescolar(models.Model):
    id = models.BigAutoField(primary_key=True)
    versaocurso = models.ForeignKey('Versaocurso', models.DO_NOTHING, db_column='versaoCurso_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'historicoescolar'


class Itemhistoricoescolar(models.Model):
    id = models.BigAutoField(primary_key=True)
    ano = models.IntegerField(blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)
    situacao = models.IntegerField(blank=True, null=True)
    disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, blank=True, null=True)
    historico_escolar = models.ForeignKey(Historicoescolar, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemhistoricoescolar'


class Professor(models.Model):
    id = models.BigAutoField(primary_key=True)
    matricula = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=255, blank=True, null=True)
    datanascimento = models.DateTimeField(db_column='dataNascimento', blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(max_length=255, blank=True, null=True)
    uf = models.CharField(db_column='UF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=255, blank=True, null=True)
    rua = models.CharField(max_length=255, blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professor'


class ProfessorDisciplina(models.Model):
    professor = models.ForeignKey(Professor, models.DO_NOTHING, primary_key=True)
    disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'professor_disciplina'
        unique_together = (('professor', 'disciplina'),)


class Tabelaequivalencias(models.Model):
    id = models.BigAutoField(primary_key=True)
    versaocursocorrespondente = models.ForeignKey('Versaocurso', models.DO_NOTHING, db_column='versaoCursoCorrespondente_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabelaequivalencias'


class TabelaequivalenciasBlocoequivalencia(models.Model):
    tabelaequivalencias = models.ForeignKey(Tabelaequivalencias, models.DO_NOTHING, primary_key=True)
    blocosequivalencia = models.ForeignKey(Blocoequivalencia, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'tabelaequivalencias_blocoequivalencia'
        unique_together = (('tabelaequivalencias', 'blocosequivalencia'),)


class Turma(models.Model):
    id = models.BigAutoField(primary_key=True)
    capacidademaxima = models.IntegerField(db_column='capacidadeMaxima')  # Field name made lowercase.
    codigo = models.CharField(max_length=255, blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)
    disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, blank=True, null=True)
    professor = models.ForeignKey(Professor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turma'


class Versaocurso(models.Model):
    id = models.BigAutoField(primary_key=True)
    cargahorariaminaitvcomp = models.TextField(db_column='cargaHorariaMinAitvComp', blank=True, null=True)  # Field name made lowercase.
    cargahorariaminoptativas = models.TextField(db_column='cargaHorariaMinOptativas', blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(max_length=255, blank=True, null=True)
    qtdperiodominimo = models.IntegerField(db_column='qtdPeriodoMinimo', blank=True, null=True)  # Field name made lowercase.
    situacao = models.IntegerField(blank=True, null=True)
    atividades = models.ForeignKey(Atividadecomplementar, models.DO_NOTHING, blank=True, null=True)
    curso = models.ForeignKey(Curso, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'versaocurso'


class VersaocursoTabelaequivalencias(models.Model):
    versaocurso = models.ForeignKey(Versaocurso, models.DO_NOTHING, primary_key=True)
    tabelasequivalencias = models.ForeignKey(Tabelaequivalencias, models.DO_NOTHING, db_column='tabelasEquivalencias_id', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'versaocurso_tabelaequivalencias'
        unique_together = (('versaocurso', 'tabelasequivalencias'),)
