from knowledge_model import Base, People

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///People.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name, birth_year, alive, rate ):
        object_f=People(
                name = name,
                birth_year = birth_year,
                alive = alive,
                rate = rate)
        session.add(object_f)
        session.commit()
        
add_article("Michael Jackson", 1958, False, 100)
add_article("Barack Obama", 1961, True, 90)
add_article("Britney Spears",1981, True, 95)

def query_all_articles():
        articles = session.query(People).all()
        return articles
print (query_all_articles())

def query_article_by_topic(thier_name):
        articles = session.query(People).filter_by(name=thier_name)
        return articles
print(query_article_by_topic("Michael Jackson"))

def delete_article_by_topic(name):
	session.query(People).filter_by(
                name=name).delete()
	session.commit()
delete_article_by_topic("Barack Obama")

def delete_all_articles():
        session.query(People).delete()
        session.commit()
delete_all_articles()

"""
def edit_article_rating(name, alive):
        object_f = session.query(
                People).filter_by(
                name=name).first()
        object_f.alive = alive
        session.commit()
edit_article_rating("Britney Spears", False)
"""

print (query_all_articles())
