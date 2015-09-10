from pytz import country_timezones
from language_codes import locale_by_country
import re

locale_by_timezone = {}

# Get a list of all the timezones by country
country_by_timezone = {}
for code in country_timezones:
    for timezone in country_timezones[code]:
        # check that each timezone only belongs to one country
        assert(timezone not in country_by_timezone)
        country_by_timezone[timezone] = code

for timezone in country_by_timezone:
    country_code = country_by_timezone[timezone]
    if country_code not in locale_by_country:
        print "Unable to find %s in locale_by_country" % country_code
    else:
        languages = locale_by_country[country_code]["languages"]
        locale_by_timezone[timezone] = [l.strip() for l in languages.split(",")]

if __name__ == "__main__":
    print "Enter a timezone and get a list of possible languages"
    timezone = "America/Chicago"
    print "Example: '%s':" % timezone
    while timezone != "":
        if timezone not in locale_by_timezone:
            print "Unable to locate timezone: '%s'" % timezone
        else:
            for i, language in enumerate(locale_by_timezone[timezone]):
                print "%d) %s" % (i+1, language)
        timezone = raw_input("Timezone: ")
