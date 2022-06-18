for i in range(i,51):
    with open(str(i) + "주차.txt," "w",incoding ="utf8") as report_file:
        report_file.write("-{0} 주차 주간보고-".formmat(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약: ")
        report_file.write()