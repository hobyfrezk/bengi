from django.db import models
import uuid


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.image.url


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class News(models.Model):
    class Meta:
        verbose_name_plural = "News"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField("date published")
    images = models.ManyToManyField(Image)
    main_image = models.ForeignKey(
        Image,
        related_name="news_main_image",
        on_delete=models.SET_NULL,
        null=True,
    )
    tags = models.ManyToManyField(Tag)

    def get_main_image(self):
        # If there is a main image, return it, else, if there are any images
        # related to this news, return the first one ordered by created_at
        if self.main_image:
            return self.main_image
        elif self.images.exists():
            return self.images.order_by("created_at").first()
        else:
            return None

    def __str__(self):
        return self.title
