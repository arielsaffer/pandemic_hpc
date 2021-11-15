import itertools
import json

def write_commands(model_files, params, start_run, end_run):
    # Name the script to be run
    if model_files == "Temp":
        script = "./hpc/wrapper_script.csh"
    else: 
        script = "python model_run_args.py"
    output = (
        " ".join(
            [
                script,
                str(params[0]),
                str(params[1]),
                str(params[2]),
                str(start_run),
                str(end_run),
            ]
        )
        + "\n"
    )
    return output 


if __name__ == "__main__":

    with open("config.json") as json_file:
        config = json.load(json_file)
    start_years = config["start_years"]
    alphas = config["alphas"]
    lamdas = config["lamdas"]
    model_files = config["model_files"]

    param_list = [alphas, lamdas, start_years]
    param_sets = list(itertools.product(*param_list))

    # Full run
    start_run = config["start_run"]
    end_run = config["end_run"]

    file1 = open("commands.txt", "w")
    # Write to a text file    
    for params in param_sets:
        file1.write(write_commands(model_files, params, start_run, end_run))

    file1.close()

