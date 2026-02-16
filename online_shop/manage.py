#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
        
        # Patch for Python 3.14 compatibility (Django 5.0.x issue)
        try:
            import django.template.context

            def fixed_base_context_copy(self):
                # Using object.__new__ to create a new instance without calling __init__
                duplicate = object.__new__(self.__class__)
                # Copy all attributes (shallow copy default behavior)
                duplicate.__dict__ = self.__dict__.copy()
                # Specific behavior from original method: shallow copy dicts list
                duplicate.dicts = self.dicts[:]
                return duplicate

            django.template.context.BaseContext.__copy__ = fixed_base_context_copy
        except Exception as e:
            print(f"Warning: Failed to apply Python 3.14 patch: {e}")

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
