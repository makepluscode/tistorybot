from logger import setup_logger
from login import TistoryLogin
from bloginfo import get_blog_info

def main():
    logger = setup_logger()
    tistory = TistoryLogin(logger)
    driver = tistory.login()

    if driver:
        try:
            blogs_info = get_blog_info(driver, logger)
            if blogs_info:
                logger.info("블로그 정보 수집 완료")
                logger.info(f"수집된 블로그 수: {len(blogs_info)}")
            else:
                logger.warning("수집된 블로그 정보가 없습니다.")
        except Exception as e:
            logger.error(f"블로그 정보 수집 중 오류 발생: {e}")
        finally:
            driver.quit()
            logger.info("브라우저 종료됨")
    else:
        logger.error("로그인 실패")

if __name__ == "__main__":
    main()