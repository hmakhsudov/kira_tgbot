from scrape_service import ScrapeService
from parser import Parser
from db_service import DbService
from base import Session


BASE_API_SEARCH_URL = 'https://menunedeli.ru'

session = Session()
db = DbService(session)

scraper = ScrapeService({
    "parser": Parser(),
    "db": DbService(session)
}, BASE_API_SEARCH_URL)

print(len(db.get_all_recipes()))
scraper.get_articles()
print(len(db.get_all_recipes()))
