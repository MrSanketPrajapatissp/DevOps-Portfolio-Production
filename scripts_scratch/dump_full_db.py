import os
import sys
import django
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.apps import apps
from django.db.models import Model
from django.forms.models import model_to_dict

def get_field_val(obj, k):
    val = getattr(obj, k)
    if not val:
        return None
    # Check if file field
    if hasattr(val, 'url'):
        try:
            return val.url
        except ValueError:
            return None
    if hasattr(val, 'isoformat'):
        return val.isoformat()
    return val

def dump_model(model):
    print(f"\n=================== MODEL: {model.__name__} ===================")
    for obj in model.objects.all():
        try:
            data = {}
            for field in obj._meta.fields:
                data[field.name] = get_field_val(obj, field.name)
            print(json.dumps(data, indent=2))
        except Exception as e:
            print(f"Error dumping record {obj}: {e}")

def main():
    models_to_dump = [
        ('core', 'HeroIdentity'),
        ('core', 'ProfessionalSummary'),
        ('core', 'SocialLink'),
        ('core', 'Resume'),
        ('skills', 'SkillCategory'),
        ('skills', 'Skill'),
        ('projects', 'Project'),
        ('certifications', 'Certification'),
        ('experience', 'Experience'),
        ('showcases', 'Showcase')
    ]
    for app_label, model_name in models_to_dump:
        try:
            model = apps.get_model(app_label, model_name)
            dump_model(model)
        except Exception as e:
            print(f"Error dumping {app_label}.{model_name}: {e}")

if __name__ == '__main__':
    main()
