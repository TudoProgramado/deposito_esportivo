from django.db import models


class Produto(models.Model):
    # 1, 2, 3, 4, 5, 6, 10000
    id_produto = models.AutoField(primary_key=True)
    # CharField = texto / Ex: bola de basquete
    nome = models.CharField(max_length=25)
    # Bola de basquete da nike/adidas infantil
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
