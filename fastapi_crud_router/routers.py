from fastapi_crud_router.generics import RouterGeneric
from fastapi_crud_router.mixins import (
    RetrieveRouterMixin,
    ListRouterMixin,
    DeleteRouterMixin,
    CreateRouterMixin,
    UpdateRouterMixin,
    PartialUpdateRouterMixin
)


class ModelCRUDRouter(
    RouterGeneric,
    RetrieveRouterMixin,
    ListRouterMixin,
    DeleteRouterMixin,
    CreateRouterMixin,
    UpdateRouterMixin,
    PartialUpdateRouterMixin
):
    pass
