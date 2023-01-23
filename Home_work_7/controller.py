import view
import process
import log
from datetime import datetime as dt


def button_click():
    data = str(dt.now()) + ': '
    rezhim = view.inp_mod()
    data = data + rezhim + ' = '
    if rezhim.lower() == 'импорт':
        sern = view.inp_import()
        data = data + sern + ' - '
        res_search = process.search(sern)
        # print(res_search)
        if isinstance(res_search, str):
            view.view_import_no()
            data = data + 'Not found'
        else:
            view.view_import(res_search)
            data = data + str(res_search)
    elif rezhim.lower() == 'экспорт':
        result = view.inp_export()
        data = data + str(result) + ' - '
        process.export(result)
        data = data + 'Succesfully added'
    log.logger(data)
            
        

    


    