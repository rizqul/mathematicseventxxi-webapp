from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import FormPlayOffPenyisihan, FormPlayOffSemifinal
from participants.models import Participant
from .models import PlayOffPenyisihan, PlayOffSemifinal


class StartPenyisihanPlayoffView(TemplateView):
    template_name = 'playoffs/start_penyisihan.html'


class UjianPenyisihanPlayoffView(FormView):
    form_class = FormPlayOffPenyisihan
    success_url = '/'
    template_name = 'playoffs/ujian_penyisihan.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, kwargs):
        peserta = Participant.objects.get(exam_code=kwargs['exam_code'])
        form = form.cleaned_data
        jawaban = PlayOffPenyisihan(
            id_peserta=peserta.no_id,
            nama_peserrta=peserta.first_name,
            tingkat=peserta.tingkat,
            jawaban=form['jawaban']
        )
        jawaban.save()
        # print("peserta", peserta)
        return HttpResponseRedirect(self.get_success_url())


class StartSemifinalPlayoffView(TemplateView):
    template_name = 'playoffs/start_semifinal.html'


class UjianSemifinalPlayoffView(FormView):
    form_class = FormPlayOffSemifinal
    succes_url = '/'
    template_name = 'playoffs/ujian_semifinal.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, kwargs):
        peserta = Participant.objects.get(exam_code=kwargs['exam_code'])
        form = form.cleaned_data
        jawaban = PlayOffSemifinal(
            id_peserta=peserta.no_id,
            nama_peserta=peserta.first_name,
            tingkat=peserta.tingkat,
            jawaban=form['jawaban']
        )
        jawaban.save()
        # print("peserta", peserta)
        return HttpResponseRedirect(self.get_success_url())
