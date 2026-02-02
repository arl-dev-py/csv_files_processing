from typing import List, Dict, Any

def generate_average_gdp_report(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    country_to_gdps = {}
    for element in data:
        country = element['country']
        gdp = float(element['gdp'])

        if country not in country_to_gdps:
            country_to_gdps[country] = []

        country_to_gdps[country].append(gdp)

    result = []
    for country, gdps in country_to_gdps.items():
        avg_gdp = sum(gdps) / len(gdps)
        result.append({"country": country, "avg_gdp": avg_gdp})

    result.sort(key=lambda x: x["avg_gdp"], reverse=True)
    return result

