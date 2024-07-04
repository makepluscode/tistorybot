import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TistoryLogin:
    def __init__(self, logger):
        load_dotenv()  # .env 파일 로드
        self.username = os.getenv('TISTORY_USERNAME')
        self.password = os.getenv('TISTORY_PASSWORD')
        self.logger = logger
        self.driver = None

    def setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    def login(self):
        if not self.username or not self.password:
            self.logger.error("TISTORY_USERNAME과 TISTORY_PASSWORD를 .env 파일에 설정해주세요.")
            return

        try:
            self.setup_driver()
            self.driver.get('https://www.tistory.com/auth/login')
            self.logger.info(f"페이지 로드 완료. 현재 URL: {self.driver.current_url}")

            self.click_kakao_login()
            self.enter_credentials()
            self.click_submit()
            self.verify_login()

            self.logger.info("로그인 성공!")
        except Exception as e:
            self.logger.error(f"로그인 중 오류 발생: {e}")
        finally:
            self.cleanup()

    def click_kakao_login(self):
        login_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'link_kakao_id'))
        )
        login_button.click()
        self.logger.info("카카오 계정으로 로그인 버튼 클릭 완료")

    def enter_credentials(self):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'loginId'))
        )
        email_field.send_keys(self.username)
        self.logger.info("이메일 입력 완료")

        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_field.send_keys(self.password)
        self.logger.info("비밀번호 입력 완료")

    def click_submit(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'submit'))
        )
        submit_button.click()
        self.logger.info("로그인 버튼 클릭 완료")

    def verify_login(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.gnb_icon.gnb_my'))
        )

    def cleanup(self):
        if self.driver:
            self.logger.info(f"최종 페이지 URL: {self.driver.current_url}")
            self.driver.save_screenshot('screenshot.png')
            self.driver.quit()
            self.logger.info("브라우저가 종료되었습니다.")