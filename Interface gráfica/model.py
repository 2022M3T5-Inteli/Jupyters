import pickle
import seaborn as sns
import matplotlib.pyplot as plt

class Model():
       def __init__(self, path, total, name) -> None:
              self.model = pickle.load(open(path, 'rb'))
              self.prediction_dictionary = {
                     f'{total} | {name}%': [], 
                     f'AB | {name}%': [], 
                     f'C1 | {name}%': [], 
                     f'C2 | {name}%': [],
                     f'DE | {name}%': [], 
                     f'Masculino | {name}%': [], 
                     f'Feminino | {name}%': [], 
                     f'4-11 anos | {name}%': [],
                     f'12-17 anos | {name}%': [], 
                     f'18-24 anos | {name}%': [], 
                     f'25-34 anos | {name}%': [],
                     f'35-49 anos | {name}%': [], 
                     f'50-59 anos | {name}%': [], 
                     f'60+ anos | {name}%': []
              } 
              self.mean_predictions = {
                     f'{total} | {name}%': 0, 
                     f'AB | {name}%': 0, 
                     f'C1 | {name}%': 0, 
                     f'C2 | {name}%': 0,
                     f'DE | {name}%': 0, 
                     f'Masculino | {name}%': 0, 
                     f'Feminino | {name}%': 0, 
                     f'4-11 anos | {name}%': 0,
                     f'12-17 anos | {name}%': 0, 
                     f'18-24 anos | {name}%': 0, 
                     f'25-34 anos | {name}%': 0,
                     f'35-49 anos | {name}%': 0, 
                     f'50-59 anos | {name}%': 0, 
                     f'60+ anos | {name}%': 0
              } 
              self.time_array = []

       def evaluate_predictions(self, input_data):
              duration = int(input_data.pop() / 5)
              x_s = []
              predictions = []
              for i in range(int(duration)):
                     if x_s == []:
                            pass
                     elif input_data[4] == 55:
                            if input_data[3] == 29:
                                   input_data[3] = 6 
                                   input_data[4] = 0
                            else:
                                   input_data[3] += 1
                                   input_data[4] = 0
                     else:
                            input_data[4] += 5
                     self.time_array.append(str(input_data[3]) + ":" + 
                            str(input_data[4]))
                     x_s.append(input_data.copy())
              
              predictions = self.model.predict(x_s)
              for prediction in predictions:
                     for i in range(len(self.prediction_dictionary.keys())):
                            self.prediction_dictionary[list(self.prediction_dictionary.keys())[i]].append(prediction[i])
              
              for key in self.prediction_dictionary.keys():
                     self.mean_predictions[key] = (sum(self.prediction_dictionary[key])/len(self.prediction_dictionary[key]))
              return self.mean_predictions

class Rat():
       def __init__(self) -> None:
              self.total_rat = pickle.load(open('main_rat.txt', 'rb'))
              self.demographics = pickle.load(open('all_rat.txt', 'rb'))
              self.rat_prediction = []
              self.mean_predictions = {}
              self.prediction_dictionary = {
                     'Total Domicílios | Rat%': [], 
                     'AB | Rat%': [], 
                     'C1 | Rat%': [], 
                     'C2 | Rat%': [],
                     'DE | Rat%': [], 
                     'Masculino | Rat%': [], 
                     'Feminino | Rat%': [], 
                     '4-11 anos | Rat%': [],
                     '12-17 anos | Rat%': [], 
                     '18-24 anos | Rat%': [], 
                     '25-34 anos | Rat%': [],
                     '35-49 anos | Rat%': [], 
                     '50-59 anos | Rat%': [], 
                     '60+ anos | Rat%': []
              } 
              self.time_array = []

       def get_main_rat(self, input_data):
              self.time_array = []
              duration = int(input_data.pop() / 5)
              x_s = []
              for i in range(int(duration)):
                     if x_s == []:
                            pass
                     elif input_data[4] == 55:
                            if input_data[3] == 29:
                                   input_data[3] = 6 
                                   input_data[4] = 0
                            else:
                                   input_data[3] += 1
                                   input_data[4] = 0
                     else:
                            input_data[4] += 5
                     self.time_array.append(str(input_data[3]) + ":" + 
                            str(input_data[4]))
                     x_s.append(input_data.copy())
              self.rat_prediction = list(self.total_rat.predict(x_s))
              output = {
                     'mean': str(sum(self.rat_prediction)/len(self.rat_prediction))[:4],
                     'all': self.rat_prediction
              }
              return output
              

       def get_demographics(self, input_data):
              self.time_array = []
              duration = int(input_data.pop() / 5)
              x_s = []
              for i in range(int(duration)):
                     if x_s == []:
                            pass
                     elif input_data[4] == 55:
                            if input_data[3] == 29:
                                   input_data[3] = 6 
                                   input_data[4] = 0
                            else:
                                   input_data[3] += 1
                                   input_data[4] = 0
                     else:
                            input_data[4] += 5
                     self.time_array.append(str(input_data[3]) + ":" + 
                            str(input_data[4]))
                     x_s.append(input_data.copy())
              predictions = self.demographics.predict(x_s)

              for prediction in predictions:
                     for i in range(len(self.prediction_dictionary.keys())):
                            self.prediction_dictionary[list(self.prediction_dictionary.keys())[i]].append(prediction[i])
                            
              for key in self.prediction_dictionary.keys():
                     self.mean_predictions[key] = (sum(self.prediction_dictionary[key])/len(self.prediction_dictionary[key]))
              
              return self.mean_predictions
       