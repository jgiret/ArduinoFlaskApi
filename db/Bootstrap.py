# -*- coding: utf-8 -*-
# @Author: Jean-Christophe Giret
# @Date:   2018-01-08 22:21:54
# @Last Modified by:   Jean-Christophe Giret
# @Last Modified time: 2018-01-08 22:26:38

from Sqlite import engine
from sqlalchemy.ext.declarative import declarative_base
from models import OregonData

Base = declarative_base()
Base.metadata.create_all(engine)
