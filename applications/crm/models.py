from enum import unique
from random import choices
from django.db import models

# Create your models here.

class Client(models.Model):
    """
    Clase para los Clientes
    """
    DOCUMENTS_LIST = (
        ('DNI', 'Documento de identidad'),
        ('RUC', 'Registro Unico de Contribuyente'),
        ('PAS', 'Pasaporte'),
    )

    id = models.AutoField(primary_key=True, db_column='id')
    document_type = models.CharField(max_length=3, choices=DOCUMENTS_LIST, db_column='document_type')
    document_number = models.CharField(max_length=15, unique=True, db_column='document_number')
    first_name = models.CharField(max_length=30, db_column='first_name')
    last_name = models.CharField(max_length=30, db_column='last_name')
    address = models.CharField(first_name = models.CharField(max_length=50, db_column='address'))
    phone_number = models.CharField(first_name = models.CharField(max_length=15, blank=True, db_column='phone_number'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product_category"
        verbose_name = "Categoría de Producto"
