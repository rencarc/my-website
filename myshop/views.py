from django.shortcuts import render

def home(request):

    products = {
        "round": [
            {"image": "round1.jpg", "name": "Geo Round Jar - Purple", "price": "$3", "id": 1},
            {"image": "round2.jpg", "name": "Geo Round Jar - Black", "price": "$3", "id": 2},
            {"image": "round3.jpg", "name": "Geo Round Jar - White", "price": "$3", "id": 3},
            {"image": "round4.jpg", "name": "Geo Round Jar - Pink", "price": "$3", "id": 4},
            {"image": "round5.jpg", "name": "Geo Round Jar - Cream", "price": "$3", "id": 5},
            {"image": "round6.jpg", "name": "Geo Round Jar - Red", "price": "$3", "id": 6},
            {"image": "round7.jpg", "name": "Geo Round Jar - Gold", "price": "$2.9", "id": 7},
        ],
        "geo": [
            {"image": "geo1.jpg", "name": "Geo Cut Jar - Black", "price": "$4", "id": 8},
            {"image": "geo2.jpg", "name": "Geo Cut Jar - Amber", "price": "$4", "id": 9},
            {"image": "geo3.jpg", "name": "Geo Cut Jar - Purple", "price": "$4", "id": 10},
            {"image": "geo4.jpg", "name": "Geo Cut Jar - Navy", "price": "$4", "id": 11},
        ],
        "other": [
            {"image": "ch1.jpg", "name": "Checkered Jar - Green", "price": "$5", "id": 12},
            {"image": "ch2.jpg", "name": "Checkered Jar - Navy", "price": "$5", "id": 13},
            {"image": "ch3.jpg", "name": "Checkered Jar - Black", "price": "$5", "id": 14},
            {"image": "ch4.jpg", "name": "Checkered Jar - White", "price": "$5", "id": 15},
        ]
    }

    return render(request, 'homepage/index.html', {"products": products})
