import time

from django.utils.text import slugify


def slugify_instance_title(instance, save=False, new_slug=None):
    """
    Create a slug for a given instance's title and ensure that it is unique.

    Args:
        instance: An instance of a Django model.
        save (bool): If True, save the instance after setting the slug.
        new_slug (str): A new slug to use instead of generating one from the title.

    Returns:
        The instance with the slug set.

    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    instance_class = instance.__class__
    qs = instance_class.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        # auto generate new slug
        slug = f"{slug}-{int(time.time())}"
        return slugify_instance_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance
