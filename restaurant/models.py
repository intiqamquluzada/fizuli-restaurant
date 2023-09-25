from django.db import models
from ckeditor.fields import RichTextField
from services.mixin import DateMixin, SlugMixin
from services.generator import Generator
from services.uploader import Uploader


class AboutModel(DateMixin, SlugMixin):
    head = models.CharField(max_length=255, verbose_name="Haqqımızda başlıq hissəsi")
    description = RichTextField(verbose_name="Açıqlama")
    years_of_experience = models.CharField(max_length=255, verbose_name="Təcrübə")
    count_of_workers = models.CharField(max_length=255, verbose_name="İşçilərin sayı")
    img_1 = models.ImageField(upload_to=Uploader.upload_photo_for_about, verbose_name="Sol üst şəkil", help_text="298x298")
    img_2 = models.ImageField(upload_to=Uploader.upload_photo_for_about, verbose_name="Sağ üst şəkil", help_text="224x224")
    img_3 = models.ImageField(upload_to=Uploader.upload_photo_for_about, verbose_name="Sol aşağı şəkil", help_text="224x224")
    img_4 = models.ImageField(upload_to=Uploader.upload_photo_for_about, verbose_name="Sağ aşağı şəkil", help_text="298x298")

    def __str__(self):
        return self.head

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Haqqımızda"
        verbose_name_plural = "Haqqımızda"

    def save(self, *args, **kwargs):
        if not self.id and AboutModel.objects.exists():
            myobj = AboutModel.objects.first()
            myobj.head = self.head
            myobj.description = self.description
            myobj.img_1 = self.img_1
            myobj.img_2 = self.img_2
            myobj.img_3 = self.img_3
            myobj.img_4 = self.img_4
            myobj.save()
        else:
            if not self.slug:
                self.slug = Generator.create_slug_shortcode(size=15, model_=AboutModel)
            super(AboutModel, self).save(*args, **kwargs)




class Personal(DateMixin, SlugMixin):
    full_name = models.CharField(max_length=255, verbose_name="İşçinin adı və soyadı")
    position = models.CharField(max_length=255, verbose_name="İşçinin vəzifəsi")
    image = models.ImageField(upload_to=Uploader.upload_photo_for_personal, verbose_name="İşçinin fotosu")

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "İşçi"
        verbose_name_plural = "İşçilər"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Personal)
        super(Personal, self).save(*args, **kwargs)


