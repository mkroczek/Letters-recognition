from random import random
from math import exp

class MLP():

    def __init__(self, training_set, n_categories):
        self.network = None
        self.train_data, self.exp_results = training_set
        self.l_rate = 0.3
        self.n_epoch = 20
        self.n_hidden = 5
        self.n_outputs = n_categories

    # Initialize a network
    def initialize_network(self, n_inputs, n_hidden, n_outputs):
        network = list()
        hidden_layer = [{'weights': [random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
        network.append(hidden_layer)
        output_layer = [{'weights': [random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
        network.append(output_layer)
        return network

    # Calculate neuron activation for an input
    def activate(self, weights, inputs):
        activation = weights[-1]
        for i in range(len(weights) - 1):
            activation += weights[i] * inputs[i]
        return activation

    # Transfer neuron activation
    def transfer(self, activation):
        return 1.0 / (1.0 + exp(-activation))

    # Forward propagate input to a network output
    def forward_propagate(self, network, row):
        inputs = row
        for layer in network:
            new_inputs = []
            for neuron in layer:
                activation = self.activate(neuron['weights'], inputs)
                neuron['output'] = self.transfer(activation)
                new_inputs.append(neuron['output'])
            inputs = new_inputs
        return inputs

    # Calculate the derivative of an neuron output
    def transfer_derivative(self, output):
        return output * (1.0 - output)

    # Backpropagate error and store in neurons
    def backward_propagate_error(self, network, expected):
        for i in reversed(range(len(network))):
            layer = network[i]
            errors = list()
            if i != len(network) - 1:
                for j in range(len(layer)):
                    error = 0.0
                    for neuron in network[i + 1]:
                        error += (neuron['weights'][j] * neuron['delta'])
                    errors.append(error)
            else:
                for j in range(len(layer)):
                    neuron = layer[j]
                    errors.append(expected[j] - neuron['output'])
            for j in range(len(layer)):
                neuron = layer[j]
                neuron['delta'] = errors[j] * self.transfer_derivative(neuron['output'])

    # Update network weights with error
    def update_weights(self, network, row, l_rate):
        for i in range(len(network)):
            inputs = row
            if i != 0:
                inputs = [neuron['output'] for neuron in network[i - 1]]
            for neuron in network[i]:
                for j in range(len(inputs)):
                    neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
                neuron['weights'][-1] += l_rate * neuron['delta']

    # Train a network for a fixed number of epochs
    def train_network(self, network, train, exp_results, l_rate, n_epoch, n_outputs):
        for epoch in range(n_epoch):
            sum_error = 0
            for row in range(len(train)):
                outputs = self.forward_propagate(network, train[row])
                expected = [0 for i in range(n_outputs)]
                expected[exp_results[row]] = 1
                sum_error += sum([(expected[i] - outputs[i]) ** 2 for i in range(len(expected))])
                self.backward_propagate_error(network, expected)
                self.update_weights(network, train[row], l_rate)
            print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))

    # Make a prediction with a network
    def predict(self, row):
        print(len(row))
        outputs = self.forward_propagate(self.network, row)
        return outputs.index(max(outputs))

    def train(self):
        self.network = self.initialize_network(len(self.train_data[0]), self.n_hidden, self.n_outputs)
        self.train_network(self.network, self.train_data, self.exp_results, self.l_rate, self.n_epoch, self.n_outputs)

# mlp = MLP()
# network = mlp.initialize_network(2, 1, 2)
# row = [1, 0, None]
# mlp.forward_propagate(network, row)
# expected = [1, 0]
# mlp.backward_propagate_error(network, expected)
# for layer in network:
#     print(layer)
