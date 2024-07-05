from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BlogInfoCollector:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def wait_for_element(self, by, value, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            self.logger.error(f"Element not found: {value}")
            return None

    def click_profile_link(self):
        profile_link = self.wait_for_element(By.CSS_SELECTOR, 'a.link_profile')
        if profile_link:
            self.logger.info("프로필 링크 발견.")
            profile_link.click()
            self.logger.info("프로필 링크 클릭 완료.")
            return True
        return False

    def get_blog_list(self):
        blog_list = self.wait_for_element(By.CLASS_NAME, 'wrap_list')
        if blog_list:
            self.logger.info("블로그 리스트가 나타났습니다.")
            return blog_list
        return None

    def extract_blog_info(self, blog_list):
        blogs_info = {}
        blog_links = blog_list.find_elements(By.CSS_SELECTOR, 'a.txt_id')
        for link in blog_links:
            blog_name = link.text
            blog_url = link.get_attribute('href').rstrip('/')
            blogs_info[blog_name] = {'url': blog_url}
        return blogs_info

    def collect_blog_info(self):
        try:
            if not self.click_profile_link():
                return {}

            blog_list = self.get_blog_list()
            if not blog_list:
                return {}

            blogs_info = self.extract_blog_info(blog_list)

            self.log_collected_info(blogs_info)
            return blogs_info

        except Exception as e:
            self.logger.error(f"블로그 정보 수집 중 오류 발생: {e}")
            return {}

    def log_collected_info(self, blogs_info):
        self.logger.info("수집된 블로그 정보:")
        for name, info in blogs_info.items():
            self.logger.info(f"블로그명: {name}, URL: {info['url']}")

def get_blog_info(driver, logger):
    collector = BlogInfoCollector(driver, logger)
    return collector.collect_blog_info()