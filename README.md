## Django ORM Query:
'''shell
python manage.py shell
'''
'''python
# Todo modelini import etmek:
from todo.models import Todo

# Butun objektler:
Todo.objects.all()

# Butun objektleri say:
Todo.objects.all().count()

# Yeni Todo yaratmaq:
Todo.objects.create(title="Shel uzerinden yeni yaradilan Todo", is_active=True)

# is_active olanlari goster:
Todo.objects.filter(is_active=True)

# is_active olanlarin sayi:
Todo.objects.filter(is_active=True).count()
'''
# Update etmek komandasi:
Todo.objects.filter(is_active=False).update(is_acive=True)

# Title icerisinde Django olmayanlari tapmaq ve Django elave etmek:
todos = Todo.objects.exclude(title__icontains='Django')
for item in todos:
    item.title = f"{item.title} - Django"
     item.save()