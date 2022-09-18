import openpyxl


class Excel(object):
    list_buffer = []

    def OpenExcel(self,file_name):
        """
        Функция открывает файл и записывает в буфер данные из файла
        :param file_name:
        :return:
        """
        wb = openpyxl.open(file_name)
        sheet = wb.active
        for row in sheet.iter_rows():
            cell_buffer = []
            for cell in row:
                cell_buffer.append(cell.value)
            self.list_buffer.append(cell_buffer)
        wb.close()


a = Excel()

a.OpenExcel("data.xlsx")
print(a.list_buffer)
