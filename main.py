import csv
from csv import reader
import urllib.request
import urllib.error

success = 'We have this many websites! '
count = 0

write_obj = open('working sites.csv', 'a', newline='')
writer = csv.writer(write_obj)

with open('websites 4 wide.csv', 'r') as read_obj:

    csv_reader = (read_obj)

    for row in csv_reader:
        noMark = row.replace('"', '')
        rowPlus = ('http://' + noMark)

        print('trying to run ' + rowPlus)
        try:
            john = urllib.request.urlopen(rowPlus)
        except urllib.error.HTTPError as e:
            print('Shits Whack'.format(e.code))

        except urllib.error.URLError as e:
            print('god why?!'.format(e.reason))

        else:
            count += 1
            print(rowPlus + 'is fucking solid!')
            writer.writerow([rowPlus])
            print(success + str(count))


write_obj.close()


