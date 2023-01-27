from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from django.core.validators import RegexValidator
import re
from projects.service import answer


# Create your models here.
def typecard(card_number):
    visa = re.compile('^4[0-9]{12}(?:[0-9]{3})?$')
    mastercard = re.compile('^5[1-5][0-9]{14}$')
    amex = re.compile('^3[47][0-9]{13}$')
    discover = re.compile('^6(?:011|5[0-9]{2})[0-9]{12}$')
    if visa.match(card_number):
        return 'Visa'
    elif mastercard.match(card_number):
        return 'Mastercard'
    elif amex.match(card_number):
        return 'American Express'
    elif discover.match(card_number):
        return 'Discover'
    else:
        return 'Invalid'


class Payment(models.Model):
    print("Payment------>")
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    card_number = models.TextField(
        validators=[MinLengthValidator(16), RegexValidator(regex='^(?:[0-9]{4}[ ]?){3}[0-9]{4}$')])
    card_cvv = models.TextField(validators=[MinLengthValidator(3)])
    total_value = models.FloatField(validators=[MinValueValidator(1000.0)])
    extra_description = models.TextField(blank=True)
    commission_value = models.FloatField(default=0.0)
    card_type = models.TextField(blank=True)
    response_Payu = models.TextField(null=True)

    def save(self, *args, **kwargs):  # pasa un numero variable de argumentos a una function
        print('save----------->')
        self.response_Payu = answer()
        self.commission_value = (self.total_value * 0.03) + (self.total_value * 0.015) + (
                (self.total_value * 0.03
                 ) * 0.19)
        self.card_number_temporal = '*' * (len(self.card_number) - 4) + self.card_number[-4:]
        self.card_type = typecard(self.card_number)
        self.card_number = self.card_number_temporal
        super().save(*args, **kwargs)

        # En este caso, se está utilizando super() para acceder al método save() de la clase padre, y se están pasando los argumentos *args y **kwargs para asegurar que cualquier argumento adicional que se pase al método save() cuando se llame desde una instancia de la clase TuModelo se pase a la llamada al método save() de la clase padre.
# La llamada al método save() de la clase padre es importante ya que este método se encarga de guardar los datos en la base de datos y si no se llama, los datos no se guardarán.
# super().save(*args, **kwargs) se encarga de guardar los cambios realizados en la instancia de TuModelo en la base de datos.
