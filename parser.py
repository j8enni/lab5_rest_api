# parser.py
import requests

def get_books(query):
    # Формируем запрос к Google Books API
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&orderBy=relevance'
    response = requests.get(url)
    data = response.json()
    exact_matches = []
    partial_matches = []

    # Приводим запрос к нижнему регистру для поиска совпадений
    lower_query = query.lower()

    for item in data.get('items', []):
        book_info = item.get('volumeInfo', {})
        
        # Получаем данные книги
        title = book_info.get('title', '').lower()
        authors = [author.lower() for author in book_info.get('authors', [])]
        
        # Проверяем на полное совпадение по названию или автору
        if lower_query == title or lower_query in authors:
            exact_matches.append({
                'title': book_info.get('title'),
                'authors': book_info.get('authors', ['Unknown']),
                'description': book_info.get('description', 'No description available'),
                'thumbnail': book_info.get('imageLinks', {}).get('thumbnail')
            })
        else:
            # Если нет полного совпадения, добавляем в список частичных совпадений
            partial_matches.append({
                'title': book_info.get('title'),
                'authors': book_info.get('authors', ['Unknown']),
                'description': book_info.get('description', 'No description available'),
                'thumbnail': book_info.get('imageLinks', {}).get('thumbnail')
            })

    # Возвращаем книги с полным совпадением первыми, а затем частичные совпадения
    return exact_matches + partial_matches
