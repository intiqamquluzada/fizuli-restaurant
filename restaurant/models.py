from django.db import models
from ckeditor.fields import RichTextField
from services.mixin import DateMixin, SlugMixin
from services.generator import Generator
from services.uploader import Uploader
from services.choices import SOCIAL_CHOICES
from services.extract import extract_yt_video_url_from_iframe

class AboutModel(DateMixin, SlugMixin):
    head = models.CharField(max_length=255, verbose_name="Haqqımızda başlıq hissəsi")
    description = RichTextField(verbose_name="Açıqlama")
    years_of_experience = models.CharField(max_length=255, verbose_name="Təcrübə")
    count_of_workers = models.CharField(max_length=255, verbose_name="İşçilərin sayı")
    img_1 = models.ImageField(upload_to=Uploader.upload_photo_for_about, verbose_name="Sol üst şəkil",
                              help_text="298x298")
    img_2 = models.ImageField(upload_to=Uploader.upload_photo_for_about, verbose_name="Sağ üst şəkil",
                              help_text="224x224")
    img_3 = models.ImageField(upload_to=Uploader.upload_photo_for_about, verbose_name="Sol aşağı şəkil",
                              help_text="224x224")
    img_4 = models.ImageField(upload_to=Uploader.upload_photo_for_about, verbose_name="Sağ aşağı şəkil",
                              help_text="298x298")

    def __str__(self):
        return self.head

    class Meta:
        ordering = ("-created_at",)
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


class Service(DateMixin, SlugMixin):
    name = models.CharField(max_length=255, verbose_name="Xidmətin adı")
    description = models.TextField(verbose_name="Xidmət haqqında")
    icon = models.ImageField(upload_to=Uploader.upload_photo_for_icon)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Xidmət"
        verbose_name_plural = "Xidmətlər"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Service)
        super(Service, self).save(*args, **kwargs)


class Category(DateMixin, SlugMixin):
    name = models.CharField(max_length=255, verbose_name="Kateqoriyalar")
    image = models.ImageField(upload_to=Uploader.upload_photo_for_icon, null=True, blank=True, verbose_name="Kateqoriya fotosu", help_text="286x286")


    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Category)
        super(Category, self).save(*args, **kwargs)


class Menu(DateMixin, SlugMixin):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to=Uploader.upload_photo_for_menu, verbose_name="Yeməyin şəkili",
                              help_text="80x80")
    food_name = models.CharField(max_length=255, verbose_name="Yeməyin adı")
    receipt = models.CharField(max_length=255, verbose_name="Yeməyin tərkibi")
    price = models.CharField(max_length=255, verbose_name="Yeməyin qiyməti")

    def __str__(self):
        return self.food_name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Menyu"
        verbose_name_plural = "Menyu"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Menu)
        super(Menu, self).save(*args, **kwargs)


class Contact(DateMixin, SlugMixin):
    name_and_surname = models.CharField(max_length=255, verbose_name="Adı və soyadı", null=True, blank=True)
    email = models.EmailField(verbose_name="Elektron poçtu", null=True, blank=True)
    subject = models.CharField(max_length=255, verbose_name="Mövzu", null=True, blank=True)
    message = models.TextField(verbose_name="Mesaj", null=True, blank=True)

    def __str__(self):
        return self.name_and_surname

    class Meta:
        ordering = ("-created_at",)
        verbose_name = 'Əlaqə saxlamaq istəyən şəxs'
        verbose_name_plural = 'Əlaqə saxlamaq istəyən şəxslər'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Contact)
        super(Contact, self).save(*args, **kwargs)


class Reserve(DateMixin, SlugMixin):
    name = models.CharField(max_length=255, verbose_name="Adı")
    phone_number = models.CharField(max_length=255, verbose_name="Əlaqə nömrəsi")
    reserve_date = models.DateTimeField(verbose_name="Rezerv tarixi və saatı")
    count_of_guest = models.IntegerField(verbose_name="Qonaq sayı")
    special_message = models.TextField(verbose_name="Xüsusi istək")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Rezerv"
        verbose_name_plural = "Rezervlər"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Reserve)
        super(Reserve, self).save(*args, **kwargs)


class HomeHeader(DateMixin, SlugMixin):
    main_text = models.TextField(verbose_name="Əsas cümlə")
    sub_text = models.TextField(verbose_name="Alt mətin")
    back_image = models.ImageField(upload_to=Uploader.upload_photo_for_home_header, verbose_name="Arxa plan foto",
                                   help_text="1366x768")
    round_image = models.ImageField(upload_to=Uploader.upload_photo_for_home_header, verbose_name="Fırlanan foto",
                                    help_text="612x612")

    def __str__(self):
        return self.main_text

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Ana səhifə başlıq"
        verbose_name_plural = "Ana səhifə başlıq"

    def save(self, *args, **kwargs):
        if not self.id and HomeHeader.objects.exists():
            myobj = HomeHeader.objects.first()
            myobj.main_text = self.main_text
            myobj.sub_text = self.sub_text
            myobj.back_image = self.back_image
            myobj.round_image = self.round_image
            myobj.save()
        else:
            if not self.slug:
                self.slug = Generator.create_slug_shortcode(size=15, model_=HomeHeader)
            super(HomeHeader, self).save(*args, **kwargs)


class Subscribe(DateMixin, SlugMixin):
    phone_number = models.CharField(max_length=255, verbose_name="Əlaqə nömrəsi", null=True, blank=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Abunə olan şəxs"
        verbose_name_plural = "Abunə olan şəxslər"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Subscribe)
        super(Subscribe, self).save(*args, **kwargs)


class MainDetails(DateMixin, SlugMixin):
    catering_menu_text = models.TextField(null=True, blank=True)
    location = models.TextField(verbose_name="Ünvan")
    phone_number = models.TextField(verbose_name="Əlaqə nömrəsi")
    email = models.EmailField(verbose_name="E-mail")
    working_time = models.TextField(verbose_name="İş vaxtları")
    logo = models.ImageField(upload_to=Uploader.upload_photo_for_logo, verbose_name="Saytın loqosu")
    video_url = models.TextField(verbose_name="Video linki", null=True, blank=True)
    map_url = models.TextField(verbose_name="Xerite linki", null=True, blank=True)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Əsas məlumat"
        verbose_name_plural = "Əsas məlumatlar"

    def save(self, *args, **kwargs):
        if not self.id and MainDetails.objects.exists():
            myobj = MainDetails.objects.first()
            myobj.location = self.location
            myobj.phone_number = self.phone_number
            myobj.working_time = self.working_time
            myobj.email = self.email
            myobj.logo = self.logo
            myobj.video_url = self.video_url

            extracted_url = extract_yt_video_url_from_iframe(self.video_url)
            map_url = extract_yt_video_url_from_iframe(self.map_url)
            if extracted_url:
                myobj.video_url = extracted_url
            if map_url:
                myobj.map_url = map_url

            myobj.save()
        else:
            if not self.slug:
                self.slug = Generator.create_slug_shortcode(size=15, model_=MainDetails)
            extracted_url = extract_yt_video_url_from_iframe(self.video_url)
            map_url = extract_yt_video_url_from_iframe(self.map_url)

            if extracted_url:
                self.video_url = extracted_url
            if map_url:
                self.map_url = map_url
            super(MainDetails, self).save(*args, **kwargs)




class SocialMedia(DateMixin, SlugMixin):
    social_media = models.CharField(max_length=255, choices=SOCIAL_CHOICES, verbose_name="Sosial media")
    link = models.TextField(verbose_name="Sosial media linki")

    def __str__(self):
        return self.social_media

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Sosial media hesab"
        verbose_name_plural = "Sosial media hesabları"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=SocialMedia)

        super(SocialMedia, self).save(*args, **kwargs)


class CateringMenuCategories(DateMixin):
    name = models.CharField(max_length=255,
                            verbose_name='Kateqoriya')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = 'Catering Menyu kateqoriya'
        verbose_name_plural = 'Catering Menyu kateqoriyaları'



class CateringMenu(DateMixin):
    category = models.ForeignKey(CateringMenuCategories, on_delete=models.SET_NULL,
                                 null=True, blank=True)
    image = models.ImageField(upload_to=Uploader.upload_photo_for_catering, null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name='Yemək adı')
    ingredients = models.TextField(verbose_name='Tərkibi')
    price = models.FloatField(verbose_name='Qiymət')


    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = 'Catering menu'
        verbose_name_plural = 'Catering menu'

