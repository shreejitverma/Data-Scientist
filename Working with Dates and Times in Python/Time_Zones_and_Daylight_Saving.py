# Time Zones and Daylight Saving!!
# In this chapter, you'll learn to confidently tackle the time-related topic that causes people the most trouble: time zones and daylight saving. Continuing with our bike data, you'll learn how to compare clocks around the world, how to gracefully handle "spring forward" and "fall back," and how to get up-to-date timezone data from the dateutil library.

# Creating timezone aware datetimes
# In this exercise, you will practice setting timezones manually.

# # Import datetime, timezone
# from datetime import datetime, timezone

# # October 1, 2017 at 15:26:26, UTC
# dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo= timezone.utc)

# # Print results
# print(dt.isoformat())


# Setting timezones
# Now that you have the hang of setting timezones one at a time, let's look at setting them for the first ten trips that W20529 took.

# timezone and timedelta have already been imported. Make the change using .replace()

# Create a timezone object corresponding to UTC-4
edt = timezone(timedelta(hours = -4))

# Loop over trips, updating the start and end datetimes to be in UTC-4
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo = edt)
  trip['end'] = trip['end'].replace(tzinfo = edt)


#   What time did the bike leave in UTC?
# Having set the timezone for the first ten rides that W20529 took, let's see what time the bike left in UTC. We've already loaded the results of the previous exercise into memory.


# Loop over the trips
for trip in onebike_datetimes[:10]:
  # Pull out the start and set it to UTC
  dt = trip['start'].astimezone(timezone.utc)
  
  # Print the start time in UTC
  print('Original:', trip['start'], '| UTC:', dt.isoformat())

#   Putting the bike trips into the right time zone
# Instead of setting the timezones for W20529 by hand, let's assign them to their IANA timezone: 'America/New_York'. Since we know their political jurisdiction, we don't need to look up their UTC offset. Python will do that for us.

# Import tz
from dateutil import tz

# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo = et)
  trip['end'] = trip['end'].replace(tzinfo = et)


#   What time did the bike leave? (Global edition)
# When you need to move a datetime from one timezone into another, use .astimezone() and tz. Often you will be moving things into UTC, but for fun let's try moving things from 'America/New_York' into a few different time zones.

# Create the timezone object
uk = tz.gettz('Europe/London')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in the UK?
notlocal = local.astimezone(uk) 

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())


# How many hours elapsed around daylight saving?
# Since our bike data takes place in the fall, you'll have to do something else to learn about the start of daylight savings time.

# Let's look at March 12, 2017, in the Eastern United States, when Daylight Saving kicked in at 2 AM.

# If you create a datetime for midnight that night, and add 6 hours to it, how much time will have elapsed?

# # Import datetime, timedelta, tz, timezone
# from datetime import datetime, timedelta, timezone
# from dateutil import tz

# # Start on March 12, 2017, midnight, then add 6 hours
# start = datetime(2017, 3, 12, tzinfo = tz.gettz('America/New_York'))
# end = start + timedelta(hours = 6)
# print(start.isoformat() + " to " + end.isoformat())

# March 29, throughout a decade
# Daylight Saving rules are complicated: they're different in different places, they change over time, and they usually start on a Sunday (and so they move around the calendar).

# For example, in the United Kingdom, as of the time this lesson was written, Daylight Saving begins on the last Sunday in March. Let's look at the UTC offset for March 29, at midnight, for the years 2000 to 2010.

# Import datetime and tz
from datetime import datetime
from dateutil import tz

# Create starting date
dt = datetime(2000, 3, 29, tzinfo = tz.gettz('Europe/London'))

# Loop over the dates, replacing the year, and print the ISO timestamp
for y in range(2000, 2011):
  print(dt.replace(year=y).isoformat())


#   Finding ambiguous datetimes
# At the end of lesson 2, we saw something anomalous in our bike trip duration data. Let's see if we can identify what the problem might be.

# The data has is loaded as onebike_datetimes, and tz has already been imported from dateutil.

# Loop over trips
for trip in onebike_datetimes:
  # Rides with ambiguous start
  if tz.datetime_ambiguous(trip['start']):
    print("Ambiguous start at " + str(trip['start']))
  # Rides with ambiguous end 
  if tz.datetime_ambiguous(trip['end']):
    print("Ambiguous end at " + str(trip['end']))

#     Cleaning daylight saving data with fold
# As we've just discovered, there is a ride in our data set which is being messed up by a Daylight Savings shift. Let's clean up the data set so we actually have a correct minimum ride length. We can use the fact that we know the end of the ride happened after the beginning to fix up the duration messed up by the shift out of Daylight Savings.

# Since Python does not handle tz.enfold() when doing arithmetic, we must put our datetime objects into UTC, where ambiguities have been resolved.

# onebike_datetimes is already loaded and in the right timezone. tz and timezone have been imported. Use tz.UTC for your timezone.

trip_durations = []
for trip in onebike_datetimes:
  # When the start is later than the end, set the fold to be 1
  if trip['start'] > trip['end']:
    trip['end'] = tz.enfold(trip['end'])
  # Convert to UTC
  start = trip['start'].astimezone(timezone.utc)
  end = trip['end'].astimezone(timezone.utc)

  # Subtract the difference
  trip_length_seconds = (end-start).total_seconds()
  trip_durations.append(trip_length_seconds)

# Take the shortest trip duration
print("Shortest trip: " + str(min(trip_durations)))


