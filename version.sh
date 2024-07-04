#!/bin/bash

# 함수: 버전 문자열을 숫자로 변환
version_to_number() {
    echo "$@" | awk -F. '{ printf("%d%03d%03d%03d\n", $1,$2,$3,$4); }'
}

# Chrome 버전 확인
CHROME_VERSION=$(google-chrome --version | awk '{print $NF}')
if [[ -z "$CHROME_VERSION" ]]; then
    echo "Error: Chrome 버전을 확인할 수 없습니다. Chrome이 설치되어 있는지 확인하세요."
    exit 1
fi

echo "Chrome 버전: $CHROME_VERSION"
echo "참고: Google Chrome for Testing 버전을 사용 중입니다."

# ChromeDriver 버전 확인
CHROMEDRIVER_VERSION=$(chromedriver --version 2>/dev/null | awk '/ChromeDriver/ {print $2}')
if [[ -z "$CHROMEDRIVER_VERSION" ]]; then
    echo "Error: ChromeDriver 버전을 확인할 수 없습니다. ChromeDriver가 설치되어 있는지 확인하세요."
    exit 1
fi
echo "ChromeDriver 버전: $CHROMEDRIVER_VERSION"

# 버전 숫자로 변환
CHROME_VERSION_NUM=$(version_to_number $CHROME_VERSION)
CHROMEDRIVER_VERSION_NUM=$(version_to_number $CHROMEDRIVER_VERSION)

# 버전 비교
if [ $CHROME_VERSION_NUM -eq $CHROMEDRIVER_VERSION_NUM ]; then
    echo "버전이 정확히 일치합니다. Chrome for Testing과 ChromeDriver가 완벽히 호환됩니다."
elif [ $CHROME_VERSION_NUM -gt $CHROMEDRIVER_VERSION_NUM ]; then
    echo "Chrome for Testing 버전이 ChromeDriver 버전보다 높습니다."
    echo "ChromeDriver를 업데이트하는 것을 강력히 권장합니다."
elif [ $CHROME_VERSION_NUM -lt $CHROMEDRIVER_VERSION_NUM ]; then
    echo "ChromeDriver 버전이 Chrome for Testing 버전보다 높습니다."
    echo "Chrome for Testing을 업데이트하거나, ChromeDriver를 다운그레이드하는 것을 고려해보세요."
fi

# 주 버전 비교
CHROME_MAJOR_VERSION=$(echo $CHROME_VERSION | cut -d. -f1)
CHROMEDRIVER_MAJOR_VERSION=$(echo $CHROMEDRIVER_VERSION | cut -d. -f1)

if [ "$CHROME_MAJOR_VERSION" != "$CHROMEDRIVER_MAJOR_VERSION" ]; then
    echo "주의: 주 버전 번호가 일치하지 않습니다."
    echo "Chrome for Testing 주 버전: $CHROME_MAJOR_VERSION"
    echo "ChromeDriver 주 버전: $CHROMEDRIVER_MAJOR_VERSION"
    echo "이는 호환성 문제를 일으킬 수 있습니다."
fi

# ChromeDriver 업데이트 제안
if [ $CHROME_VERSION_NUM -gt $CHROMEDRIVER_VERSION_NUM ]; then
    echo "ChromeDriver 업데이트 방법:"
    echo "1. https://googlechromelabs.github.io/chrome-for-testing/ 에서 Chrome for Testing 버전에 맞는 ChromeDriver를 다운로드하세요."
    echo "2. 다운로드한 파일을 압축 해제하고 기존 ChromeDriver를 대체하세요."
    echo "3. 권한을 설정하세요: sudo chmod +x /path/to/chromedriver"
    echo "4. 이 스크립트를 다시 실행하여 버전을 확인하세요."
fi