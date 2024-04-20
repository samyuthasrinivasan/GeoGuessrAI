class AI():

  def __init__(self):
    self.registeredCountries = {}

  def predict(self, img): # need to fix, for loop is looping through countries and is calling the method on the inner dictionary with the metas instead of singular metas
    list_of_tuples = []
    for country in self.registeredCountries:
      for dict_meta in self.registeredCountries[country]:
        list_of_tuples.append((dict_meta, dict_meta.get_confidence(img)))

    return sorted(list_of_tuples, key=lambda x: x[1])

  def add_perceptron(self, country, perceptron):
    self.registeredCountries.update({country: perceptron})

  def get_dictionary(self):
    return self.registeredCountries
