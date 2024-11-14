from django.db import models
from django.contrib.auth.models import User

def avatar_upload_to(instance, filename):
    name, extension = filename.split('.')
    email = instance.user
    return f'avatars/{email}.{extension}'

def shoe_gallery_upload_to(instance, filename):
    shoe_model = instance.shoe.model
    extension = filename.split('.')[-1]
    return f'images/shoes/{shoe_model}/gallery/{filename}'
    
class Address(models.Model):
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    
    def __str__(self):
        return f"{self.street} {self.house_number}, {self.city}, {self.postal_code}, {self.country}"
    
    class Meta:
        verbose_name_plural = "Addresses"

class UserDetails(models.Model):
    GENDER_CHOICES = {
        ('male', 'Męskie'),
        ('female', 'Damskie'),
        ('unisex', 'Uniseks')
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userEmail")
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    preferedGender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    dateOfBirth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to=avatar_upload_to, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Details"
    
    class Meta:
        verbose_name_plural = "UsersDetails"

class ShoeColors(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "ShoesColors"
    
class Manufacturers(models.Model):
    brand = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.brand}"
    
    class Meta:
        verbose_name_plural = "Manufacturers"
    
class ShoeSizes(models.Model):
    size = models.CharField(max_length=3)
    
    def __str__(self):
        return f"{self.size}"
    
    class Meta:
        verbose_name_plural = "ShoeSizes"
    
class ShoeCategories(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "ShoeCategories"
    
class ShoeCollections(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "ShoeCollections"
    
class Shoe(models.Model):
    GENDER_CHOICES = {
        ('male', 'Męskie'),
        ('female', 'Damskie'),
        ('unisex', 'Uniseks')
    }
    SHOE_HIGH_CHOICES = {
        ('low', 'Low Top'),
        ('mid', 'Mid Top'),
        ('high', 'High Top')
    }
    manufacturer = models.ForeignKey(Manufacturers, on_delete=models.CASCADE)
    shoe_sizes = models.ManyToManyField(ShoeSizes)
    category = models.ForeignKey(ShoeCategories, on_delete=models.CASCADE)
    collection = models.ForeignKey(ShoeCollections, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default="Shoe Description")
    bestseller = models.BooleanField(blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    shoe_high = models.CharField(max_length=50, choices=SHOE_HIGH_CHOICES)

    def __str__(self):
        return f"Shoe model: {self.model}"

    class Meta:
        verbose_name_plural = "Shoes"
        
class ShoeImageGallery(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE, related_name='images_gallery')
    color = models.CharField(max_length=10, default="black")
    image1 = models.ImageField(upload_to=shoe_gallery_upload_to, null=True)
    image2 = models.ImageField(upload_to=shoe_gallery_upload_to, null=True)
    image3 = models.ImageField(upload_to=shoe_gallery_upload_to, null=True)
    image4 = models.ImageField(upload_to=shoe_gallery_upload_to, null=True)

    def __str__(self):
        return f"Gallery Image for {self.shoe.model} {self.color}"

    class Meta:
        verbose_name_plural = "Shoe Images Gallery"
        
class ShoeVariant(models.Model):
    shoe = models.ForeignKey(Shoe, related_name="variants", on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColors, on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to="images/shoes/main_images/", default="images/mainImages/default_shoe.png")
    images_gallery = models.ManyToManyField(ShoeImageGallery)

    def __str__(self):
        return f"{self.shoe.model} - {self.color.name}"

    class Meta:
        verbose_name_plural = "Shoe Variants"