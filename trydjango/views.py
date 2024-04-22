"""
To render html pages
"""

import random
from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    name = "Justin"
    number = random.randint(10, 1000000)
    H1_STRING = f"""
    <h1>Hello {name} - {number}</h1>
    """
    P_STRING = f"""
    <p>Hi {name} - {number}</p>
    """

    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)