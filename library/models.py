from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class Book(models.Model):
    GENRE_CHOICES = [  # new
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science Fiction', 'Science Fiction'),
        ('Fantasy', 'Fantasy'),
        ('M', 'Mystery'),
        ('Biography', 'Biography'),
    ]

    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', null=True, on_delete=models.SET_NULL)
    publishing_date = models.DateField()
    # Task 5
    summary = models.TextField(null=True, blank=True)  # new
    genre = models.CharField(max_length=50, null=True, choices=GENRE_CHOICES)  # new
    page_count = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(10000)])
    publisher_member = models.ForeignKey('Member', null=True, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL, related_name='books')
    libraries = models.ManyToManyField('Library', related_name='books')

    @property
    def rating(self):
        reviews = self.reviews.all()
        total_reviews = reviews.count()

        if total_reviews == 0:
            return 0

        total_rating = sum(review.rating for review in reviews)
        average_rating = total_rating / total_reviews

        return round(average_rating, 2)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    birth_date = models.DateField(verbose_name="Дата рождения")

    # Task 2
    profile = models.URLField(null=True, blank=True, verbose_name="Ссылка на профиль")
    deleted = models.BooleanField(default=False, verbose_name="Удалён ли автор",
                                  help_text="Если False - автор активен. Если True - автора \
                                  больше нет в списке доступных")

    rating = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Рейтинг автора"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]

    ROLE_CHOICES = [
        ('stuff', 'Stuff'),
        ('reader', 'Reader')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    age = models.IntegerField(validators=[MinValueValidator(6), MaxValueValidator(120)],
                          error_messages={'min_value': 'Please more', 'max_value': 'Please less!!!!!!!'})
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    active = models.BooleanField(default=True)
    libraries = models.ManyToManyField('Library', related_name='members')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Posts(models.Model):
    title = models.CharField(max_length=255, unique_for_date='created_at')
    body = models.TextField()
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='posts')
    moderated = models.BooleanField(default=False)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Borrow(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='borrows')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrows')
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='borrows')
    borrow_date = models.DateField()
    return_date = models.DateField()
    returned = models.BooleanField(default=False)

    def is_overdue(self):
        if self.returned:
            return False
        return self.return_date < timezone.now().date()


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='reviews')
    rating = models.FloatField()
    description = models.TextField()


class AuthorDetail(models.Model):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]

    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='details')
    biography = models.TextField()
    birth_city = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='events')
    books = models.ManyToManyField(Book, related_name='events')


class EventParticipant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    member = models.ManyToManyField(Member, related_name='event_participations')
    registration_date = models.DateField(default=timezone.now)


