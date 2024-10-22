from data_generator import generate_fake_temperature_data
from plot_data import plot_temperature_data

if __name__ == '__main__':
    # Generisanje i cuvanje podataka
    data = generate_fake_temperature_data(100)
    data.to_csv('../data/fake_iot_data.csv', index=False)
    print("Podaci su sacuvani u data/fake_iot_data.csv")

    # Vizualizacija podataka
    plot_temperature_data(data)