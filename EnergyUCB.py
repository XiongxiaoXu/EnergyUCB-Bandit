import numpy as np
import os
import pickle
import math
import argparse
import random

class UCBArm:
    def __init__(self, arm_id, alpha):
        self.arm_id = arm_id
        self.count = 0
        self.avg_reward = 0
        self.alpha = alpha

    def get_value(self, t):
        return self.avg_reward + self.alpha * math.sqrt(math.log(t)/(self.count))

    def update(self, reward):
        self.count = self.count + 1
        self.avg_reward = (self.avg_reward * (self.count - 1) + reward)/self.count

def get_mu(simulator):
    mu_list = []
    for i in range(9):
        freq = int(str(i+8) + '00000000')
        cur_simulator = simulator[freq]
        avg1, std1 = cur_simulator.loc['avg', 'GPU_ENERGY_PER'], cur_simulator.loc['std', 'GPU_ENERGY_PER']
        avg2, std2 = cur_simulator.loc['avg', 'Ratio1'], cur_simulator.loc['std', 'Ratio1']
        mu_list.append(-avg1*avg2)

    return mu_list

def get_reward_energy(freq, simulator):
    simulator = simulator[freq]
    simulated_value_list = []
    for col in ['GPU_ENERGY_PER', 'Ratio1', 'Ratio2']:
        avg, std = simulator.loc['avg',col], simulator.loc['std',col]
        simulated_value = np.random.normal(avg, std)
        while simulated_value<=0:
            simulated_value = np.random.normal(avg, std)
        simulated_value_list.append(simulated_value)
    energy, r1, r2 = simulated_value_list[0], simulated_value_list[1], simulated_value_list[2], 

    reward = -(energy*r1)

    return reward, energy

parser = argparse.ArgumentParser(description="Process Data")
parser.add_argument('--seed', type=int, default=0)
parser.add_argument('--C', type=int, default=4)
parser.add_argument('--app', type=str, choices=['505.lbm_t', '518.tealeaf_t', '519.clvleaf_t', '521.miniswp_t', '528.pot3d_t', '532.sph_exa_t', '535.weather_t'])

args = parser.parse_args()

seed = args.seed
random.seed(seed)
np.random.seed(seed)

app = args.app
path = os.path.join(app, 'trace.pkl')
with open(path, 'rb') as f:
    trace_dic = pickle.load(f)
path = os.path.join(app, 'simulator.pkl')
with open(path, 'rb') as f:
    simulator = pickle.load(f)
path = os.path.join(app, 'app_time.pkl')
with open(path, 'rb') as f:
    app_time_dic = pickle.load(f)
path = os.path.join(app, 'gpu_energy.pkl')
with open(path, 'rb') as f:
    gpu_energy_dic = pickle.load(f)

mu_list = get_mu(simulator)
mu_star = max(mu_list)
mu_star_index = mu_list.index(mu_star)

iterations = 10
K = len(simulator)
T = 100000
C = 4 # pure explorastion cycles
alpha = 1 # weight of exploration
time_interval = 10 # ms
total_energy = np.zeros((iterations))
finish_time = np.zeros((iterations))
Regret = np.zeros((iterations, T))

t_min = T
for iteration in range(iterations):
    #---------------EnergyUCB---------------
    rest_task = 1
    regret = 0
    accumed_energy = 0
    arm_list = []
    for i in range(K):
        arm_list.append(UCBArm(i, alpha))
    for t in range(T):
        if t < C*K:
            arm = t%K
        else:
            arm_value = []
            for i in range(K):
                arm_value.append(arm_list[i].get_value(t))
            arm = arm_value.index(max(arm_value))
        freq = int(str(arm+8) + '00000000')
        reward, energy = get_reward_energy(freq, simulator)
        arm_list[arm].update(reward)
        regret = regret + mu_star - mu_list[arm]
        Regret[iteration, t+1] = regret
        accumed_energy = accumed_energy + energy
        rest_task = rest_task - time_interval/(app_time_dic[freq]*1000)
        if rest_task<=0:
            if t<t_min: t_min = t
            cur_finish_time = (t+1)*time_interval/1000
            break
    total_energy[iteration] = accumed_energy
    finish_time[iteration] = cur_finish_time

total_energy = np.mean(total_energy)
finish_time = np.mean(finish_time)

print(f'The HPC application {app}: the execution time is {finish_time:.2f}s and the energy consumption is {total_energy/1000:.4f}MJ')
