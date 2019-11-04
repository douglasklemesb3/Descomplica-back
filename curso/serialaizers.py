from rest_framework import serializers

from curso.models import Curso


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome', 'idade', 'rg', 'cpf',
                  'dataNascimento', 'sexo', 'email', 'telefone', 'bairro', 'endereco', 'numero_de_recidencia',
                  'periodo']
