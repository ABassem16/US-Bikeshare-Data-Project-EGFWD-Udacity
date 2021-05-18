import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS= ['January','Feburary','March','April','May','June','July','August','September','October','November','December','All']
DAYS=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']

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
    cities=CITY_DATA.keys()
    city=''
    month=''
    day=''
    while city not in cities:
        try:
            city=input('Enter city name you want to analyze: ')
        except Exception as e:
            print('Exception Occurred :{}'.format(e))

    # get user input for month (all, january, february, ... , june)
    while month not in MONTHS:
        try:
            month=input('Enter month you want to analyze, type all for all months: ').title()
        except Exception as e:
             print('Exception Occurred :{}'.format(e))
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in DAYS:
        try:
            day=input('Enter day you want to analyze, type all for all days: ').title()
        except Exception as e:
             print('Exception Occurred :{}'.format(e))

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.dayofweek
    if month!='All':
        month=MONTHS.index(month)+1
        print(month)
        df=df[df['month']==month]
    if day!='All':
        day=DAYS.index(day)
        df=df[df['day']==day]
        print("day modified")
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if not df.empty:
        mostCommonMonth=MONTHS[df['month'].mode()[0]-1]
        print('Most Common Month: ' , mostCommonMonth)
        # display the most common day of week
        mostCommonDay=DAYS[df['day'].mode()[0]]
        print('Most Common Day: ' , mostCommonDay)
        # display the most common start hour
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['hour']=df['Start Time'].dt.hour
        mostCommonHour=df['hour'].mode()[0]
        if mostCommonHour>12:    
            print('Most Common Hour: ' , mostCommonHour-12 , ':00 PM')
        else:
            print('Most Common Hour: ' , mostCommonHour , ':00 AM')
    else:
        print("DataFrame is empty!")   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    if not df.empty:
        # display most commonly used start station
        mostCommonStart=df['Start Station'].value_counts().index[0]
        print('Most Common Start Station: ' , mostCommonStart)
        # display most commonly used end station
        mostCommonEnd=df['End Station'].value_counts().index[0]
        print('Most Common End Station: ' , mostCommonEnd)

        # display most frequent combination of start station and end station trip
        mostFrqeuentCombination=(df['Start Station'] + ' AND ' + df['End Station']).mode()[0]
        print('Most Frequent Combination of stations: ' , mostFrqeuentCombination)
    else:
        print("DataFrame is empty!")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    if not df.empty:
        # display total travel time
        totalTravelTime=df['Trip Duration'].sum()
        print('Total Travel Time in minutes: ' , totalTravelTime/60)
        # display mean travel time
        meanTravelTime=df['Trip Duration'].mean()
        print('Mean Travel Time in minutes: ' , meanTravelTime/60)
    else:
        print("DataFrame is empty!")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    if not df.empty:
        if 'User Type' in df.columns:
            userTypes=df['User Type'].value_counts()
            print(userTypes)
        # Display counts of gender
        if 'Gender' in df.columns:
            genders=df['Gender'].value_counts()
            print(genders)
        # Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df.columns:
            mostRecentDOB=df['Birth Year'].max()
            earliestDOB=df['Birth Year'].min()
            mostCommonDOB=df['Birth Year'].mode()[0]
            print('Most Recent Date of Birth: ' , mostRecentDOB)
            print('Most Common Date of Birth: ' , mostCommonDOB)
            print('Earliest Date of Birth: ' , earliestDOB)
    else:
        print("DataFrame is empty!")
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
