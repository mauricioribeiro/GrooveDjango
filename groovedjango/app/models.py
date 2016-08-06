from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

# estas funcoes sao usadas nos args "upload_to" para fazer migrations, uma vez que o Django nao faz migrations com funcoes anonimas (lambdas)
def get_artista_path(instance, filename): return 'artistas/{0}_{1}'.format(instance.nome, filename)
def get_album_path(instance, filename): return 'albuns/{0}_{1}'.format(instance.nome, filename)

class Categoria(models.Model):
	nome = models.CharField(max_length = 100)

	def __str__(self):
		return self.nome

class Artista(models.Model):
	nome = models.CharField(max_length = 100)
	foto = models.ImageField(upload_to = get_artista_path, max_length = 100)

	def __str__(self):
		return self.nome

	def get_foto_url(self):
		return '{0}/{1}'.format(settings.MEDIA_URL, self.foto) if self.foto else False

class Album(models.Model):
	nome = models.CharField(max_length = 100)
	foto = models.ImageField(upload_to = get_album_path, max_length = 100)
	ano = models.IntegerField(validators = [MinValueValidator(1899), MaxValueValidator(2999)])
	categoria = models.ManyToManyField(Categoria)
	artista = models.ForeignKey(Artista, on_delete=models.PROTECT)

	def __str__(self):
		return '{0} ({1})'.format(self.nome, self.ano)

	def get_foto_url(self):
		return '{0}/{1}'.format(settings.MEDIA_URL, self.foto) if self.foto else False

class Musica(models.Model):
	nome = models.CharField(max_length = 100)
	duracao = models.DurationField()
	album = models.ForeignKey(Album, on_delete=models.CASCADE)

	def __str__(self):
		return '{0} - {1}'.format(self.nome, self.duracao)

	def get_duracao(self):
		return '{0}:{1}'.format((self.duracao.seconds//60)%60, '%02d' %(self.duracao.seconds%60))