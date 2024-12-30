from django.db import models


class BaseModel(models.Model):
    # auto_now_add: 현재 데이터 생성 시간을 기준으로 생성이 된다 -> 이후 데이터가 업데이트 되어도 수정되지 않는다.
    created_at = models.DateTimeField(auto_now_add=True)

    # auto_now: 생성되는 시간 기준으로 일단 생성된다. -> 이후 데이터가 업데이트가 되면 시간도 업데이트된 현재 시간을 기준으로 업데이트된다.
    updated_at = models.DateTimeField(auto_now=True)

    # 메타데이터를 정의하는 내부 클래스인 Meta라는 클래스를 작성
    class Meta:
        # 추상클래스로 설정해주어서 데이터베이스의 테이블에 위와 같은 컬럼이 추가되지 않는다.
        abstract = True
