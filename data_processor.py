from validators.validate_gender import ValidateGender as vg
from validators.validate_bmi import ValidateBmi as vb
from validators.validate_date import ValidateDate as vd
from validators.validate_empid import ValidateEmpid as ve


class DataProcessor(object):

    @staticmethod
    def send_to_validate(dict_root):
        print(dict_root)
        rows = 0
        values = 0
        for k, v in dict_root.items():
            values += 1
            if k != '':
                print("EMPID")
                result = ve.is_valid(k)
                print(result)
                for kv in v.keys():
                    if kv == 'gender':
                        print("GENDER")
                        result = vg.is_valid(vg, dict_root[k][kv])
                        print(result)
                    if kv == 'bmi':
                        print("BMI")
                        result = vb.is_valid(vb, dict_root[k][kv])
                        print(result)
                    if kv == 'birthday':
                        print("BIRTHDAY")
                        print(dict_root[k][kv])
                        i = vd()
                        result = i.is_valid(dict_root[k][kv])
                        print("result" + str(result))
        print("number of values:")
        print(values)
        return dict_root
