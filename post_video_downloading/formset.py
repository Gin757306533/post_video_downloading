# -*- encoding: utf-8 -*-
from django.forms import modelformset_factory, BaseModelFormSet

from post_video_downloading.models import Image


class BaseMultiImageFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Image.objects.none()

MultiImageForm = modelformset_factory(Image, fields=('file',), formset=BaseMultiImageFormSet)