import Calculator_time_fee
import File_Resave
import Golf_Cost_Auto_Download
import Refactor_To_Hand_In
import apply_style
import gather_data

target_month = '10'  # 목표하는 달을 두 자리 수로 입력해주세요 ex) 01 ,  05 ,  12  => # 아직 기능 완성 못함
target_day_volume = 31
#Calculator_time_fee 에서 공유일과 첫째 토요일, 첫째 일요일 날짜를 설정해주세요.
Golf_Cost_Auto_Download.download(target_month, target_day_volume)
File_Resave.file_resave(target_month, target_day_volume)

gather_data.gather_data()
apply_style.apply_style(Calculator_time_fee.calculator_time_fee())
Refactor_To_Hand_In.refactor(target_month)