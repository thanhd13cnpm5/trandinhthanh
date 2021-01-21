from datetime import datetime
import requests
import MySQLdb
import time
import schedule


def do_request():
    mydb = MySQLdb.connect("localhost", "root", "thanh2210", "nhanvien" )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT url_name FROM web")
    result = mycursor.fetchall()
    dem = 0
    for result1 in result:
        for result2 in result1:
            x = requests.get(result2)
            y = result2
            val = (result2,)
            sql = ("SELECT web_name FROM web WHERE url_name = %s")
            mycursor.execute(sql, val)
            result3 = mycursor.fetchone()
            duong_dan = str(y)
            thoigian_check = str(datetime.now())
            trang_thai = str(x.status_code)
            tup = (duong_dan, thoigian_check, trang_thai, result3)

            sql = "INSERT INTO web_status(url_name,time_check,status,web_name) VALUES(%s,%s,%s,%s)"

            mycursor.execute(sql, tup)
            mydb.commit()
            dem += mycursor.rowcount
        print(dem, "record is inserted")
    print("\nthe next send after delay time\n")

def main():
    tg = int(input("lập lịch thời gian gọi request: "))
    schedule.every(tg).seconds.do(do_request) #đặt lịch theo giây
    #schedule.every(tg).minutes.do(do_request)  #đặt lịch theo phút
    #schedule.every(tg).day.at("06:00").do(do_request)  #đặt lịch theo ngày
    while True:
        schedule.run_pending()
        time.sleep(1)

main()