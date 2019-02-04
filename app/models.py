# source class
class Sources:
    '''
    Source class to define Objects
    '''

    def __init__(self,id,name,description):
        self.id =id
        self.name = name
        self.description = description


# Article class
class Articles:
    '''
    Article class to define Objects
    '''

    def __init__(self,id,name,description,title,author,url,urlToImage,publishedAt):
        self.id =id
        self.name = name
        self.author= author
        self.title = title
        self.description = description
        self.url = url 
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt