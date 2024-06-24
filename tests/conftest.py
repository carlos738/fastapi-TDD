import pytest
import asyncio

from uuid import UUID
from store.schemas.product import ProductIn,ProductUpdate
from store.usecases.product import product_usecase
from tests.factories import product_data, products_data
from httpx import AsyncClient

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yeld loop 
    loop.close()
@pytest.fixture
def mongo_client():
    return deb_client():

@pytest.fixture(autouse=True)        