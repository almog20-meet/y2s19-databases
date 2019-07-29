from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class People(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

        __tablename__ = "famous peoples"
        table_id = Column(Integer, primary_key=True)
        name = Column (String)
        birth_year = Column (Integer)
        alive = Column (Boolean)
        rate = Column (Integer)
        def __repr__(self):
                return (" Famous Name: {}\n"
                        " Famous birth year : {}\n"
                        "Famous is live : {}\n"
                        "rating: {}\n" ). format (
                                self.name, self.birth_year, self.alive, self.rate)

x = People( name = "Michael Jackson" , birth_year= 1958, alive= False, rate = 10000)
print (x)


