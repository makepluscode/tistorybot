#!/bin/bash

# 버전 설정
VERSION="126.0.6478.126"

# Chrome 다운로드 URL
CHROME_URL="https://storage.googleapis.com/chrome-for-testing-public/${VERSION}/linux64/chrome-linux64.zip"

# ChromeDriver 다운로드 URL
CHROMEDRIVER_URL="https://storage.googleapis.com/chrome-for-testing-public/${VERSION}/linux64/chromedriver-linux64.zip"

# 임시 디렉토리 생성
TEMP_DIR=$(mktemp -d)
cd $TEMP_DIR

echo "Downloading Google Chrome..."
wget $CHROME_URL -O chrome.zip
unzip chrome.zip

echo "Installing Google Chrome..."
sudo mkdir -p /opt/google/chrome
sudo mv chrome-linux64/* /opt/google/chrome/
sudo ln -sf /opt/google/chrome/chrome /usr/bin/google-chrome

echo "Downloading ChromeDriver..."
wget $CHROMEDRIVER_URL -O chromedriver.zip
unzip chromedriver.zip

echo "Installing ChromeDriver..."
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver

# 정리
cd ~
rm -rf $TEMP_DIR

echo "Installation completed."
echo "Google Chrome version:"
google-chrome --version
echo "ChromeDriver version:"
chromedriver --version

# 자동 업데이트 비활성화
echo "Disabling automatic updates..."
sudo sed -i 's/deb http/deb [arch=amd64] http/' /etc/apt/sources.list.d/google-chrome.list 2>/dev/null
sudo apt-mark hold google-chrome-stable

echo "Setup completed successfully."