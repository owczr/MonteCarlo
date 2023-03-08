# PI Number Estimation using Monte Carlo

![plot](https://github.com/owczr/MonteCarlo/blob/main/montecarlo.png?raw=true)

## To run experiment
### Create new conda environement from requirements.txt
```
conda create -n montecarlo requirements.txt;
conda activate montecarlo;
```
### Execute run.sh script
```
bash run.sh
```
### Or execute:
```
python main/main.py --points-count 1000
```
### See help for more options
```
python main/main.py --help
```

## Other information
<p>This experiment is conducted with according parameters:</p>

- Radius: 1
- X range: 0, 1
- Y range: 0, 1

<p>Other default values are:</p>

- Points count: 1000
- Random seed: 123
- First percentile: 25
- Second percentile: 75
- Save plot: False

<p>This program is part fo Computational Intelligence course, during 2023 summer semester on 3rd year of Data Engineering and Analysis on AGH UST</p>


