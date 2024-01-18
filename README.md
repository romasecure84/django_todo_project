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
