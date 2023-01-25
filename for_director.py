from django.http import FileResponse
import pandas as pd
from robots.models import Robots

def export_to_excel(request):
    # Retrive data from your database
    robots = Robots.objects.all()
    # Create a pandas dataframe from the queryset
    df = pd.DataFrame.from_records(robots.values())
    # Create a excel file using pandas
    file = df.to_excel('robots.xlsx', index=False)
    # Create a `FileResponse` object with the excel file
    response = FileResponse(file, as_attachment=True)
    response['Content-Disposition'] = 'attachment; filename=robots.xlsx'
    return response