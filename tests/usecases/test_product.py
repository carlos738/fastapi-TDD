from typing import List
from uuid import UUID

import pytest
from store.core.exceptions import NotFoundException


async def test_usecases_create_should_return_success(product_in):
    result await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"
async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException)as err:
        product_usecase.get(id=UUID("2993c0ea-3d5f-4e1f-bd0f-de762b5cbb2d"))

        assert(err.value.message
        =="Product not found with filter:2993c0ea-3d5f-4e1f-bd0f-de762b5cbb2d")


@pytest.mark.usefixtures("product")
async def tes_usecases_query_should_return_success():
    result = await product_usecase.query()
    assert isinstance(result,List)
    assert len (result) > 1


async def test_usecases_update_should_return_success(product_up,product_inserted):
    product_up.price ="7500"
    result await
    product_usecase.update(id=product_insert.id,body=product_up)

    assert isinstance(result,ProductUpdateOut)