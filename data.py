from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.clock import Clock
import mysql.connector

global table


class MainApp(MDApp):
    def build(self):
        screen = Screen()

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

            return data_as_list

        def update_data(*args):
            # Lấy dữ liệu từ bảng 'nhietdo'
            data = get_data_from_table_as_string('nhietdo')
            global old_data
            old_data = None

            if data != old_data:
                time1,temp1 = data[0]
                time2,temp2 = data[1]
                table.add_row((time1,temp1))
                table.add_row((time2,temp2))


                if len(table.row_data) > 2:
                    table.row_data.pop(0)
                    table.row_data.pop(0)
                old_data = data
            else:
                pass
        table = MDDataTable(
            size_hint=(0.4, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            column_data=[
                ("Thời Gian", dp(30)),
                ('Nhiệt Độ', dp(30)),
            ],
            row_data=[

            ]

        )

        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_paletee = 'Light'
        screen.add_widget(table)
        Clock.schedule_interval(update_data, 0.2 * 60)

        return screen


MainApp().run()
