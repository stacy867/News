class Source:
    sources= []
    '''
    news'source to define news_source objects
    '''
    
    def __init__(self,id,name,country,sourceurl):
        self.id = id
        self.name = name
        self.country = country
        self.sourceurl = sourceurl



        
    # def save_sources(self):
    #     Source.sources.append(self)
        
        
    # @classmethod
    # def clear_sources(cls):
    #     Source.sources.clear() 
        
    # @classmethod
    # def get_sources(cls,name1):
        
    #     response_source = []
        
    #     for src in cls.sources:
    #         if src.name == name1:
    #             response_source.append(src)
    #     return response       