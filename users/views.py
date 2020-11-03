from django.shortcuts import redirect
import urllib


# code 요청
def kakao_login(request):
    app_rest_api_key = "109df8ad3e3f058320388ab400d50464"
    redirect_uri = "http://ec2-18-220-10-141.us-east-2.compute.amazonaws.com:8000/account/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )


# access token 요청
def kakao_callback(request):
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'http://ec2-18-220-10-141.us-east-2.compute.amazonaws.com:8000/account/login/kakao/callback?{params}')