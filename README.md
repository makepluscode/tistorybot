# Tistory 자동 로그인 봇

이 프로젝트는 Selenium을 사용하여 Tistory에 자동으로 로그인하는 Python 스크립트입니다.

## 기능

- Tistory 로그인 페이지 자동 접속
- 카카오 계정을 통한 자동 로그인
- 로그인 성공 여부 확인
- 스크린샷 저장

## 필요 조건

- Python 3.7+
- Chrome 브라우저
- ChromeDriver (WebDriver Manager에 의해 자동으로 관리됨)

## 설치

1. 이 저장소를 클론합니다:

```bash
git clone https://github.com/yourusername/tistory-auto-login.git
cd tistory-auto-login
```

2. 필요한 패키지를 설치합니다:

```bash
pip install -r requirements.txt
```

3. `.env.example` 파일을 `.env`로 복사하고 Tistory 로그인 정보를 입력합니다:

```bash
cp .env.example .env
```

그리고 `.env` 파일을 열어 `TISTORY_USERNAME`과 `TISTORY_PASSWORD`를 입력하세요.

## 사용법

스크립트를 실행하려면 다음 명령어를 사용하세요:

```bash
python main.py
```

성공적으로 로그인되면 콘솔에 로그 메시지가 출력되고, 'screenshot.png' 파일에 최종 페이지의 스크린샷이 저장됩니다.

## 프로젝트 구조

- `main.py`: 메인 실행 파일
- `login.py`: Tistory 로그인 클래스 정의
- `logger.py`: 로깅 설정
- `.env`: 환경 변수 (로그인 정보) 저장
- `requirements.txt`: 필요한 Python 패키지 목록

## 주의사항

- `.env` 파일에는 민감한 정보가 포함되어 있으므로 절대로 공개 저장소에 업로드하지 마세요.
- 이 스크립트는 교육 목적으로만 사용해야 합니다. 웹사이트의 이용 약관을 준수하고 과도한 자동화로 서버에 부담을 주지 않도록 주의하세요.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 있습니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.