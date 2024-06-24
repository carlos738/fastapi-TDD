from typing import List
from uuid import UUID

import pytest
from store.core.exceptions import NotFoundException


async def test_usecases_create_should_return_success(product_in):
    result await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"