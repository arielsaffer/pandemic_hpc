import numpy as np
import os
from hpc.create_config_params import create_global_config_args
from dotenv import load_dotenv

load_dotenv(os.path.join(".env"))
project_loc = os.getenv("DATA_PATH")

# Save model outputs? (Keep = save all model files; Temp = write temporary model files, save only summary statistics)
model_files = "Temp"  # "Keep" or "Temp"

# Print out model run time steps (True recommended for HPC/large #'s of runs)
quiet_time = True  # True or False

# Model parameters
sim_name = "slf_grid"
start_run = 0
end_run = 80
commodity_list = ["6802"]
trade_type = "adjusted"  # "adjusted" or "agg"
country_of_interest = "USA"
native_countries_list = ["China", "Viet Nam"]

# To keep one parameter static, pass it as a list e.g. alpha = [0.15]
start_years = [2005, 2006, 2007]
alphas = [round(a, 2) for a in list(np.arange(0.4, 1, 0.05))]
betas = [0.5]
lamdas = [round(l, 2) for l in list(np.arange(0.7, 3, 0.05))]

# Lamda weights, if relevant
lamda_weights_path = None
# lamda_weights_path = (
#     rf"{project_loc}/inputs/Area_Percent.csv"
# )

# Transmission lag type
transmission_lag_type = "stochastic"
gamma_shape = 4
gamma_scale = 1
threshold_val = ""
scaled_min = 0.3
scaled_max = 0.8

season_dict = {
    "NH_season": ["09", "10", "11", "12", "01", "02", "03", "04",],
    "SH_season": ["04", "05", "06", "07", "08", "09", "10",],
}

timestep = "monthly"  # options: annual or monthly

# Summary statistics
years_before_firstRecord = 5
years_after_firstRecord = 0
end_valid_year = 2020
sim_years = [2014, 2020]  # list(range(2006,2035))

create_global_config_args(
    model_files,
    quiet_time,
    project_loc,
    sim_name,
    start_run,
    end_run,
    commodity_list,
    trade_type,
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
