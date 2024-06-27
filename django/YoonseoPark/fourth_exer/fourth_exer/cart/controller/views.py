from rest_framework import viewsets, status
from rest_framework.response import Response

from cart.entity.cart import Cart
from cart.service.cart_service_impl import CartServiceImpl
from oauth.service.redis_service_impl import RedisServiceImpl


class CartView(viewsets.ViewSet):
    queryset = Cart.objects.all()
    cartService = CartServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def cartItemList(self, request):
        data = request.data
        userToken = data.get('userToken')

        if not userToken:
            return Response({'error': 'User token is required'}, status=status.HTTP_400_BAD_REQUEST)

        accountId = self.redisService.getValueByKey(userToken)
        if not accountId:
            return Response({'error': 'Invalid user token'}, status=status.HTTP_400_BAD_REQUEST)

        cartItemListResponseForm = self.cartService.cartList(accountId)
        return Response(cartItemListResponseForm, status=status.HTTP_200_OK)

    def cartRegister(self, request):
        try:
            data = request.data
            print('data:', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            self.cartService.cartRegister(data, accountId)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('상품 등록 과정 중 문제 발생:', e)
            return Response({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def cartRemove(self, request):
        try:
            data = request.data
            userToken = data.get('userToken')

            if not userToken:
                return Response({'error': 'User token is required'}, status=status.HTTP_400_BAD_REQUEST)

            accountId = self.redisService.getValueByKey(userToken)
            if not accountId:
                return Response({'error': 'Invalid user token'}, status=status.HTTP_400_BAD_REQUEST)

            cartItemId = data.get('cartItemId')
            if not cartItemId:
                return Response({'error': 'cartItemId is required'}, status=status.HTTP_400_BAD_REQUEST)

            self.cartService.removeCartItem(accountId, cartItemId)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('장바구니 정리 중 문제 발생:', e)