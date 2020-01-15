from ..models import State, Chamber, District, simple_numbered_districts

ND = State(
    name="North Dakota",
    abbr="ND",
    capital="Bismarck",
    capital_tz="America/North_Dakota/Center",
    fips="38",
    unicameral=False,
    legislature_name="North Dakota Legislative Assembly",
    division_id="ocd-division/country:us/state:nd",
    jurisdiction_id="ocd-jurisdiction/country:us/state:nd/government",
    url="http://www.legis.nd.gov/",
    lower=Chamber(
        chamber_type="lower",
        name="House",
        num_seats=94,
        title="Representative",
        districts=[
            District("1", "lower", 2),
            District("2", "lower", 2),
            District("3", "lower", 2),
            District("4", "lower", 2),
            District("5", "lower", 2),
            District("6", "lower", 2),
            District("7", "lower", 2),
            District("8", "lower", 2),
            District("9", "lower", 2),
            District("10", "lower", 2),
            District("11", "lower", 2),
            District("12", "lower", 2),
            District("13", "lower", 2),
            District("14", "lower", 2),
            District("15", "lower", 2),
            District("16", "lower", 2),
            District("17", "lower", 2),
            District("18", "lower", 2),
            District("19", "lower", 2),
            District("20", "lower", 2),
            District("21", "lower", 2),
            District("22", "lower", 2),
            District("23", "lower", 2),
            District("24", "lower", 2),
            District("25", "lower", 2),
            District("26", "lower", 2),
            District("27", "lower", 2),
            District("28", "lower", 2),
            District("29", "lower", 2),
            District("30", "lower", 2),
            District("31", "lower", 2),
            District("32", "lower", 2),
            District("33", "lower", 2),
            District("34", "lower", 2),
            District("35", "lower", 2),
            District("36", "lower", 2),
            District("37", "lower", 2),
            District("38", "lower", 2),
            District("39", "lower", 2),
            District("40", "lower", 2),
            District("41", "lower", 2),
            District("42", "lower", 2),
            District("43", "lower", 2),
            District("44", "lower", 2),
            District("45", "lower", 2),
            District("46", "lower", 2),
            District("47", "lower", 2),
        ],
    ),
    upper=Chamber(
        chamber_type="upper",
        name="Senate",
        num_seats=47,
        title="Senator",
        districts=simple_numbered_districts("upper", 47),
    ),
)
