from django.db import models
from django.core.exceptions import ValidationError


#File size validation check

# def validate_image(image):
#     file_size = image.file.size
#     limit_kb = 20
#     if file_size > limit_kb * 1024:
#         raise ValidationError("Max size of file is %s KB" %limit_kb)
    # limit_mb = 20
    # if file_size > limit_mb * 1024 * 1024:
    #    raise ValidationError("Max size of file is %s MB" % limit_mb)

class Image(models.Model):
    image = models.ImageField(upload_to="./uploads/")
    # image = models.ImageField(upload_to="uploads/", validators=[validate_image])
