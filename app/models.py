## source class
class Source:
    sources= []
    '''
    news'source to define news_source objects
    '''
    
    def __init__(self,id,name,description,sourceurl):
        self.id = id
        self.name = name
        self.description = description
        self.sourceurl = sourceurl


## article class
class Article:
    articles= []
    '''
    news'article to define articles objects
    '''
    
    def __init__(self,author,tittle,imageurl,description,time,url):
        self.author = author
        self.tittle = tittle
        self.imageurl = imageurl
        self. description = description
        self.time = time 
        self.url = url