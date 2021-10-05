import numpy as np
import os
from hpc.create_config_params import create_global_config_args
from dotenv import load_dotenv

# Model parameters
sim_name = "tobrfv_monthly_revEstabEq"
start_run = 0
end_run = 10
# start_commodity = "0702"
# end_commodity = "120991"
commodity_list = ["0702", "120991", "070960"]
country_of_interest = "Mexico"
native_countries_list = ["Israel", "Jordan"]

# To keep one parameter static, pass it as a list e.g. alpha = [0.15]
start_years = list(range(2012, 2014))
alphas = [round(a, 2) for a in list(np.arange(0.25, 0.55, 0.1))]
lamdas = [round(l, 2) for l in list(np.arange(0.2, 3, 0.2))]

# Transmission lag type
transmission_lag_type = None
gamma_shape = 2
gamma_scale = 1
threshold_val = 16
scaled_min = 0.3
scaled_max = 0.8

season_dict = {
    "NH_season": [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
    ],
    "SH_season": [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
    ],
}

timestep = "monthly"

# Summary statistics
years_before_firstRecord = 10
years_after_firstRecord = 1
end_valid_year = 2020
sim_years = [2014, 2023]  # list(range(2006,2035))

load_dotenv(os.path.join(".env"))
project_loc = os.getenv("DATA_PATH")

create_global_config_args(
    project_loc,
    sim_name,
    start_run,
    end_run,
    commodity_list,
    country_of_interest,
    native_countries_list,
    start_years,
    alphas,
    lamdas,
    transmission_lag_type,
    gamma_shape,
    gamma_scale,
    threshold_val,
    scaled_min,
    scaled_max,
    season_dict,
    timestep,
    years_before_firstRecord,
    years_after_firstRecord,
    end_valid_year,
    sim_years,
)
