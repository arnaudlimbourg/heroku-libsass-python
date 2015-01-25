from __future__ import absolute_import

from django.contrib.staticfiles.storage import ManifestStaticFilesStorage

from whitenoise.django import GzipStaticFilesMixin

from pipeline.storage import PipelineMixin


class WhiteNoisePipeline(GzipStaticFilesMixin, PipelineMixin, ManifestStaticFilesStorage):
    pass
