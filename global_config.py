import numpy as np
import os
from hpc.create_config_params import create_global_config_args
from dotenv import load_dotenv

# Model parameters
sim_name = "slf_start_year"
start_run = 0
end_run = 50
start_commodity = 6801
end_commodity = 6804
country_of_interest = "USA"
native_countries_list = ["China", "Viet Nam"]

# To keep one parameter static, pass it as a list e.g. alpha = [0.15]
start_years = list(range(2000, 2010))
alphas = [round(a, 2) for a in list(np.arange(0.15, 0.36, 0.05))]
lamdas = [round(l, 2) for l in list(np.arange(1.0, 4.1, 0.05))]

# Transmission lag type
transmission_lag_type = "stochastic"
gamma_shape = 4
gamma_scale = 1
threshold_val = 16
scaled_min = 0.3
scaled_max = 0.8

season_dict = {
    "NH_season": ["09", "10", "11", "12", "01", "02", "03", "04"],
    "SH_season": ["04", "05", "06", "07", "08", "09", "10"],
}

# Summary statistics
years_before_firstRecord = 5
years_after_firstRecord = 1
end_valid_year = 2014
sim_years = [2014, 2020]  # list(range(2006,2035))

load_dotenv(os.path.join(".env"))
project_loc = os.getenv("DATA_PATH")

create_global_config_args(
    project_loc,
    sim_name,
    start_run,
    end_run,
    start_commodity,
    end_commodity,
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
    years_before_firstRecord,
    years_after_firstRecord,
    end_valid_year,
    sim_years,
)
