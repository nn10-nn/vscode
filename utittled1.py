import numpy as np  
  
def preProcess(N, dx1, dx2, gamma):  
    # 初始化粒子属性  
    part = np.zeros(N, dtype=[  
        ('x', float), ('d', float), ('e', float), ('p', float),  
        ('u', float), ('c', float), ('m', float), ('h', float)  
    ])  
  
    # 粒子位置初始化  
    for i in range(N):  
        if i < ((N / 5) * 4 + 1):
            # 均匀分布位置  
            part['x'][i] = -0.6 + dx1 * i  
            part['d'][i] = 1.0  
            part['e'][i] = 2.5  
        else:  
            # 非均匀分布位置  
            part['x'][i] = dx2 * (i - (4 * N // 5))  
            part['d'][i] = 0.25  
            part['e'][i] = 1.795  
  
        # 通用属性  
        part['p'][i] = (gamma - 1) * part['d'][i] * part['e'][i]  
        part['u'][i] = 0.0  
        part['c'][i] = np.sqrt((gamma - 1) * part['e'][i])  
        part['m'][i] = dx1  # 注意：这里假设所有粒子的质量都是dx1，即使对于非均匀部分  
        if i < ((N / 5) * 4 + 1):
            part['h'][i] = 8 * dx1  
        else:  
            part['h'][i] = 2 * dx2  
  
    return part  
  
# 示例用法  
N = 100  
dx1 = 0.01  
dx2 = 0.02  
gamma = 1.4  
particles = preProcess(N, dx1, dx2, gamma)  
print(particles)