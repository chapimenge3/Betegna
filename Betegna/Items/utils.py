# Python Builtin import
import uuid

def item_directory_path(instance, filename):
    ext = (filename).split(".")[-1]
    filename = str(uuid.uuid1())
    print(instance, instance.pk)
    return f"store/{instance.id}-{filename}.{ext}"