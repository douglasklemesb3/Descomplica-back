from rest_framework import serializers

from entretenimentos.models import Entretenimento


class EntretenimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entretenimento
        fields = ['id', 'nome', 'idade', 'rg', 'cpf',
                'sexo', 'email', 'telefone', 'endereco','periodo']
