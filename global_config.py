import numpy as np
import os
from hpc.create_config_params import create_global_config_args
from dotenv import load_dotenv

# Save model outputs? (Keep = save all model files; Temp = write temporary model files, save only summary statistics)
model_files = "Temp"  # "Keep" or "Temp"

# Print out model run time steps (True recommended for HPC/large #'s of runs)
quiet_time = True  # True or False

# Model parameters
sim_name = "mln_eqn_test"
start_run = 0
end_run = 5
commodity_list = ["100510"]
country_of_interest = "KEN"
native_countries_list = [
    "Peru",
    "Argentina",
    "Mexico",
    "Thailand",
    "Colombia",
    "United States",
]

# To keep one parameter static, pass it as a list e.g. alpha = [0.15]
start_years = list(range(2000, 2010))
alphas = [round(a, 2) for a in list(np.arange(0.05, 1, 0.1))]
betas = [0.5]
lamdas = [round(l, 2) for l in list(np.arange(0.05, 1, 0.1))]

# Lamda weights, if relevant
lamda_weights_path = None
# lamda_weights_path = (
#     rf"{data_path}/inputs/Area_Percent.csv"
# )

# Transmission lag type
transmission_lag_type = "stochastic"
gamma_shape = 1
gamma_scale = 0.5
threshold_val = ""
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

timestep = "annual" # options: annual or monthly

# Summary statistics
years_before_firstRecord = 50
years_after_firstRecord = 0
end_valid_year = 2020
sim_years = [2014, 2020]  # list(range(2006,2035))

load_dotenv(os.path.join(".env"))
project_loc = os.getenv("DATA_PATH")

create_global_config_args(
    model_files,
    quiet_time,
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
