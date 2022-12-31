from map.models import *
AbstractTile.objects.all().delete()
Problem(row=4, column=5, ejudge_short_name="00", name="Вещественное число", statement_file_name="00.pdf", automatic_open_time=0, solved_award=100, wrong_penalty=5).save()
Problem(row=5, column=5, ejudge_short_name="01", name="Смайлик", statement_file_name="01.pdf", automatic_open_time=40, solved_award=300, wrong_penalty=15).save()
Problem(row=5, column=6, ejudge_short_name="02", name="Время", statement_file_name="02.pdf", automatic_open_time=40, solved_award=500, wrong_penalty=25).save()
Problem(row=1, column=4, ejudge_short_name="03", name="Текст", statement_file_name="03.pdf", automatic_open_time=80, solved_award=1200, wrong_penalty=60).save()
Problem(row=0, column=4, ejudge_short_name="04", name="Друзья Деда Мороза", statement_file_name="04.pdf", automatic_open_time=120, solved_award=2000, wrong_penalty=100).save()
