from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import TemplateView

# Create your views here.
from participants.models import Participant
from .models import (
    Event,
    SoalSemifinalSD,
    SoalSemifinalSMP,
    SoalSemifinalSMA,
    JawabanSemifinalSD,
    JawabanSemifinalSMP,
    JawabanSemifinalSMA,
)


class SemifinalResultView(TemplateView):
    template_name = "penyisihans/result.html"

    def result(self, jawaban):
        kunciA = [
            "1A",
            "2B",
            "3C",
            "4D",
            "5E",
            "6A",
            "7B",
            "8C",
            "9D",
            "10E",
            "11A",
            "12A",
            "13A",
            "14A",
            "15A",
        ]
        kunciB = [
            "1B",
            "2B",
            "3B",
            "4B",
            "5B",
            "6B",
            "7B",
            "8B",
            "9B",
            "10B",
            "11B",
            "12B",
            "13B",
            "14B",
            "15B",
        ]
        kunciC = [
            "1C",
            "2C",
            "3C",
            "4C",
            "5C",
            "6C",
            "7C",
            "8C",
            "9C",
            "10C",
            "11C",
            "12C",
            "13C",
            "14C",
            "15C",
        ]
        kunciD = [
            "1D",
            "2D",
            "3D",
            "4D",
            "5D",
            "6D",
            "7D",
            "8D",
            "9D",
            "10D",
            "11D",
            "12D",
            "13D",
            "14D",
            "15D",
        ]
        kunciE = [
            "1E",
            "2E",
            "3E",
            "4E",
            "5E",
            "6E",
            "7E",
            "8E",
            "9E",
            "10E",
            "11E",
            "12E",
            "13E",
            "14E",
            "15E",
        ]
        benar = 0
        paket_soal = jawaban.paket_soal
        jawaban = jawaban.jawaban_peserta.split()
        if paket_soal == "A":
            for i in range(len(jawaban)):
                if kunciA[i] == jawaban[i]:
                    benar += 1

        return benar

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        jawaban = JawabanSemifinalSD.objects.get(exam_code=kwargs["exam_code"])
        result = self.result(jawaban)
        jawaban.result_peserta = result
        jawaban.save()

        context["jawaban"] = jawaban
        return self.render_to_response(context)


# bukan view
# method untuk mengisi field jawaban peserta


def generate_jawaban(data):
    jawaban = ""
    for d in data:
        if d != "csrfmiddlewaretoken":
            jawaban += d + data[d] + " "

    return jawaban


def UjianSemifinalView(request, *args, **kwargs):
    peserta = Participant.objects.get(exam_code=kwargs["exam_code"])
    context = {}

    if request.method == "GET":
        # mengambil soal
        soal = None
        event = None
        if peserta.tingkat == "SD":
            soal = SoalSemifinalSD.objects.filter(paket_soal=peserta.paket_soal)
            event = Event.objects.get(nama_event="Semifinal SD")

        if peserta.tingkat == "SMP":
            soal = SoalSemifinalSMP.objects.filter(paket_soal=peserta.paket_soal)

        if peserta.tingkat == "SMA":
            soal = SoalSemifinalSMA.objects.filter(paket_soal=peserta.paket_soal)

        # elif peserta.tingkat == 'SMP':
        #     soal = SoalPenyisihanSMP.objects.filter(
        #         paket_soal=peserta.paket_soal)

        # data
        context = {
            "peserta": peserta,
            "soal": soal,
            "end_time": datetime(2021, 2, 3, 15, 45, 0, 0),
            "event": event,
        }

        print(event)

        from django.core.serializers import serialize

        data = serialize("json", soal)
        context["data"] = data

    if request.method == "POST":
        data = request.POST
        jawaban = generate_jawaban(data)
        if peserta.tingkat == "SD":
            jawaban_peserta = JawabanSemifinalSD(
                id_peserta=peserta.no_id,
                nama_peserta=peserta.first_name,
                exam_code=peserta.exam_code,
                paket_soal=peserta.paket_soal,
                jawaban_peserta=jawaban,
            )
            jawaban_peserta.save()

        success_url = reverse_lazy(
            "semifinals:result", kwargs={"exam_code": peserta.exam_code}
        )
        return HttpResponseRedirect(success_url)

    return render(request, "semifinals/ujian.html", context)


class StartSemiFinalsView(TemplateView):
    model = Participant
    template_name = "semifinals/start.html"

    def get(self, request, *args, **kwargs):
        peserta = self.model.objects.get(exam_code=kwargs["exam_code"])
        peserta.paket_soal = "A"
        peserta.save()
        event = None

        if peserta.tingkat == "SD":
            event = Event.objects.get(nama_event="Semifinal SD")

        context = self.get_context_data(**kwargs)
        context["peserta"] = peserta
        context["event"] = event
        return self.render_to_response(context)
