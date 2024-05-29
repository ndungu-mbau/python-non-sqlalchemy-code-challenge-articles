class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        author.articles_list.append(self)
        magazine.article_list.append(self)

class Author:
    def __init__(self, name):
        self.name = name
        self.articles_list = []

    def articles(self):
        return self.articles_list

    def magazines(self):
        return list(set([article.magazine for article in self.articles_list]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set([article.magazine.category for article in self.articles_list]))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.article_list = []

    def articles(self):
        return self.article_list

    def contributors(self):
        return list(set([article.author for article in self.article_list]))

    def article_titles(self):
        return [article.title for article in self.article_list]

    def contributing_authors(self):
        authors_count = {}
        return [author for author, count in authors_count.items() if count > 2]

