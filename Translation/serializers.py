from django.urls import reverse
from rest_framework import serializers

from .models import Translation


class TranslationSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='translation-detail', lookup_field='id')
    translation = serializers.SerializerMethodField('get_translation')
    verse = serializers.SerializerMethodField('get_verse')

    def get_verse(self, translation):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('verse-detail', kwargs={'verse_number': translation.verse.verse_number}))

    def get_translation(self, translation):
        f = translation.translation.open()
        trans_text = f.read()
        f.close()
        return trans_text

    class Meta:
        model = Translation
        fields = ['detail', 'id', 'translation', 'verse']
