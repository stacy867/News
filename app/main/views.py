from flask import render_template,request,redirect,url_for
# from app import app
from . import main
from ..request import get_source
from ..request import get_article
from ..models import Source,Article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting sources
    news_sources = get_source('entertainment')
    news_sources1= get_source('sports')
    news_sources2= get_source('business')
    print(news_sources)
    title = 'Home -welcome to the newswebsite'
    return render_template('index.html', title = title,news = news_sources,news1=news_sources1,news2=news_sources2)





@main.route('/everything/<source_id>')
def source(source_id):

    '''
    View source page function that returns the articles  page
    '''
    news_articles = get_article(source_id)
    

    title = 'article -welcome to articles'
    return render_template('articles.html',id = source_id,title = title,articles= news_articles)