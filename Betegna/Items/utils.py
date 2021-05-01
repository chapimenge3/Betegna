# Python Builtin import
import uuid
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

def item_directory_path(instance, filename):
    ext = (filename).split(".")[-1]
    filename = str(uuid.uuid1())
    print(instance, instance.pk)
    return f"store/{instance.id}-{filename}.{ext}"


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening
