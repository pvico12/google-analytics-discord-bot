import os

cwd = os.getcwd()

KEY_FILE_LOCATION = cwd + '/' + os.getenv('GOOGLE_ANALYTICS_API_KEY_JSON_FILE')
PROPERTY_ID = '<your-property-id>'

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Filter,
    FilterExpression,
    Metric,
    RunReportRequest,
)

googleAnayticsClient = BetaAnalyticsDataClient.from_service_account_json(KEY_FILE_LOCATION)


"""Fetches a report on page views."""
def getPageViews(startDate="2023-03-31", endDate="today"):
    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[Dimension(name="pagePath")],
        dimension_filter=FilterExpression(
            filter=Filter(
                field_name="pagePath",
                in_list_filter=Filter.InListFilter(
                    values=[
                        "/" # add more page paths to filter
                    ]
                ),
            )
        ),
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date=startDate, end_date=endDate)]
    )
    response = googleAnayticsClient.run_report(request)

    outputArray = []
    outputArray.append(["Page", "User Visits"])

    for row in response.rows:
        outputArray.append([
            row.dimension_values[0].value,
            row.metric_values[0].value
            ])
      
    return outputArray


"""Fetches a report on viewer location."""
def getLocations(locationType="country", startDate="2023-03-31", endDate="today"):
    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[Dimension(name=locationType)],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date=startDate, end_date=endDate)]
    )
    response = googleAnayticsClient.run_report(request)

    outputArray = []
    outputArray.append(["Site", "Total User Visits"])

    for row in response.rows:
        outputArray.append([
            row.dimension_values[0].value,
            row.metric_values[0].value
            ])
      
    return outputArray

