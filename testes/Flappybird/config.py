""" 
[NEAT]
fitness_criterion     = max           maximizar pontuação
fitness_threshold     = 1000          termina quando alcançar 1000 pontos
pop_size              = 100           tamanho da população
reset_on_extinction   = False         mensagem de erro quando uma especie for extinta em vez de resetar especie

[DefaultGenome]
# node activation options
activation_default      = tanh          tangente hiperbolica no output
activation_mutate_rate  = 0.0           0.0 significa que não testará outra função dentro do output
activation_options      = tanh          opções de funções para uso: apenas tangente hiperbolica

# node aggregation options
aggregation_default     = sum           soma entre os inputs*peso
aggregation_mutate_rate = 0.0           não testará outros tipos de operações
aggregation_options     = sum           as opções são apenas a soma

# node bias options
bias_init_mean          = 0.0           média do bias
bias_init_stdev         = 1.0           desvio padrão
bias_max_value          = 30.0
bias_min_value          = -30.0
bias_mutate_power       = 0.5           poder de mutação
bias_mutate_rate        = 0.7           probabilidade de modificar o bias
bias_replace_rate       = 0.1           probabilidade de criar um novo bias aleatorio

# genome compatibility options                      configura a classificação de cada especie
compatibility_disjoint_coefficient = 1.0
compatibility_weight_coefficient   = 0.5

# connection add/remove rates
conn_add_prob           = 0.5           probabilidade de adicionar um input novo
conn_delete_prob        = 0.5           probabilidade de excluir um input

# connection enable options
enabled_default         = True          True: só terá conexoes ativas
enabled_mutate_rate     = 0.01          probabilidade de mutação nas conexões

feed_forward            = True          camadas são conectadas sempre pra frente
initial_connection      = full          full: todos os inputs conectados

# node add/remove rates
node_add_prob           = 0.2           probabilidade de adicionar um nó novo (bolinha)
node_delete_prob        = 0.2           probabilidade de remover um nó (bolinha)

# network parameters
num_hidden              = 0             nós intermediários    
num_inputs              = 3             quantos nós iniciais
num_outputs             = 1             quantas saídas

# node response options                 response: valor que será multiplicado pelo resultado do inputs*peso
response_init_mean      = 1.0
response_init_stdev     = 0.0
response_max_value      = 30.0
response_min_value      = -30.0
response_mutate_power   = 0.0
response_mutate_rate    = 0.0
response_replace_rate   = 0.0

# connection weight options             pesos dos inputs
weight_init_mean        = 0.0
weight_init_stdev       = 1.0
weight_max_value        = 30
weight_min_value        = -30
weight_mutate_power     = 0.5
weight_mutate_rate      = 0.8
weight_replace_rate     = 0.1

[DefaultSpeciesSet]
compatibility_threshold = 3.0           nivel de compatibilidade para ser considerado de uma especie

[DefaultStagnation]
species_fitness_func = max              maximizar pontuação (objetivo das especies)
max_stagnation       = 20               numero maximo de gerações que uma especie pode ficar sem evoluir
species_elitism      = 2                garente que pelo menos duas especies nao sejam extintas por nao evoluirem

[DefaultReproduction]
elitism            = 2                  dois individuos sao passados para a proxima geração sem sofrer mutações
survival_threshold = 0.2                percentual de uma especie que pode se reproduzir de uma geração para outra

"""