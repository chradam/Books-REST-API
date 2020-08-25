from .models import Book, Author, Category


def import_books(data):

    for i in range(len(data)):
        item = data[i]['volumeInfo']
        book = {
            'title': item['title'],
            'published_date': item['publishedDate'][:4],
            'average_rating': item.get('averageRating'),
            'ratings_count': item.get('ratingsCount'),
            'thumbnail': item['imageLinks']['thumbnail']
        }

        book_instance, book_created = Book.objects.update_or_create(title=book['title'], published_date=book['published_date'],
                                            average_rating=book['average_rating'], ratings_count=book['ratings_count'],
                                            thumbnail=book['thumbnail'])

        for j in range(len(item['authors'])):
            author, author_created = Author.objects.update_or_create(name=item['authors'][j])
            book_instance.authors.add(author)

        if item.get('categories') is not None:
            for k in range(len(item['categories'])):
                category, category_created = Category.objects.update_or_create(name=item['categories'][k])
                book_instance.categories.add(category)

        book_instance.save()
