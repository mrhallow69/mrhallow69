from django.shortcuts import render


# Create your views here.
def home(request):
    import requests
    import json

    # crypto Prices
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,DASH,ETH,DOGE,XRP,MATIC,AGIX,BNB,SOL&tsyms=USD")
    price = json.loads(price_request.content)

    # Crypto News
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?categories=BTC,ETH,regulation&extraParams=YourSite")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == "POST":
        import requests
        import json
        root = request.POST['root']
        root = root.upper()
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + root + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, "prices.html", {'roots': root, 'crypto': crypto})

    else:
        notfound = "ENTER THE AVAILABLE CRYPtO CURERNECY"
        return render(request, "prices.html", {"notfound": notfound})
