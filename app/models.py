class Source:
    
    '''
    class to define source objects
    '''

    def __init__(self,id,name,description,url,category,country):


        self.id=id
        self.name=name
        self.description=description
        self.url="http://www.bbc.co.uk/news"
        self.category=category
        self.country=country

class Articles:

    '''

    class that defines the article objects
    '''


    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt,content):
        


        self.id=id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content