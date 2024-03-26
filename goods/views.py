from django.shortcuts import render


def catalog(request):
    context = {
        "title": "КЗВС Каталог",
        "goods": [
            {
                "image": "deps/images/goods/zoocharm-for-yung-cats.jpg",
                "name": "ZOOCHARM Для котят",
                "description": "1.5 кг, Индейка, рис.",
                "price": 450,
            },
            {
                "image": "deps/images/goods/zoocharm-for-old-cats.jpg",
                "name": "ZOOCHARM Корм для взрослых кошек",
                "description": "1.5 кг, свинина, лосось, рис",
                "price": 450,
            },
            {
                "image": "deps/images/goods/zoocharm-milky-way-grill.jpg",
                "name": "ZOOCHARM Влажный корм",
                "description": "Молочный ломтик вяленый",
                "price": 40,
            },
            {
                "image": "deps/images/goods/VG-osheinik-tigr-biruze-for-dog.jpg",
                "name": "Ошейник VG для собак",
                "description": "Кожаный с тигром бирюзовый и черными изогнутыми шипами.",
                "price": 1245,
            },
            {
                "image": "deps/images/goods/VG-toy-for-dog-guantel.jpg",
                "name": "Игрушка VG для собак",
                "description": "Древ.основе с отвер. для корма Гантеля с аром. курицы",
                "price": 299,
            },
            {
                "image": "deps/images/goods/silitter-napolnitel-siligel-aloe-vera.jpg",
                "name": "Silica Light Наполнитель силикагелевый",
                "description": "Объем 5л, ALOE VERA",
                "price": 399,
            },
            {
                "image": "deps/images/goods/silitter-napolnitel-bentonil-lavanda.jpg",
                "name": "Silitter Наполнитель бентонитовый",
                "description": "Объем 5л, ЛАВАНДА",
                "price": 499,
            },
            {
                "image": "deps/images/goods/yugi-lezhanka-for-dogs-blue.jpg",
                "name": "YUGI Лежанка комбинированная",
                "description": "Серо-синяя 68*59*25см",
                "price": 1499,
            },
            {
                "image": "deps/images/goods/yugi-kletka-dlya-ptic-39.jpg",
                "name": "YUGI Клетка  для птиц",
                "description": "Красное дно 39,5*29,5*45,5см",
                "price": 899,
            },
            {
                "image": "deps/images/goods/bestdinner-sterlised-adult-hypoallergenic.jpg",
                "name": "Best Dinner Целостный гиппоалергенный",
                "description": "3 кг. Для взрослых стерилизованных кошек. Ягненок И Базилик",
                "price": 799,
            },
            {
                "image": "deps/images/goods/bestdinner-exclusive-vet-Profi-Renal.jpg",
                "name": "Best Dinner Exclusive Vet Profi Renal",
                "description": "Кусочки в соусе, Говядина",
                "price": 945,
            },
            {
                "image": "deps/images/goods/alphapet-white-fish-for-old-dog-min-porod.jpg",
                "name": "Alpha Pet Белая рыба",
                "description": "2 кг. Для взрослых собак мелких пород.",
                "price": 645,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
