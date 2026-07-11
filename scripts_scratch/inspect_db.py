import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.apps import apps

def main():
    print("Listing all models and their counts:")
    for model in apps.get_models():
        try:
            count = model.objects.count()
            print(f"- {model.__name__} (app: {model._meta.app_label}): {count} records")
            # If records exist, print them
            if count > 0:
                for obj in model.objects.all()[:3]:
                    print(f"  - [{obj.pk}] {str(obj)[:100]}")
        except Exception as e:
            print(f"- Error reading {model.__name__}: {e}")

if __name__ == '__main__':
    main()
