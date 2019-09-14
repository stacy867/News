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
    news_sources = get_source('news')
    # print(news_sources)
    title = 'Home -welcome to the newswebsite'
    return render_template('index.html', title = title, news = news_sources)


# @app.route('/sources/<int:sources_id>')
# def source(source_id):

#     '''
#     View source page function that returns the sources  page
#     '''
#     return render_template('source.html',id = sources_id)


# @app.route('/everything/<int:articles_id>')
# def source(articles_id):

#     '''
#     View source page function that returns the articles  page
#     '''
#     return render_template('articles.html',id = articles_id)