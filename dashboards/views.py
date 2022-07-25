from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from participants.models import Participant
from penyisihans.models import JawabanPenyisihanSD, JawabanPenyisihanSMP, JawabanPenyisihanSMA
from semifinals.models import JawabanSemifinalSD, JawabanSemifinalSMP, JawabanSemifinalSMA
from balloons.models import BalloonSoalModel
from fasts.models import JawabanFastModel


class DataView(TemplateView):
    template_name = "dashboards/data.html"

    def get(self, request, *args, **kwargs):
        peserta_sd = Participant.objects.filter(tingkat="SD")
        peserta_smp = Participant.objects.filter(tingkat="SMP")
        peserta_sma = Participant.objects.filter(tingkat="SMA")

        penyisihan_sd = JawabanPenyisihanSD.objects.order_by("-result_peserta")[:5]
        penyisihan_smp = JawabanPenyisihanSMP.objects.order_by("-result_peserta")[:5]
        penyisihan_sma = JawabanPenyisihanSMA.objects.order_by("-result_peserta")[:5]

        semifinal_sd = JawabanSemifinalSD.objects.order_by("-result_peserta")[:5]
        semifinal_smp = JawabanSemifinalSMP.objects.order_by("-result_peserta")[:5]
        semifinal_sma = JawabanSemifinalSMA.objects.order_by("-result_peserta")[:5]



        # baloon
        peserta_sd_baloon = Participant.objects.filter(tingkat="SD", balloongame=True)

        nama_peserta_sd_baloon = []
        for q in peserta_sd_baloon:
            nama_peserta_sd_baloon.append(q)

        list_jawaban_balloon = []
        for p in peserta_sd_baloon:
            jawaban = BalloonSoalModel.objects.filter(exam_code=p.exam_code)
            list_jawaban_balloon.append(jawaban)

        dict_jawaban = {}
        for o in range(len(nama_peserta_sd_baloon)):
            dict_jawaban[nama_peserta_sd_baloon[o].first_name] = list_jawaban_balloon[o]

        #fast
        peserta_smp_fast = Participant.objects.filter(tingkat="SMP", fastgame=True)

        # print(peserta_smp_fast)
        nama_peserta_smp_fast = []
        for i in peserta_smp_fast:
            nama_peserta_smp_fast.append(i)
        # print("cek",nama_peserta_smp_fast)
        list_jawaban_fast_smp = []
        for j in peserta_smp_fast:
            jawaban = JawabanFastModel.objects.filter(exam_code=j.exam_code)
            list_jawaban_fast_smp.append(jawaban)
        # print("cek",list_jawaban_fast_smp)
        dict_fast_smp = {}
        for k in range(len(nama_peserta_smp_fast)):
            dict_fast_smp[nama_peserta_smp_fast[k].first_name] = list_jawaban_fast_smp[k]
        print("cek",dict_fast_smp)

        self.extra_context = {
            "peserta_sd": peserta_sd,
            "peserta_smp": peserta_smp,
            "peserta_sma": peserta_sma,
            "penyisihan_sd": penyisihan_sd,
            "penyisihan_smp": penyisihan_smp,
            "penyisihan_sma": penyisihan_sma,
            "semifinal_sd": semifinal_sd,
            "semifinal_smp": semifinal_smp,
            "semifinal_sma": semifinal_sma,
            "dict_jawaban": dict_jawaban,
            "dict_fast_smp": dict_fast_smp,
        }
        return self.render_to_response(self.get_context_data())


class AboutView(TemplateView):
    template_name = "dashboards/about.html"


class DocumentView(TemplateView):
    template_name = "dashboards/document.html"


class TutorialRegistrasiView(TemplateView):
    template_name = "dashboards/tutorial_registrasi.html"


class IndexView(TemplateView):
    template_name = "dashboards/index.html"

    def get(self, request, *args, **kwargs):
        peserta = Participant.objects.get(id=kwargs["user_id"])
        jawaban_penyisihan_sd = None

        jawaban_semifinal_sd = None
        try:
            jawaban_penyisihan_sd = JawabanPenyisihanSD.objects.get(
                exam_code=peserta.exam_code
            )
            jawaban_semifinal_sd = JawabanSemifinalSD.objects.get(
                exam_code=peserta.exam_code
            )
        except JawabanPenyisihanSD.DoesNotExist:
            print("Jawaban Penyisihan Not Found")
        except JawabanSemifinalSD.DoesNotExist:
            print("Jawaban Semifinal Not Found")
        self.extra_context = {
            "peserta": peserta,
            "jawaban_penyisihan_sd": jawaban_penyisihan_sd,
            "jawaban_semifinal_sd": jawaban_semifinal_sd,
        }
        return self.render_to_response(self.get_context_data())


class Home(TemplateView):
    template_name = "dashboards/home.html"
