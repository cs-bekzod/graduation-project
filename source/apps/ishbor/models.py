from django.db import models
from datetime import datetime 
from django.urls import reverse
from django.db.models import Count
from django.contrib.auth.models import User


class Categories(models.Model):
    title = models.CharField(max_length=50)
    icon_name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Kategoriyalar'
        
    def __str__(self):
        return self.title
    
    
class Jobs(models.Model):
    LOCATION_CHOICES = (
    ("Toshkent shahri", "Toshkent shahri"),
    ("Andijon viloyati", "Andijon viloyati"),
    ("Toshkent viloyati", "Toshkent viloyati"),
    ("Buxoro viloyati", "Buxoro viloyati"),
    ("Samarqand viloyati", "Samarqand viloyati"),
    ("Sirdaryo viloyati", "Sirdaryo viloyati"),
    ("Surxondaryo viloyati", "Surxondaryo viloyati"),
    ("Navoiy viloyati", "Navoiy viloyati"),
    ("Namangan viloyati", "Namangan viloyati"),
    ("Xorazm viloyati", "Xorazm viloyati"),
    ("Farg'ona viloyati", "Farg'ona viloyati"),
    ("Qashqadaryo viloyati", "Qashqadaryo viloyati"),
    ("Qoraqalpog'iston Respublikasi", "Qoraqalpog'iston Respublikasi"),
    )
    
    JOB_TYPE_CHOICES = (
    ("To'liq ish kuni", "To'liq ish kuni"),
    ("Yarim ish kuni", "Yarim ish kuni"),
    ("Kontrakt asosida", "Kontrakt asosida"),
    ("Masofaviy", "Masofaviy"),
    ("Internship (amaliyot)", "Internship (amaliyot)"), 
    )
    
    title = models.CharField(max_length = 150)
    image = models.ImageField("Kompaniya logosi", upload_to='jobs')
    locations = models.CharField(max_length=150, choices=LOCATION_CHOICES)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField("Oylikni dollarda kiriting")
    about_job = models.TextField("Ish haqida batafsil")
    about_company = models.TextField("Kompaniya haqida qisqacha")
    phone = models.CharField("Aloqa uchun telefon raqam", max_length = 150)
    email = models.CharField("Xodim aloqaga chiqishi uchun email", max_length = 150)
    tg_username = models.CharField("Aloqa uchun Telegram username (@ belgisi bilan yozing)", max_length = 150)
    linkedin = models.CharField("Aloqa uchun Linkedin profilingiz linki", max_length = 150)
    created_at  = models.DateTimeField(default=datetime.now())
    
    class Meta:
        verbose_name_plural = "Ish o'rinlari"
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("job_detail", kwargs={
            "id": self.id
        })
        
        
class Universities(models.Model):
    LOCATION_CHOICES = (
    ("Toshkent shahri", "Toshkent shahri"),
    ("Andijon viloyati", "Andijon viloyati"),
    ("Toshkent viloyati", "Toshkent viloyati"),
    ("Buxoro viloyati", "Buxoro viloyati"),
    ("Samarqand viloyati", "Samarqand viloyati"),
    ("Sirdaryo viloyati", "Sirdaryo viloyati"),
    ("Surxondaryo viloyati", "Surxondaryo viloyati"),
    ("Navoiy viloyati", "Navoiy viloyati"),
    ("Namangan viloyati", "Namangan viloyati"),
    ("Xorazm viloyati", "Xorazm viloyati"),
    ("Farg'ona viloyati", "Farg'ona viloyati"),
    ("Qashqadaryo viloyati", "Qashqadaryo viloyati"),
    ("Qoraqalpog'iston Respublikasi", "Qoraqalpog'iston Respublikasi"),
    )
    
    UNIVERSITY_TYPE_CHOICES = (
    ("Mahalliy", "Mahalliy"),
    ("Xorijiy", "Xorijiy"),
    )
    
    name = models.CharField(max_length=100)
    image = models.ImageField("Universitet logosi",upload_to='universities')
    location = models.CharField("Joylashuv", max_length=150, choices=LOCATION_CHOICES)
    number_of_students = models.PositiveIntegerField("Talabalar soni")
    university_type = models.CharField("Turi", max_length=150, choices=UNIVERSITY_TYPE_CHOICES)
    rank = models.PositiveIntegerField(default=0)
    link = models.CharField("Website", max_length=100)

    class Meta:
        verbose_name_plural = 'Universitetlar ro`yxati'
        
    def __str__(self):
        return self.name
    

class Candidates(models.Model):
    
    LOCATION_CHOICES = (
    ("Toshkent shahri", "Toshkent shahri"),
    ("Andijon viloyati", "Andijon viloyati"),
    ("Toshkent viloyati", "Toshkent viloyati"),
    ("Buxoro viloyati", "Buxoro viloyati"),
    ("Samarqand viloyati", "Samarqand viloyati"),
    ("Sirdaryo viloyati", "Sirdaryo viloyati"),
    ("Surxondaryo viloyati", "Surxondaryo viloyati"),
    ("Navoiy viloyati", "Navoiy viloyati"),
    ("Namangan viloyati", "Namangan viloyati"),
    ("Xorazm viloyati", "Xorazm viloyati"),
    ("Farg'ona viloyati", "Farg'ona viloyati"),
    ("Qashqadaryo viloyati", "Qashqadaryo viloyati"),
    ("Qoraqalpog'iston Respublikasi", "Qoraqalpog'iston Respublikasi"),
    )
    
    DEGREE_CHOICES = (
    ("Maktab o'quvchisi", "Maktab o'quvchisi"),
    ("O'rta maxsus", "O'rta maxsus"),
    ("Oliy ma'lumotli", "Oliy ma'lumotli"), 
    )
    STATUS_CHOICES = (
    ("Ishsiz", "Ishsiz"),
    ("Ish joyi bor", "Ish joyi bor"),
    )
    
    JOB_TYPE_CHOICES = (
    ("To'liq ish kuni", "To'liq ish kuni"),
    ("Yarim ish kuni", "Yarim ish kuni"),
    ("Kontrakt asosida", "Kontrakt asosida"),
    ("Masofaviy", "Masofaviy"),
    ("Internship (amaliyot)", "Internship (amaliyot)"), 
    )
    
    first_name = models.CharField("Ism" ,max_length=70)
    last_name = models.CharField("Familiya" ,max_length=70)
    image = models.ImageField("Profil rasmi",upload_to='candidates')
    profession = models.CharField("Kasb" ,max_length=100)
    experience = models.PositiveIntegerField("Tajriba (yilda)")
    degree = models.CharField("Ma'lumoti", max_length=150, choices=DEGREE_CHOICES)
    college_name = models.CharField("O'quv muassasangiz nomi" ,max_length=200)
    university_name = models.ForeignKey(Universities, on_delete=models.CASCADE)
    job_type = models.CharField("Ish turi", max_length=150, choices=JOB_TYPE_CHOICES)
    GPA = models.CharField("GPA (masalan 4.7/5)" ,max_length=70)
    email = models.CharField("Email" ,max_length=70)
    tg_username = models.CharField("Aloqa uchun Telegram username (@ belgisi qo'shmang)", max_length = 150)
    phone = models.CharField("Aloqa uchun telefon raqam", max_length = 150)
    linkedin = models.CharField("Aloqa uchun Linkedin profilingiz linki", max_length = 150)
    locations = models.CharField("Joylashuv", max_length=150, choices=LOCATION_CHOICES)
    status = models.CharField("Hozirgi holati", max_length=150, choices=STATUS_CHOICES)
    about_me = models.TextField("O'zingiz haqingizda qisqacha yozing")
    created_at  = models.DateTimeField(default=datetime.now())
    
    

    class Meta:
        verbose_name_plural = 'Xodimlar'
        
    def __str__(self):
        return self.first_name
    
    
class Events(models.Model):
    LOCATION_CHOICES = (
    ("Toshkent shahri", "Toshkent shahri"),
    ("Andijon viloyati", "Andijon viloyati"),
    ("Toshkent viloyati", "Toshkent viloyati"),
    ("Buxoro viloyati", "Buxoro viloyati"),
    ("Samarqand viloyati", "Samarqand viloyati"),
    ("Sirdaryo viloyati", "Sirdaryo viloyati"),
    ("Surxondaryo viloyati", "Surxondaryo viloyati"),
    ("Navoiy viloyati", "Navoiy viloyati"),
    ("Namangan viloyati", "Namangan viloyati"),
    ("Xorazm viloyati", "Xorazm viloyati"),
    ("Farg'ona viloyati", "Farg'ona viloyati"),
    ("Qashqadaryo viloyati", "Qashqadaryo viloyati"),
    ("Qoraqalpog'iston Respublikasi", "Qoraqalpog'iston Respublikasi"),
    )
    
    title = models.CharField("Mavzu", max_length=50)
    locations = models.CharField("Joylashuv",default="Toshkent shahri", max_length=150, choices=LOCATION_CHOICES)
    image = models.ImageField("Rasm",upload_to='events', null=True)
    price = models.CharField("Qatnashish narxi", default="Bepul",max_length=200)
    count = models.CharField("Qatnashuvchilar soni" ,default=150,max_length=200)
    start_time = models.DateTimeField("Boshlanish vaqti", default=datetime.now())
    phone = models.CharField("Aloqa uchun telefon raqam", default="+998977737373", max_length = 150)
    email = models.CharField("Email" ,default="example@gmail.com", max_length=70)
    about_event = models.TextField("Tadbir haqida yozing", default="Dasturchilar uchun masterklass")
    created_at = models.DateTimeField( default=datetime.now)
    

    class Meta:
        verbose_name_plural = 'Tadbirlar'
        
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)      
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = 'Xabarlar'
    
