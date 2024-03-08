import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def simulate_bandwagon_effect(population_size, rounds, initial_buyers_ratio):
    population = np.zeros(population_size)
    initial_buyers = int(population_size * initial_buyers_ratio)
    population[:initial_buyers] = 1
    np.random.shuffle(population)
    
    def decide_to_buy(current_ratio):
        return np.random.rand() < current_ratio
    
    buyers_ratio = [initial_buyers_ratio]
    
    for round in range(rounds):
        undecided_indices = np.where(population == 0)[0]
        if undecided_indices.size == 0:
            break
        current_ratio = population.sum() / population_size
        for idx in undecided_indices:
            if decide_to_buy(current_ratio):
                population[idx] = 1
        buyers_ratio.append(population.sum() / population_size)
    
    return buyers_ratio


# Streamlit UI
st.title('Bandwagon Effect Simulation')

population_size = st.slider('Population Size', min_value=100, max_value=10000, value=1000, step=100)
rounds = st.slider('Number of Rounds', min_value=1, max_value=50, value=20)
initial_buyers_ratio = st.slider('Initial Buyers Ratio', min_value=0.01, max_value=0.1, value=0.05, step=0.01)

if st.button('Simulate'):
    buyers_ratio = simulate_bandwagon_effect(population_size, rounds, initial_buyers_ratio)
    
    plt.figure(figsize=(10, 6))
    plt.plot(buyers_ratio, marker='o', linestyle='-')
    plt.title('Bandwagon Effect Simulation')
    plt.xlabel('Round')
    plt.ylabel('Ratio of Buyers')
    plt.grid(True)
    st.pyplot(plt)
