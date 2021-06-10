import numpy as np
import math as math


g_0 = 9.80665               #m/s^2
m_dry = 2000.0              #kg   
m_fuel = 300.0              #kg
m_wet = m_dry + m_fuel
T_max = 24000.0             #N
rho_1 = 0.2 * T_max         #thrust lower bound
rho_2 = 0.8 * T_max         # thrust upper bound
alhpa = 0.0005              #s/m
r_0 = np.array([2400.0, 450.0, -330.0]).T   #m -initial position
r_dot = np.array([-10.0, -40.0, 10.0]).T    #m/s -intial velocity
r_f = np.array([0.0, 0.0, 0.0]).T
r_dot_f = np.array([0.0, 0.0 ,0.0]).T

g_m = np.array([-3.71, 0.0, 0.0]).T             # mars gravity m/s^2
omega = np.array([2.53E-5, 0.0, 6.62E-5]).T   #mars constant angular velocity
gamma = np.radians(30.0)        # the glide scope constraint 
theta = np.radians(120.0)
r_dotmax = 90.0                 # max velocity m/s



e1 = np.array([1.0, 0.0, 0.0]).T
e2 = np.array([0.0, 1.0, 0.0]).T
e3 = np.array([0.0, 0.0, 1.0]).T


