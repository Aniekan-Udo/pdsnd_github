import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

all_months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWhich city would you like to filter by? (New York City, Chicago, Washington)\n").title()
        if city in CITY_DATA:
            break
        else:
            print("You did not enter a correct city name. Please try again!")



    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("\nWhich month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n").strip().title()
      if month not in all_months:
        print("You can only enter months between January to June!!!")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("\nAre you looking for a particular day? If so, enter the day (e.g., Sunday, Monday) or type 'all' for no preference.\n").strip().title()
        if day in days:
            break
        else:
            print("Please make sure you entered the correct day of the week.")



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (str) df_head - show first 5 rows of dataframe, enter "no" to show statistics without showing dataframe
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load Data
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day and hour of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    # extract day of week 
    df['day-of-week'] = df['Start Time'].dt.day_name()
    # extract hour
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day-of-week'] == day.title()]

    # Ask user if thry want to see the first 5 rows of the raw data
    start_row = 0
    while True:
        df_head = input("Do you want to see the next 5 rows of the raw data? (yes/no): ").lower()
    # if user say yes
        if df_head == "yes":
            # Use iloc to get the first five row by index position
            # remember that start_row has been assignrd 0 above, so its the row of our rat data (index 0)
            raw_data = df.iloc[start_row:start_row + 5]
            print(raw_data)
        # Add 5 to the start_row  for the next interation
            start_row += 5
        # if user does not want to see the raw data, then break and move to the next item.
        elif df_head == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].value_counts().nlargest(1)
    print('This is the most common month:', most_common_month)

    # display the most common day of week
    most_common_day = df['day-of-week'].value_counts().nlargest(1)
    print('This is the most common day of the week:', most_common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].value_counts().nlargest(1)
    print('This is the most common start hour:', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Start_Station = df['Start Station'].value_counts().nlargest(1)
    print('\nThis is the most commonly used start station:', Start_Station)

    # display most commonly used end station
    End_Station = df['End Station'].value_counts().nlargest(1)
    print('\nThis is the most commonly used end station:', End_Station)

    # display most frequent combination of start station and end station trip
    most_freq_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()

    # Extract the values from most_freq_comb into start_station and end_station this will help us print the result better
    start_station, end_station = most_freq_combination

    print('\nMost frequently combination trips starts from', start_station, " to ", end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_travel_time = df['Trip Duration'].sum()
    print('This is the Total travel time: ', Total_travel_time)

    # display mean travel time
    Mean_travel_time = df['Trip Duration'].mean()
    print('This is the mean travel time: ', Mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        User_type = df['User Type'].value_counts()
        print('User type:\n', User_type)
    except KeyError:
        print("No column like User Type in the DataFrame")


    # Display counts of gender counts
    try:
        gender_count = df['Gender'].value_counts()
        print('gender_count:\n', gender_count)
    except KeyError:
        print("No column like Gender in the DataFrame")



    # Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nThere is no available data to work with.\nThis could result from the DataFrame not having the column name 'Birth Year'")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nThere is no available data to work with.\nThis could result from the DataFrame not having the column name 'Birth Year'.")

    try:
      Most_Common_Year = df['Birth Year'].mode().get([0])
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nThere is no available data to work with.\nThis could result from the DataFrame not having the column name 'Birth Year'")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
