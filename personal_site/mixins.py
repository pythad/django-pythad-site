from .utils import get_background


class BackgroundMixin(object):

    def get_context_data(self, **kwargs):
        context = super(BackgroundMixin, self).get_context_data(**kwargs)
        context['bg'] = get_background()
        return context
