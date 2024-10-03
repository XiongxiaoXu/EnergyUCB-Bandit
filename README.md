# EnergyUCB-Bandit
The official EnergyUCB implementation for the paper "Online Energy Optimization in GPUs: A Multi-Armed Bandit Approach".

## EnergyUCB Algorithm
<img width="488" alt="image" src="https://github.com/user-attachments/assets/6f6f2d35-d841-47cf-8ad5-ee53d9ad436e">

## Architcture of an Aurora Node
<img width="472" alt="image" src="https://github.com/user-attachments/assets/7b904c5f-2337-47c5-870a-54754e154ec5">

## Contributions
• Problem Formulation: We formally define the **new problem of online GPU energy optimization** and formulate it as a **multi-armed bandit framework**, which inherently addresses the exploration \& exploitation dilemma across frequencies in the online setting. <br/>
• Algorithm: We propose a novel meta-learning approach to learn to transfer node representations from self-supervised tasks to assist supervised tasks with little labeled anomalies. <br/>
• Evaluation: We conduct extensive experiments on six real-world datasets with synthetically injected anomalies and organic anomalies. The experimental results demonstrate the effectiveness of the proposed approach MetaGAD for graph anomaly detection. <br/>

## Getting Started
### Environment
* python             3.10.14
* numpy              1.26.4
* pandas             2.2.2

### Run
Run the Energyucb.py with the following command in a terminal:

`python main.py --app app`

Replace app wirt the name of HPC application.

For exmaple, if we want to optimize emnergy in GPUs for the HPC application 532.sph_exa_t, the command should be as follows:

`python main.py --app 532.sph_exa_t`

## Experimental Results
### Energy Consumption
<img width="1410" alt="image" src="https://github.com/user-attachments/assets/8301301b-15a0-4d9a-9f6a-51b4d3aa3258">

### Regret
<img width="702" alt="image" src="https://github.com/user-attachments/assets/62588fd0-e058-4711-8920-cb302435f09b">

### Execution time analysis
<img width="735" alt="image" src="https://github.com/user-attachments/assets/98fa2ee1-7cfc-4fed-8675-1af961d20939">



