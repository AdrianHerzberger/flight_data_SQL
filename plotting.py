import matplotlib.pyplot as plt

def plot_delayed_flights_percentage(data):
    """
    Plot the percentage of delayed flights per airline.
    """
    airlines = [record['AIRLINE'] for record in data]
    total_flights = [record['TOTAL_FLIGHTS'] for record in data]
    delayed_flights = [record['DELAYED_FLIGHTS'] for record in data]

    percentages = [delayed / total * 100 if total != 0 else 0 for delayed, total in zip(delayed_flights, total_flights)]

    plt.figure(figsize=(10, 6))
    plt.barh(airlines, percentages, color='skyblue')
    plt.xlabel('Percentage of Delayed Flights (%)')
    plt.title('Percentage of Delayed Flights per Airline')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
