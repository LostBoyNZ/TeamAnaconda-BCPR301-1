from validators.validate_gender import ValidateGender as vg
from validators.validate_bmi import ValidateBmi as vb
from validators.validate_date import ValidateDate as vd
from validators.validate_empid import ValidateEmpid as ve
from validators.validate_age import ValidateAge as va
from validators.validate_salary import ValidateSalary as vs
from validators.validate_sales import ValidateSales as vsa



class DataProcessor(object):

    @staticmethod
    def send_to_validate(dict_root):
        valid_rows = 0
        invalid_rows = 0
        for k, v in dict_root.items():
            valid = 0
            length_of_values = len(v)
            if k != '':
                result = ve.is_valid(k)
                if result:
                    valid += 1
                for kv in v.keys():
                    if kv == 'gender':
                        result = vg.is_valid(vg, dict_root[k][kv])
                        if result[1]:
                            valid += 1
                    if kv == 'bmi':
                        result = vb.is_valid(vb, dict_root[k][kv])
                        if result[1]:
                            valid += 1
                    if kv == 'birthday':
                        i = vd()
                        result = i.is_valid(dict_root[k][kv])
                        if result[1]:
                            valid += 1
                    if kv == 'age':
                        i = va()
                        result = i.is_valid(dict_root[k][kv])
                        if result[1]:
                            valid += 1
                    if kv == 'salary':
                        i = vs()
                        result = i.is_valid(dict_root[k][kv])
                        if result[1]:
                            valid += 1
                    if kv == 'sales':
                        i = vsa()
                        result = i.is_valid(dict_root[k][kv])
                        if result[1]:
                            valid += 1
                if valid == length_of_values:
                    dict_root[k]['valid'] = '1'
                    valid_rows += 1
                else:
                    invalid_rows += 1
        print("{0} Rows Of Valid Data".format(valid_rows))
        print("{0} Rows Of Invalid Data".format(invalid_rows))
        return dict_root