from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "control_freaks/index.html"


class InformView(TemplateView):
    template_name = "control_freaks/inform.html"


class InformActionView(TemplateView):
    template_name = "control_freaks/inform_action.html"


class InformFilmView(TemplateView):
    template_name = "control_freaks/inform_film.html"


class InfromFutureView(TemplateView):
    template_name = "control_freaks/inform_future.html"


class InformOpinionView(TemplateView):
    template_name = "control_freaks/inform_opinion.html"


class InformSeriousView(TemplateView):
    template_name = "control_freaks/inform_serious.html"


class ContactView(TemplateView):
    template_name = "control_freaks/contact.html"
