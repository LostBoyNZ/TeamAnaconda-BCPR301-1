from validators.validate_gender import ValidateGender as vg
from validators.validate_bmi import ValidateBmi as vb
from validators.validate_date import ValidateDate as vd
from validators.validate_empid import ValidateEmpid as ve
from validators.validate_age import ValidateAge as va
from validators.validate_salary import ValidateSalary as vs
from validators.validate_sales import ValidateSales as vsa


class DataProcessor(object):

    @staticmethod
    def send_to_validate(dict_root, switch, dup_keys):
        valid_rows = 0
        invalid_rows = 0
        for k, v in dict_root.items():
            valid = 0
            length_of_values = len(v)
            # if k != '':
            result = ve.is_valid(k)
            if result[1]:
                valid += 1
            for kv in v.keys():
                if kv == 'gender':
                    result = vg.is_valid(dict_root[k][kv])
                    if result[1]:
                        dict_root[k][kv] = result[0]
                        valid += 1
                if kv == 'bmi':
                    result = vb.is_valid(dict_root[k][kv])
                    if result[1]:
                        dict_root[k][kv] = result[0]
                        valid += 1
                if kv == 'birthday':
                    i = vd()
                    result = i.is_valid(dict_root[k][kv])
                    if result[1]:
                        dict_root[k][kv] = result[0]
                        valid += 1
                if kv == 'age':
                    i = va()
                    result = i.is_valid(dict_root[k][kv])
                    if result[1]:
                        dict_root[k][kv] = result[0]
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
                        dict_root[k][kv] = result[0]
                        valid += 1
            if valid == length_of_values:
                dict_root[k]['valid'] = '1'
                valid_rows += 1
            else:
                invalid_rows += 1
        if switch.upper() == 'D':
            print("{0} Rows Of Valid Data".format(valid_rows))
            print("{0} Rows Of Invalid Data".format(invalid_rows))
            print("{0} Duplicate ID Key(s) appended to log".format(dup_keys))
        return dict_root

    @staticmethod
    def validate_key(key_to_validate):
        """
        >>> DataProcessor.validate_key('a001')
        'A001'

        >>> DataProcessor.validate_key('a123')
        'A123'

        >>> DataProcessor.validate_key('abc5')
        'Abc5'
        """
        result = ve.is_valid(key_to_validate)
        return result[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
