from pydnevnikruapi.dnevnik import dnevnik

login = ""
password = ""

dn = dnevnik.DiaryAPI(login=login, password=password)


print(dn.get_final_group_marks_by_subject(group_id=1831168584419618567, subject_id=1192159007994913))
