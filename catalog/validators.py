from rest_framework.exceptions import ValidationError


def validator(file):
    max_size = 100
    if file.size > max_size * 1024:
        return ValidationError(f"image size cannot be more than {max_size}KB")
