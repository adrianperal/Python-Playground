from datetime import datetime


class Record:
    def __init__(self, date_time, latitude, longitude, depth, magnitude):
        self.date_time = date_time
        self.latitude = latitude
        self.longitude = longitude
        self.depth = depth
        self.magnitude = magnitude

    def __str__(self):
        return f"{self.date_time}: {self.depth}, {self.magnitude}"


class RecordSet:
    def __init__(self, input_file):
        self.records = []
        self.parse_records(input_file)

    def parse_records(self, from_file):
        with open(from_file, "r") as records_file:
            lines = records_file.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    continue

                elements = line.split(",")
                str_date_time = elements[0]

                date_time = datetime.strptime(str_date_time, '%Y-%m-%dT%H:%M:%S.%fZ')
                latitude = # TODO
                longitude = # TODO
                depth = # TODO
                mag = # TODO

                new_record = None # TODO
                self.records.append(new_record)

    def mean_depth(self):
        depth_sum = 0
        for record in self.records:
            depth_sum = depth_sum + record.depth

        return depth_sum / len(self.records)

    def mean_magnitude(self):
        # TODO

    def max_depth(self):
        # TODO

    def max_magnitude(self):
        # TODO

    def min_depth(self):
        # TODO

    def min_magnitude(self):
        # TODO

    def records_occurred_after_max_depth(self):
        # TODO

if __name__ == "__main__":
    earthquakes = RecordSet("earthquakes.txt")

    mean_depth = # Call the appropriate method
    print(f"The mean depth of the earthquakes files is {mean_depth}.")

    mean_magnitude = # Call the appropriate method
    print(f"The mean magnitude of the earthquakes files is {mean_magnitude}.")

    max_depth_record = # Call the appropriate method
    print(f"The record that has the maximum depth is {max_depth_record}.")

    min_depth_record = # Call the appropriate method
    print(f"The record that has the minimum depth is {min_depth_record}.")

    max_magnitude_record = # Call the appropriate method
    print(f"The record that has the maximum magnitude is {max_magnitude_record}.")

    min_magnitude_record = # Call the appropriate method
    print(f"The record that has the minimum magnitude is {min_magnitude_record}.")

    filtered_records = # Call the appropriate method
    # TODO: Loop over the filtered_records and print out the details!
