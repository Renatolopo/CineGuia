from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify

# Create your models here.
class Filme(models.Model):
    id_filme = models.CharField('nome', max_length=100)
    title = models.CharField('nome', max_length=200, unique=True)
    descricao = models.CharField('nome', max_length=1000)
    img = models.CharField('nome', max_length=100)
    avaliacao = models.CharField('nome', max_length=100) 
    similar_id = models.CharField('nome', max_length=100) 
