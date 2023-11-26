import mysql.connector


def get_data_from_table_as_string(table_name):
    # Tạo kết nối đến MySQL
    cnx = mysql.connector.connect(user='root', password='@Vtb28042002',
                                  host='localhost',
                                  database='dncn')

    # Tạo một đối tượng cursor
    cursor = cnx.cursor()

    # Thực hiện truy vấn SQL
    query = f"SELECT * FROM {table_name} ORDER BY Timee DESC"
    cursor.execute(query)

    # Lấy tất cả các dòng từ kết quả truy vấn
    rows = cursor.fetchmany(2)

    # Đóng kết nối
    cnx.close()

    # Chuyển đổi dữ liệu thành danh sách các bộ giá trị (time, temp)
    data_as_list = list(rows)
    B=1
    return data_as_list
get_data_from_table_as_string('nhietdo')