# EnergyUCB-Bandit
The official EnergyUCB implementation for the paper "Online Energy Optimization in GPUs: A Multi-Armed Bandit Approach".

## Contributions
• Problem Formulation: We formally define the new problem of online GPU energy optimization and formulate it as a multi-armed bandit framework, which inherently addresses the exploration \& exploitation dilemma across frequencies in the online setting. <br/>
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

