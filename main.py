from pydnevnikruapi.dnevnik import dnevnik

login = "daniiarmendygaliev"
password = ""

dn = dnevnik.DiaryAPI(login=login, password=password)
пуцпцы

print(dn.get_final_group_marks_by_subject(group_id=1831168584419618567, subject_id=1192159007994913))
