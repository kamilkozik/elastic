# -*- coding: utf-8 -*-
from elasticsearch_dsl import DocType, String, Integer

from .client import client


class MovieType(DocType):
    director = String()
    title = String()
    year = Integer()
    genres = String()

    class Meta:
        index = 'movies'

    def save(self, using=client, index=None, validate=True, **kwargs):
        return super(MovieType, self).save(using=client)
