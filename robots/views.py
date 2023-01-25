from datetime import date, timedelta
from itertools import groupby
from openpyxl import Workbook

from django.db.models import Count
from django.http import HttpResponse

from .models import Robots


def weekly_report(request):
    today = date.today()
    last_week = today - timedelta(days=7)

    # Получает отфильтрованный queryset за последнюю неделю,
    # с полями model и version, а также через аннотацию добавляем поле count
    robot_production = (
        Robots.objects.filter(created__range=[last_week, today])
        .values('model', 'version').annotate(count=Count('id')))

    wb = Workbook()
    #  используем groupby для группировки списка robot_production по модели
    for model, group in groupby(robot_production, key=lambda x: x['model']):
        sheet = wb.create_sheet(title=model)
        sheet.append(['Модель', 'Версия', 'Количество за неделю'])
        for robot in group:
            sheet.append([robot['model'], robot['version'], robot['count']])

    # Указываем тим содержимого ответа
    response = HttpResponse(
        content_type='application/vnd.openxmlformats'
                     '-officedocument.spreadsheetml.sheet')
    # Определяем в заголовке, что при переходе на эндпоинт,
    # нужно сохранить файл с отчётом
    response['Content-Disposition'] = ('attachment;'
                                       'filename=robot_production_report.xlsx')
    wb.save(response)
    return response
