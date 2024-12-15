import numpy as np
import matplotlib.pyplot as plt

def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

if __name__ == '__main__':
    plt.figure(figsize=(8, 6.5))
    window_size = 5
    model_learning_period = 1000
    evaluation_cycle = 50
    scale = model_learning_period / evaluation_cycle

    # Directory for data with kmeans
    dir_2_1 = 'C:/Users/berna/Desktop/uav/TSI/result/qmix/RDMmodel_aided_fedqmix'  
    
    # Load data
    data_2_1 = np.load(dir_2_1 + '/global_data.npy') / 200000

    # With kmeans (Red Graph)
    mean_data_2 = np.mean([data_2_1], axis=0)
    low_quantile_data_2 = np.percentile([data_2_1], 0.5, axis=0)
    high_quantile_data_2 = np.percentile([data_2_1], 99.5, axis=0)
    mv_mean_data_2 = moving_average(mean_data_2, window_size)
    mv_low_quantile_data_2 = moving_average(low_quantile_data_2, window_size)
    mv_high_quantile_data_2 = moving_average(high_quantile_data_2, window_size)
    mv_x_axis_2 = list(range(len(mv_mean_data_2)))
    mv_x_axis_2 = mv_x_axis_2[0:101] + [(x-98) * evaluation_cycle for x in mv_x_axis_2[101:]]

    # Plot graph for dir_2_1
    plt.plot(mv_x_axis_2, mv_mean_data_2, color='red', linewidth=4, label='Model-aided FedQMIX', linestyle='-')
    plt.fill_between(mv_x_axis_2, mv_low_quantile_data_2, mv_high_quantile_data_2, color='g', alpha=0.1)

    # Actual number of episodes
    num_episodes_with_kmeans = len(data_2_1) * evaluation_cycle + len(data_2_1) * model_learning_period
    print("Number of episodes (with kmeans):", num_episodes_with_kmeans)

    # Set plot properties
    plt.xscale("log")
    plt.grid()
    plt.xlim([0.11, 1000])
    plt.ylim([0.0, 1.0])
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xlabel('Episode [log scale]', fontsize=22)
    plt.ylabel('Data collection ratio', fontsize=22)
    plt.legend(loc='upper right', fontsize=18)
    plt.show()
