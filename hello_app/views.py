from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def print_hello(request):
    movie_data = {
        "movies": [
            {
                "title": "The Godfather",
                "year": 1972,
                "summary": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                "success": False,
            },
            {
                "title": "The Shawshank Redemption",
                "year": 1994,
                "summary": "a guy who escape jail",
                "success": True,
            },
            {
                "title": "Schindler's List",
                "year": 1993,
                "summary": "get to watch he movie wee",
                "success": True,
            },
            {
                "title": "Raging Bull",
                "year": 1980,
                "summary": "a guy who is a boxer",
                "success": False,
            },
            {
                "title": "Casablanca",
                "year": 1942,
                "summary": "a guy who is a boxer",
                "success": True,
            },
            {
                "title": "Citizen Kane",
                "year": 1941,
                "summary": "not sure what this movie is about",
                "success": False,
            },
        ]
    }
    return render(request, "hello.html", movie_data)
