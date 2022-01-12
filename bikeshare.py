import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months_list = [ 'all', 'january', 'february', 'march', 'april', 'may', 'june']
days_list = [ 'all', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday' , 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input('Choose a city name for more details, \nchicago \nnew york city \nwashington  \n').lower()
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in CITY_DATA.keys():
        print("Its invalid city name,Please type a correct city name")
        city = input('Choose a city name for more details, \nchicago \nnew york city \nwashington  \n').lower()
 
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Choose a month from January to June or all\n").lower()
    while month not in months_list:
        print("Its invalid month, Please type a correct month")
        month = input("Choose a month from January to June or all\n").lower()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Choose a day or all\n").lower()
    while day not in days_list:
        print("Its invalid day, Please type a correct day")
        day = input("Choose a day or all\n").lower
        
    print('-'*40)
    return city.lower(), month.lower(), day.lower()

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
   
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    
    if month != 'all':
        months = ['all','january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) 
        df = df[df['month'] == month]
    if day != 'all':
        days = ['all','monday', 'tuesday', 'wednesday', 'thrusday', 'friday' , 'saturday', 'sunday',]
        day = days.index(day) 
        df = df[df['day'] == day]
        

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    common_day = df['day'].mode()

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()
    print("the most common month: ",common_month)
    print("the most common day of week: ", common_day)
    print("the most common start hour: ",common_start_hour)
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
  
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()


    # TO DO: display most frequent combination of start station and end station trip
    combo_start_end = df['End Station'].mode() + df['End Station'].mode()
    print("most commonly used start station:",common_start_station)
    print("most commonly used end station:",common_end_station)
    print("mostt frequent combination of start station and end station trip:",combo_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    total_travel_time = (df['End Time'] - df['Start Time'])


    # TO DO: display mean travel time
    avg_travel_time = total_travel_time.mean()
    print("total travel time: ", total_travel_time)
    print("mean travel time: ", avg_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].nunique()
    print("counts of user types: ", user_types)


    # TO DO: Display counts of gender
    
    if 'Gender' in df :
        gender_counts = df['Gender'].nunique()
        print("counts of gender: ", gender_counts)
    else:
        print("There's no gender data for that city!")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()
        print("earliest: ", earliest_birth)
        print("most recent birth: ", most_recent_birth)
        print("most common year of birth: ", common_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def head(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while view_data == 'yes' :
        if view_data != 'yes':
            break
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display.lower() != 'yes':
            break
    print('-'*40)    

def main():
    while True:
        city, month, day= get_filters()
        df = load_data(city, month, day)

        time_stats(df)
       
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        head(df)
        print("done")


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
