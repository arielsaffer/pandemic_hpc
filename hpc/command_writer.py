import itertools
import json

# Name the script to be run
model_script = "model_run_args.py"

with open("config.json") as json_file:
    config = json.load(json_file)
start_years = config["start_years"]
alphas = config["alphas"]
lamdas = config["lamdas"]

param_list = [alphas, lamdas, start_years]
param_sets = list(itertools.product(*param_list))

# Full run
start_run = config["start_run"]
end_run = config["end_run"]

# Write to a text file

file1 = open("commands.txt", "w")
for params in param_sets:
    output = (
        " ".join(
            [
                "python",
                model_script,
                str(params[0]),
                str(params[1]),
                str(params[2]),
                str(start_run),
                str(end_run),
            ]
        )
        + "\n"
    )
    file1.write(output)
file1.close()
