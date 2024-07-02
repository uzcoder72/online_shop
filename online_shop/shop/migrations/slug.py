# custom_migration.py
from django.db import migrations
from django.template.defaultfilters import slugify
import itertools

def generate_unique_slug(instance, new_slug=None):
    slug = new_slug or slugify(instance.name)
    Product = instance.__class__
    max_length = instance._meta.get_field('slug').max_length
    slug = slug[:max_length]
    for i in itertools.count(1):
        if not Product.objects.filter(slug=slug).exists():
            break
        slug = '{}-{}'.format(slugify(instance.name)[:max_length - len(str(i)) - 1], i)
    return slug

def update_slugs(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    for product in Product.objects.all():
        product.slug = generate_unique_slug(product)
        product.save()

class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0002_alter_category_options_rename_body_comment_message_and_more'), # replace with your actual migration dependencies
    ]

    operations = [
        migrations.RunPython(update_slugs),
    ]
