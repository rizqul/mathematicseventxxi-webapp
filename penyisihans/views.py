from datetime import datetime
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

# Create your views here.

from participants.models import Participant
from .models import (
    Event, JawabanPenyisihanSMA, JawabanPenyisihanSMP,
    SoalPenyisihanSD,
    SoalPenyisihanSMP,
    SoalPenyisihanSMA,
    JawabanPenyisihanSD,
)


class PenyisihanResultView(TemplateView):
    template_name = "penyisihans/result.html"

    def result(self, jawaban):
        kunciA = [
            "1A",
            "2A",
            "3A",
            "4A",
            "5A",
            "6A",
            "7A",
            "8A",
            "9A",
            "10A",
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
        benar, salah, kosong = 0, 0, 0
        paket_soal = jawaban.paket_soal
        jawaban = jawaban.jawaban_peserta.split()
        if paket_soal == "A":
            for i in range(len(jawaban)):
                if kunciA[i] == "":
                    print("kosong")
                    kosong += 1
                elif kunciA[i] == jawaban[i]:
                    print("sama")
                    benar += 1
                else:
                    print("beda")
                    salah += 1

        data = [benar, salah, kosong]

        return data

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        peserta = Participant.objects.get(exam_code=kwargs['exam_code'])

        jawaban = None
        if peserta.tingkat == 'SD':
            jawaban = JawabanPenyisihanSD.objects.get(
                exam_code=kwargs["exam_code"])
        if peserta.tingkat == 'SMP':
            jawaban = JawabanPenyisihanSMP.objects.get(
                exam_code=kwargs["exam_code"])
        if peserta.tingkat == 'SMA':
            jawaban = JawabanPenyisihanSMA.objects.get(
                exam_code=kwargs["exam_code"])

        data = self.result(jawaban)
        print(data)
        jawaban.result_peserta = 0
        jawaban.jawaban_benar = data[0]
        jawaban.jawaban_salah = data[1]
        jawaban.jawaban_kosong = data[2]
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


# belum selesai untuk smp dan sma(soal dan jawaban)


def UjianPenyisihanView(request, *args, **kwargs):
    peserta = Participant.objects.get(exam_code=kwargs["exam_code"])
    context = {}

    if request.method == "GET":
        # mengambil soal
        soal = None
        event = None
        if peserta.tingkat == "SD":
            soal = SoalPenyisihanSD.objects.filter(
                paket_soal=peserta.paket_soal)
            event = Event.objects.get(nama_event="Penyisihan SD")

        if peserta.tingkat == "SMP":
            soal = SoalPenyisihanSMP.objects.filter(
                paket_soal=peserta.paket_soal)
            event = Event.objects.get(nama_event="Penyisihan SD")

        if peserta.tingkat == "SMA":
            soal = SoalPenyisihanSMA.objects.filter(
                paket_soal=peserta.paket_soal)
            event = Event.objects.get(nama_event="Penyisihan SD")

        # data
        context = {
            "peserta": peserta,
            "soal": soal,
            "end_time": datetime(2021, 1, 21, 15, 45, 0, 0),
            "event": event,
        }

        from django.core.serializers import serialize

        data = serialize("json", soal)
        context["data"] = data

    if request.method == "POST":
        data = request.POST
        jawaban = generate_jawaban(data)
        if peserta.tingkat == "SD":
            jawaban_peserta = JawabanPenyisihanSD(
                id_peserta=peserta.no_id,
                nama_peserta=peserta.first_name,
                exam_code=peserta.exam_code,
                paket_soal=peserta.paket_soal,
                jawaban_peserta=jawaban,
            )
            jawaban_peserta.save()
        if peserta.tingkat == "SMP":
            jawaban_peserta = JawabanPenyisihanSMP(
                id_peserta=peserta.no_id,
                nama_peserta=peserta.first_name,
                exam_code=peserta.exam_code,
                paket_soal=peserta.paket_soal,
                jawaban_peserta=jawaban,
            )
            jawaban_peserta.save()
        if peserta.tingkat == "SMA":
            jawaban_peserta = JawabanPenyisihanSMA(
                id_peserta=peserta.no_id,
                nama_peserta=peserta.first_name,
                exam_code=peserta.exam_code,
                paket_soal=peserta.paket_soal,
                jawaban_peserta=jawaban,
            )
            jawaban_peserta.save()

        success_url = reverse_lazy(
            "penyisihans:result", kwargs={"exam_code": peserta.exam_code}
        )
        return HttpResponseRedirect(success_url)

    return render(request, "penyisihans/ujian.html", context)


class StartPenyisihanView(TemplateView):
    template_name = "penyisihans/start.html"
    model = Participant

    def cek_paket(self, peserta):
        peserta = peserta
        if peserta.paket_soal == "":
            import random

            paket = "ABCDE"
            peserta.paket_soal = random.choice(paket)
            peserta.save()
            print("peserta paket", peserta.paket_soal)

    def get(self, request, *args, **kwargs):
        peserta = self.model.objects.get(exam_code=kwargs["exam_code"])
        event = None

        if peserta.tingkat == "SD":
            event = Event.objects.get(nama_event="Penyisihan SD")
        if peserta.tingkat == "SMP":
            event = Event.objects.get(nama_event="Penyisihan SMP")
        if peserta.tingkat == "SMA":
            event = Event.objects.get(nama_event="Penyisihan SMA")

        context = self.get_context_data(**kwargs)
        context["peserta"] = peserta
        context["event"] = event
        self.cek_paket(peserta)
        return self.render_to_response(context)
