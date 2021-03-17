from BeerMile import BeerMile

# Sasha sasa123
# Main.py bonta2000@mail.ru 9yG^VVSu+T3=jXw


if __name__ == "__main__":
    beer_mile = BeerMile("Sasha", "sasa123")
    beer_mile.login()
    beer_mile.getPage()
    beer_mile.getTop1000()

    # for rec in beer_mile.records:
    #     print(rec.record_position,
    #           " | ", rec.records_name,
    #           " | ", rec.records_time,
    #           " | ", rec.records_year,
    #           " | ", rec.records_beer, "\n")
