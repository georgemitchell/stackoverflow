from pytz import country_timezones
from timezone_to_locale.language_codes import locale_by_country

locale_by_timezone = {}

country_by_timezone = {}
for code in country_timezones:
    for timezone in country_timezones[code]:
        assert timezone not in country_by_timezone
        country_by_timezone[timezone] = code

for timezone in country_by_timezone:
    country_code = country_by_timezone[timezone]
    if country_code not in locale_by_country:
        raise IndexError(f"Unable to find {country_code} in locale_by_country")
    else:
        languages = locale_by_country[country_code]["languages"]
        locale_by_timezone[timezone] = [language.strip() for language in languages.split(",")]

if __name__ == "__main__":
    timezone = "America/Chicago"
    while timezone != "":
        if timezone not in locale_by_timezone:
            raise IndexError(f"Unable to locate timezone: '{timezone}'")
        else:
            for i, language in enumerate(locale_by_timezone[timezone]):
                print("%d) %s" % (i + 1, language))
