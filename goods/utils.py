from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


from goods.models import Products



def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector("name", "description")
    query = SearchQuery("cheese")

    return Products.objects.annotate(rank=SearchRank(vector, query)).order_by("-rank")