from pyramid.config import Configurator
from pyramid.events import NewRequest
from pyramid.events import subscriber
from pyramid.events import ApplicationCreated
from pyramid.session import UnencryptedCookieSessionFactoryConfig
import sqlite3
import os
import logging

logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))

@subscriber(ApplicationCreated)
def application_created_subscriber(event):
    log.warn('Initializing datanase...')
    with open(os.path.join(here, 'schema.sql')) as f:
        stmt = f.read()
        settings=event.app.registry.settings
        db = sqlite3.connect(settings['db'])
        db.executescript(stmt)
        db.commit()

@subscriber(NewRequest)
def new_request_subscriber(event):
    request=event.request
    settings = request.registry.settings
    request.db = sqlite3.connect(settings['db'])
    request.add_finished_callback(close_db_connection)

def close_db_connection(request):
    request.db.close()

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings['mako.directories'] = os.path.join(here, 'templates')
    settings['reload_all'] = True
    settings['debug_all'] = True
    settings['db'] = os.path.join(here, 'growstats.db')
    
    session_factory = UnencryptedCookieSessionFactoryConfig('not for your eyes, mine only')
    
    config = Configurator(settings=settings, session_factory=session_factory)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('list','/list')
    config.add_route('timeline', '/timeline')
    config.add_route('addsupply', '/add/supply')
    config.add_route('addcolumn', '/add/column')
    config.add_route('addslot','/add/slot')
    config.add_route('addplant','/add/plant')
    config.add_route('addtimer','/add/timerconfig')
    config.add_route('watering','/record/watering')
    config.add_route('water','/record/water')
    config.add_route('nutrients','/record/nutrients')
    config.add_route('ph','/record/ph')
    config.add_route('ec','/record/ec')
    config.add_route('temp','/record/temp')
    config.add_route('humidity','/record/humidity')
    config.add_route('height','/record/height')
    config.add_route('harvest','/record/harvest')
    config.add_route('pic','/record/picture')
    config.add_route('log','/record/log')
    config.add_route('editsupply','/edit/supply/{id}')
    config.add_route('editcolumn','/edit/supply/{id}')
    config.add_route('editslot','/edit/slot/{id}')
    config.add_route('editplant','/edit/plant/{id}')
    config.add_route('edittimer','/edit/timerconfig/{id}')
    config.add_route('editwatering','/edit/watering/{id}')
    config.add_route('editwater','/edit/water/{id}')
    config.add_route('editnutrients','/edit/nutrients/{id}')
    config.add_route('editph','/edit/ph/{id}')
    config.add_route('editec','/edit/ec/{id}')
    config.add_route('edittemp','/edit/temp/{id}')
    config.add_route('edithumidity','/edit/humidity/{id}')
    config.add_route('editlength','/edit/length/{id}')
    config.add_route('editharvest','/edit/harvest/{id}')
    config.add_route('editpic','/edit/picture/{id}')
    config.add_route('editlog','/edit/log/{id}')
    config.scan()
    return config.make_wsgi_app()
