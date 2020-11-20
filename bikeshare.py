import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input('Which city would you like to see the data for (e.g. chicago, new york city, washington)? ')).lower()
        if city in ('chicago', 'new york city', 'washington'):
            break
        else:
            print('That\'s not a valid city! Please enter a valid city..')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('Which month (e.g. all, january, february, ... , june)? ')).lower()
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):    
            break
        else:
            print('That\'s not a valid month! Please enter a valid month..')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day of week (e.g. all, monday, tuesday, ... sunday)? ').lower()
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            break
        else:
            print('That\'s not a valid day of week! Please enter a valid week..')

    print('-'*40)
    return city, month, day


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
      # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('\nMost common month: ' + months[int(df['month'].mode()[0])-1].title())

    # TO DO: display the most common day of week
    print('\nMost common day of week: ' + df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('\nMost common start hour: ' + str(df['Start Time'].dt.hour.mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nMost commonly used start station: ' + df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('\nMost commonly used end station: ' + df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Stations'] = df['Start Station'] + ' and ' + df['End Station']
    print('\nMost frequent combination of start station and end stations: ' + df['Combined Stations'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal travel time: ' + str(int(df['Trip Duration'].sum()//3600)) 
          + ' hours and ' + str(int((df['Trip Duration'].sum()%3600)//60)) + ' minutes')

    # TO DO: display mean travel time
    print('\nAverage travel time: ' + str(int(df['Trip Duration'].mean()//3600))
          + ' hours and ' + str(int((df['Trip Duration'].mean()%3600)//60)) + ' minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCounts of user types:\n' + str(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    try:
        print('\nCounts of gender:\n' + str(df['Gender'].value_counts().dropna()))
    except:
        print('\nCounts of gender are not available for this city')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\nEarliest year of birth: ' + str(int(df['Birth Year'].min())))
        print('\nMost recent year of birth: ' + str(int(df['Birth Year'].max())))
        print('\nMost common year of birth: ' + str(int(df['Birth Year'].mode()[0])))
    except:
        print('\nEarliest, most recent, and most common year of birth are not available for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df): 
    while True:        
        view_data = str(input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')).lower()
        if view_data in ('yes', 'no'):
            break
        else:
            print('Please enter yes or no..')  
    start_loc = 0
    while (view_data == 'yes'):
        end_loc = start_loc+5
        print(df.iloc[start_loc:end_loc])
        start_loc += 5
        view_data = input('Do you wish to continue?: ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

