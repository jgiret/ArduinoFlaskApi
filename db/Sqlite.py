# -*- coding: utf-8 -*-
# @Author: Jean-Christophe Giret
# @Date:   2018-01-08 22:10:53
# @Last Modified by:   Jean-Christophe Giret
# @Last Modified time: 2018-01-08 22:24:21

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
