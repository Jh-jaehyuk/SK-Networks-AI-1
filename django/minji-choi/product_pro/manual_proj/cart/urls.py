from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cart.controller.views import CartView

router = DefaultRouter()
router.register(r'cart', CartView, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path('list', CartView.as_view({'post': 'cartItemList'}), name='cart-list'), # userToken 정보가 들어가기 때문
    path('register', CartView.as_view({'post': 'cartRegister'}), name='cart-register'),
    path('remove', CartView.as_view({'post': 'cartRemove'}), name='cart-remove'),
]