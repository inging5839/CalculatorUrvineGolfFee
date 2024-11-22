from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

def download(month, day_volume):
    ##### ----------------- 사용자 수정 칸 --------------------
    target_month = str(month)  # 목표하는 달을 두 자리 수로 입력해주세요 ex) 01 ,  05 ,  12  => # 아직 기능 완성 못함
    target_day_volume = day_volume
    # --------사용자 수정 칸 종료 ------------- 이하 내용 건들지 말 것 ------------------

    # 크롬 드라이버 경로 설정
    # chrome_path = 'chromedriver.exe'

    # 크롬 드라이버 실행 옵션 설정
    download_path = '/Users/geon/Desktop/Golf_Cost_Auto_System'

    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # 브라우저 창을 띄우지 않고 실행하려면 주석 해제
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(f'--download.default_directory={download_path}')
    chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_path})

    # 크롬 드라이버 실행
    driver = webdriver.Chrome(options=chrome_options)

    # 웹페이지로 이동
    url = 'https://olympus.aptner.com/OLYMPUS/home.do'  # 대상 웹페이지 주소로 변경
    driver.get(url)

    # 로그인 하기
    login_url = 'https://olympus.aptner.com/OLYMPUS//login.do?admin=Y'
    driver.get(login_url)

    # 로그인 정보 입력
    username = 'urvinehs'
    password = '1234'

    username_input = driver.find_element(By.XPATH, '//*[@id="ip_id"]')
    password_input = driver.find_element(By.XPATH, '//*[@id="ip_pw"]')

    username_input.send_keys(username)
    password_input.send_keys(password)

    login_button = driver.find_element(By.XPATH, '//*[@id="btn_login"]')
    login_button.click()
    time.sleep(1)

    # 룸 예약 탭으로 이동
    room_tap = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[2]/div[5]')
    room_tap.click()
    time.sleep(1)

    
    # 캘린더로 프레임 이동
    frame_element = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/iframe[1]')
    time.sleep(1)
    driver.switch_to.frame(frame_element)
    
    # 이전 달로 이동 
    previous_month = driver.find_element(By.XPATH, '//*[@id="calendar"]/div[1]/div[3]/button[1]')
    previous_month.click()
    time.sleep(1)

    # target_month의 값 -> 목표하는 월 캘린더로 이동
    # move_target_month = driver.find_element(By.XPATH, '//*[@id="calendar"]/div[1]/div[3]/button[1]')
    # move_target_month.click()
    # time.sleep(1)
    # 엑셀 파일명 날짜로 수정하기 위한 값들
    original_file_path = download_path + '/예약내역.xlsx'

    # 해당 월의 날짜 수만큼 반복시행
    for i in range(target_day_volume):  # range(해당 월 날짜 수 입력하기 Ex) 28, 29, 30, 31 값 중 하나만 입력가능
        # 날짜 탭 선택
        if i < 9:
            date_tap = driver.find_element(By.XPATH, f'//td[contains(@class, "fc-day-top") and contains(@data-date, "2024-{target_month}-0{i+1}")]')
        else:
            date_tap = driver.find_element(By.XPATH, f'//td[contains(@class, "fc-day-top") and contains(@data-date, "2024-{target_month}-{i+1}")]')
        date_tap.click()
        time.sleep(1)
        # 엑셀 다운 버튼 접근 -> 클릭 -> 다운로드 진행
        btn_excel = driver.find_element(By.XPATH, '//*[@id="btn_excel"]')
        btn_excel.click()
        time.sleep(1)
        if i < 9:
            new_path = os.path.join(os.path.dirname(original_file_path), f'2024-{target_month}-0{i+1}.xlsx')
        else:
            new_path = os.path.join(os.path.dirname(original_file_path), f'2024-{target_month}-{i+1}.xlsx')
        os.rename(original_file_path, new_path)
        time.sleep(1)

    # 브라우저 종료
    driver.quit()
