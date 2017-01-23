# -*- coding: utf-8 -*-
from elasticsearch_dsl import Search

from .client import client


def compose_query():
    return Search(using=client, index="movies").query("query_string", query="drama")


def get_response():
    return compose_query().execute()


def get_results():
    for hit in get_response():
        print hit, hit.genres
