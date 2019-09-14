from flask import render_template
from app import app
from .request import get_source
from .request import get_article

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting sources
    news_sources = get_source('sports')
    print(news_sources)
    title = 'Home -welcome to the newswebsite'
    return render_template('index.html', title = title,news = news_sources)


# @app.route('/sources/<int:sources_id>')
# def source(source_id):

#     '''
#     View source page function that returns the sources  page
#     '''
#     return render_template('source.html',id = sources_id)


@app.route('/everything/<source_id>')
def source(source_id):

    '''
    View source page function that returns the articles  page
    '''
    news_articles = get_article('source_id')
    # print(news_articles)
    title = 'Home -welcome to articles'
    return render_template('articles.html',id = source_id, articles= news_articles)