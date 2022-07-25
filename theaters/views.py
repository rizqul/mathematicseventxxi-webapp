from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

# Create your views here.

from participants.models import Participant
from .models import JawabanTheaterModel
from .forms import JawabanTheaterForm


class UjianTheatreView(FormView):
    form_class = JawabanTheaterForm
    template_name = "theaters/ujian.html"

    def get(self, request, *args, **kwargs):
        id = int(kwargs["id"])
        if id > 10:
            success_url = reverse_lazy("dashboards:home")
            return HttpResponseRedirect(success_url)
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, kwargs):
        form = form.cleaned_data
        jawaban = JawabanTheaterModel(
            no_soal=kwargs["id"],
            exam_code=kwargs["exam_code"],
            nama_peserta=Participant.objects.get(
                exam_code=kwargs["exam_code"]
            ).first_name,
            jawaban=form["jawaban"],
        )
        jawaban.save()
        id = int(kwargs["id"]) + 1
        success_url = reverse_lazy(
            "theaters:ujian",
            kwargs={"exam_code": kwargs["exam_code"], "id": id},
        )

        return HttpResponseRedirect(success_url)


# class UjianTheaterView(FormView):
#     form_class = JawabanTheaterForm
#     template_name = 'theaters/ujian.html'

#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form, kwargs)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form, kwargs):
#         form = form.cleaned_data
#         peserta = Participant.objects.get(exam_code=kwargs['exam_code'])

#         print(form['jawaban0'])
#         jawaban = JawabanTheaterModel(
#             exam_code=kwargs['exam_code'],
#             nama_peserta=peserta.first_name,
#             jawaban0=form['jawaban0'],
#             jawaban1=form['jawaban1'],
#             jawaban2=form['jawaban2'],
#             jawaban3=form['jawaban3'],
#             jawaban4=form['jawaban4'],
#             jawaban5=form['jawaban5'],
#             jawaban6=form['jawaban6'],
#             jawaban7=form['jawaban7'],
#             jawaban8=form['jawaban8'],
#             jawaban9=form['jawaban9'],
#         )
#         jawaban.save()

#         success_url = reverse_lazy('dashboards:index', kwargs={
#                                    'user_id': peserta.id})
#         return HttpResponseRedirect(success_url)


class StartTheaterView(TemplateView):
    template_name = "theaters/start.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        peserta = Participant.objects.get(exam_code=kwargs["exam_code"])
        context["peserta"] = peserta
        return self.render_to_response(context)
