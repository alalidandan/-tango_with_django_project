import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
django.setup()

from rango.models import Category, Page

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_category(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

def populate():
    python_cat = add_category('Python', likes=64)
    django_cat = add_category('Django', likes=32)
    other_cat = add_category('Other Frameworks', likes=16)

    add_page(python_cat, title="Official Python Tutorial", url="http://docs.python.org/3/tutorial/", views=100)
    add_page(python_cat,title="How to Think like a Computer Scientist",url="http://www.greenteapress.com/thinkpython/",views=75)
    add_page(python_cat, title="Learn Python in 10 Minutes", url="http://www.korokithakis.net/tutorials/python/", views=50)

    add_page(django_cat, title="Official Django Tutorial", url="https://docs.djangoproject.com/en/2.1/intro/tutorial01/", views=60)
    add_page(django_cat, title="Django Rocks", url="http://www.djangorocks.com/", views=45)
    add_page(django_cat, title="How to Tango with Django", url="http://www.tangowithdjango.com/", views=30)

    add_page(other_cat, title="Bottle", url="http://bottlepy.org/docs/dev/", views=25)
    add_page(other_cat, title="Flask", url="http://flask.pocoo.org", views=20)

    print("Database populated!")

if __name__ == '__main__':
    populate()

