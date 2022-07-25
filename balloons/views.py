from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, FormView

# Create your views here.
from .models import BalloonSoalModel
from participants.models import Participant

from .forms import JawabanBalloonForm


class BalloonJawabView(FormView):
    form_class = JawabanBalloonForm
    template_name = "balloons/show_soal.html"

    def get(self, request, *args, **kwargs):
        soal = BalloonSoalModel.objects.get(id=kwargs["pk"])
        self.extra_context = {
            "soal": soal,
        }
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, kwargs):
        form = form.cleaned_data

        soal = BalloonSoalModel.objects.get(id=kwargs["pk"])
        soal.jawaban = form["jawaban"]
        soal.save()

        success_url = reverse_lazy(
            "balloons:show", kwargs={"exam_code": kwargs["exam_code"]}
        )
        return HttpResponseRedirect(success_url)


class BalloonSoalDetailView(DetailView):
    model = BalloonSoalModel
    template_name = "balloons/show_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        peserta = Participant.objects.get(exam_code=kwargs["exam_code"])

        # set soal pengalih sudah diambil
        soal = self.object
        soal.is_taken = True
        soal.save()

        # set soal asli examcode dan nama
        soal_asli = BalloonSoalModel.objects.get(id=soal.soal_acak)
        if soal_asli.exam_code:
            succes_url = reverse_lazy(
                "balloons:show", kwargs={"exam_code": kwargs["exam_code"]}
            )
            return HttpResponseRedirect(succes_url)
        else:
            soal_asli.exam_code = kwargs["exam_code"]
            soal_asli.nama_peserta = peserta.first_name
            soal_asli.save()

        context = self.get_context_data(object=self.object)
        context["peserta"] = peserta
        context["exam_code"] = kwargs["exam_code"]
        context["soal_asli"] = soal_asli
        print("peserta", peserta.exam_code)
        print("soal", soal.exam_code)
        print("Soal Aslis", soal_asli.exam_code)
        return self.render_to_response(context)


class BalloonSoalView(TemplateView):
    model = BalloonSoalModel
    template_name = "balloons/show_balloon.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        jawaban = self.model.objects.filter(exam_code=kwargs["exam_code"])
        soal = self.model.objects.all()

        context["soal"] = soal
        context["exam_code"] = kwargs["exam_code"]
        context["jawaban"] = jawaban
        return self.render_to_response(context)
