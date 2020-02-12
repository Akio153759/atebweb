from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
    nombre_categoria = models.CharField('Nombre Categoria', max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre_categoria


class Publicacion(models.Model):
    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    fecha_publicacion = models.DateTimeField('Fecha Publicacion', blank=False, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    titulo = models.CharField('Titulo', null=False,blank=False,max_length=50)
    resumen = models.TextField('Resumen',max_length=300, blank=False, null=False)
    contenido = models.TextField('Contenido', null=False, blank=False, max_length=1000)
    foto_portada = models.ImageField(upload_to= 'fotopublicaciones', blank=False, null=False)
    foto_1 = models.ImageField(upload_to= 'fotopublicaciones', blank=True, null=True)
    foto_2 = models.ImageField(upload_to= 'fotopublicaciones', blank=True, null=True)
    foto_3 = models.ImageField(upload_to= 'fotopublicaciones', blank=True, null=True)
    foto_4 = models.ImageField(upload_to= 'fotopublicaciones', blank=True, null=True)
    foto_5 = models.ImageField(upload_to= 'fotopublicaciones', blank=True, null=True)
    
    
    
    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

    

class Equipo(models.Model):
    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    nombre = models.CharField('Nombre Equipo', max_length=30, blank=False, null=False)
    abreviacion = models.CharField('Abreviación Equipo', max_length=5,blank=False, null=False)
    logo_equipo = models.ImageField(upload_to= 'logoequipos', blank=False, null=False)

    def __str__(self):
        return self.nombre



class Fecha(models.Model):
    class Meta:
        verbose_name = "Fecha"
        verbose_name_plural = "Fechas"
    
    nombre_fecha = models.CharField('Nombre Fecha', max_length=15, blank=False, null=False)
    
    def __str__(self):
        return '{}'.format(self.nombre_fecha)



class Partido(models.Model):
    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"


    fecha = models.ForeignKey(Fecha, blank=False, null=False, on_delete=models.CASCADE)
    fecha_partido = models.DateTimeField('Fecha de Partido',blank=False, null=False)
    equipo1 = models.ForeignKey(Equipo, blank=False, null=False, on_delete=models.PROTECT)
    equipo2 = models.ForeignKey(Equipo, blank=False, related_name='equipo_2', null=False, on_delete=models.PROTECT)

    def __str__(self):
        return '{} vs {}'.format(self.equipo1, self.equipo2)


class FotoGaleria(models.Model):
    class Meta:
        verbose_name = "Foto Para Galería"
        verbose_name_plural = "Fotos Para Galería"

    foto = models.ImageField(upload_to = 'gallery', blank=False, null=False)

class VideoGaleria(models.Model):
    class Meta:
        verbose_name = 'Video para Galería'
        verbose_name_plural = 'Videos para Galería'
    
    video = models.FileField(upload_to= 'gallery', blank=False, null=False)