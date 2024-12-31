# 직렬화(Serialization): 객체를 JSON형식으로 변환합니다.
# 역직렬화(Deserialization): JSON형식을 객체로 변환합니다.
from rest_framework import serializers
from .models import User

# ModelSerializer를 상속받는 UserSerializer 클래스를 작성합니다.
class UserSerializer(serializers.ModelSerializer):
    # password를 쓰기 전용으로 설정하여 응답시에 반환하지 않도록 설정합니다.
    password = serializers.CharField(write_only=True)

    class Meta:
        # 직렬화할 모들을 설정합니다.
        model = User
        # 직렬화할 필드를 설정합니다.
        fields = "__all__"

    # User객체를 생성할 때 사용할 create메서드를 작성합니다.
def create(self, validated_data):
    # 허용된 이메일 도메인 리스트를 정의합니다.
    allowed_domains = ["gmail.com", "naver.com"]

    # 이메일에서 도메인 부분만 추출합니다.
    """
    email.split("@")는 "user@gmail.com"을 ["user", "gmail.com"]으로 나누고 
    그 후에 [-1]을 사용하여 리스트의 마지막 요소인 "gmail.com"을 가져옴
    """
    email = validated_data.get("email")
    domain = email.split("@")[-1]

    # 도메인이 허용된 리스트에 포함되어 있는지 확인합니다.
    if domain not in allowed_domains:
        raise serializers.ValidationError(f"허용되지 않은 이메일임 다시 확인해: {domain}")
    
    # 유저 생성 로직
    user = User(**validated_data)
    user.set_password(validated_data.get("password"))
    user.save()
    return user



# User의 세부 정보만 직렬화하는 UserDetailSerializer 클래스를 작성합니다.
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "nickname", "email", "phone_number", "last_login")