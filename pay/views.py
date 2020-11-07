from django.shortcuts import render
from django.views.generic import View

import payjp


# Create your views here.
class PayView(View):
    """
    use PAY.JP API
    """

    def get(self, request):
        # 公開鍵を渡す
        return render(
            request, "pay/index.html", {"public_key": "pk_test_9bedc31c6c0d2e5d1f5b609b"}
        )

    def post(self, request):
        amount = request.POST.get("amount")
        payjp_token = request.POST.get("payjp-token")

        # トークンから顧客情報を生成
        customer = payjp.Customer.create(email="example@pay.jp", card=payjp_token)
        # 支払いを行う
        charge = payjp.Charge.create(
            amount=amount,
            currency="jpy",
            customer=customer.id,
            description="Django example charge",
        )

        context = {"amount": amount, "customer": customer, "charge": charge}
        return render(request, "index.html", context)
