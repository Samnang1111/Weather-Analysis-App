import requests 
import matplotlib.pyplot as plt  
import os  

# OpenWeatherMap API key
API_KEY = 'a8aa1554bd05e74f9bd2275c622d3f0d'
try:
    def fetch_weather_data(city):
        # Construct the API request URL with the city name and API key
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={API_KEY}"
        try:
            response = requests.get(url)  # Send the GET request to the API
            data = response.json()  # Parse the JSON response

            # Check if the response status code indicates an error
            if response.status_code != 200:
                print(f"Error: {data['message']}")  # Print the error message from the API
                return None  # Return None if there was an error

            # Extract temperatures for the next 5 days
            temps = []
            for i in range(0, 40, 8):  # Get one temperature per day (every 8th entry)
                temps.append(data['list'][i]['main']['temp'])  # Append the temperature to the list

            return temps  # Return the list of temperatures
        except requests.exceptions.RequestException as e:
            # Handle any exceptions that occur during the request
            print(f"An error occurred: {e}")
            return None  # Return None if an exception occurred

    def collect_weather_data():

        city = input("Enter the city name: ")  # Prompt the user for a city name
        os.system("cls")  # Clear the console screen (Windows specific)
        temperatures = fetch_weather_data(city)  # Fetch the weather data for the city
        
        # Check if temperatures were successfully retrieved
        if temperatures is None:
            print("Failed to get weather data.")
            return None, None, None, None, None  # Return None values if fetching failed

        print(f"Temperatures for the next 5 days in {city}: {temperatures}")  # Print the retrieved temperatures
        return temperatures  # Return the temperatures

    def calculate_average(temps):

        return sum(temps) / len(temps)  # Return the average of the temperatures

    def find_highest(temps):

        return max(temps)  # Return the maximum temperature

    def find_lowest(temps):

        return min(temps)  # Return the minimum temperature

    def present_results(average, highest, lowest):

        print()  # Print a new line for better readability
        print("-----------------------------------")
        print("Results of a 5-Day Weather Analysis")
        print("-----------------------------------")
        print(f"- Average Temperature: {average:.2f} °C")  # Print the average temperature formatted to 2 decimal places
        print(f"- Highest Temperature: {highest} °C")  # Print the highest temperature
        print(f"- Lowest Temperature: {lowest} °C")  # Print the lowest temperature
        print("-----------------------------------")

    def plot_temperatures_line_chart(temps):

        plt.figure(figsize=(10, 5))  # Create a new figure with specified size

        # Plot daily temperatures with markers
        plt.plot(temps, marker='o', color='b', label='Daily Temperatures')

        # Find the highest and lowest temperatures for marking on the plot
        highest_temp = max(temps)
        lowest_temp = min(temps)
        
        # Get the indices of the highest and lowest temperatures
        highest_temp_index = temps.index(highest_temp)
        lowest_temp_index = temps.index(lowest_temp)

        # Plot the highest temperature in green
        plt.plot(highest_temp_index, highest_temp, 'go', label='Highest Temperature')
        
        # Plot the lowest temperature in gray
        plt.plot(lowest_temp_index, lowest_temp, 'o', color='gray', label='Lowest Temperature')

        # Add titles and labels to the chart
        plt.title('Temperature Analysis')
        plt.xlabel('Days')  # X-axis label
        plt.ylabel('Temperature (°C)')  # Y-axis label
        plt.grid(True)  # Add grid lines to the chart
        plt.legend()  # Show the legend
        plt.show()  # Display the plot

    def main(): # Main program

        temps = collect_weather_data()  # Collect weather data
        
        # Check if temperatures were retrieved successfully
        if temps is None:
            return  # Exit the program if fetching data failed

        # Calculate average, highest, and lowest temperatures
        average = calculate_average(temps)
        highest = find_highest(temps)
        lowest = find_lowest(temps)
    
        # Present the calculated results
        present_results(average, highest, lowest)
        
        # Plot the temperature data
        plot_temperatures_line_chart(temps)

    # Entry point for the script
    if __name__ == "__main__":
        main()  # Call the main function 
except Exception as e:
    print("Please enter a valid city name.")  # Print any errors that occurred during execution
    


