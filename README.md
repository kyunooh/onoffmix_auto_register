# 온오프믹스 자동 등록

## 주의사항
**본 프로그램 사용으로인한 법적인 것을 포함한 모든 책임은 사용자에게 있습니다. 또한 본 프로그램은 어디까지나 임시방편입니다. 프로그램을 실행한 뒤 다른 브라우저로도 열심히 수강 신청하세요.**

## 준비

### 파이어폭스 설치
현재 셀레늄이 파이어 폭스를 바라보고 있으므로 **파이어폭스를 설치**한다. 최신버전의 파이어폭스는 현재 셀레늄이 개발중이어서 불가능 하다. 아래에서 47 버전을 다운 받는다.
https://support.mozilla.org/ko/kb/install-older-version-of-firefox

### 파이썬 의존성 설치
터미널에서 해당 폴더로 이동해 아래와 같은 명령어를 이용해 의존성을 설치한다.
```shell
pip install --upgrade -r requirements.txt
```

## 스크립트 수정

### 이메일과 비밀번호 수정
아래와 같이 로그인 정보를 수정한다.

```python
email = "nickname@example.com"
pw = "password"
```

### login type 수정
아래와 같이 로그인 타입을 정한다. (현재 온오프믹스와 페이스북만 지원한다.)
```python
login_type = "facebook"
```

### 모임 URL 설정
아래와 같이 모임의 주소를 설정해준다.
```python
meetup_url = "http://onoffmix.com/event/76453"
```

## 실행
아래의 명령어를 사용해 실행한다.
```shell
python onoffmix_auto_register.py
```


