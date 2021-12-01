import numpy as np
import os
from hpc.create_config_params import create_global_config_args
from dotenv import load_dotenv

# Model parameters
sim_name = "tobrfv_120991"
start_run = 0
end_run = 3
commodity_list = ["120991"]
country_of_interest = "MEX"
native_countries_list = ["Israel", "Jordan"]

# To keep one parameter static, pass it as a list e.g. alpha = [0.15]
start_years = list(range(2013, 2014))
alphas = [round(a, 2) for a in list(np.arange(0.25, 0.55, 0.1))]
betas = [round(b, 2) for b in list(np.arange(0.15, 0.50, 0.05))]
lamdas = [round(l, 2) for l in list(np.arange(0.2, 3, 0.2))]

# Transmission lag type
transmission_lag_type = None
gamma_shape = None
gamma_scale = None
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
data_path = "/share/rkmeente/cawalden/pops_global"
lamda_weights_path = (
    rf"{data_path}/inputs/" r"Tomato_HarvestedArea_Percent_VegetablesPrimary_full.csv"
)

# Summary statistics
years_before_firstRecord = 50
years_after_firstRecord = 0
end_valid_year = 2020
sim_years = [2014, 2020]  # list(range(2006,2035))

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
    betas,
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
    lamda_weights_path,
)
