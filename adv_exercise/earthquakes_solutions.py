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
                latitude = float(elements[1])
                longitude = float(elements[2])
                depth = float(elements[3])

                try:
                    mag = float(elements[4].rstrip("\n"))
                except ValueError:
                    mag = 0.0

                new_record = Record(date_time, latitude, longitude, depth, mag)
                self.records.append(new_record)

    def mean_depth(self):
        depth_sum = 0
        for record in self.records:
            depth_sum = depth_sum + record.depth

        return depth_sum / len(self.records)

    def mean_magnitude(self):
        magnitude_sum = 0
        for record in self.records:
            magnitude_sum += record.magnitude

        return magnitude_sum / len(self.records)

    def max_depth(self):
        max_record = self.records[0]

        for i in range(1, len(self.records)):
            current_record = self.records[i]

            if current_record.depth > max_record.depth:
                max_record = current_record

        return max_record

    def max_magnitude(self):
        max_record = self.records[0]

        for i in range(1, len(self.records)):
            current_record = self.records[i]

            if current_record.magnitude > max_record.magnitude:
                max_record = current_record

        return max_record

    def min_depth(self):
        min_record = self.records[0]

        for i in range(1, len(self.records)):
            current_record = self.records[i]

            if current_record.depth < min_record.depth:
                min_record = current_record

        return min_record

    def min_magnitude(self):
        min_record = self.records[0]

        for i in range(1, len(self.records)):
            current_record = self.records[i]

            if current_record.magnitude < min_record.magnitude:
                min_record = current_record

        return min_record

    def records_occurred_after_max_depth(self):
        max_record = self.max_depth()
        filtered_records = []

        for record in self.records:
            if record.date_time >= max_record.date_time:
                filtered_records.append(record)

        return filtered_records


if __name__ == "__main__":
    earthquakes = RecordSet("earthquakes.txt")

    mean_depth = earthquakes.mean_depth()
    print(f"The mean depth of the earthquakes files is {mean_depth}.")

    mean_magnitude = earthquakes.mean_magnitude()
    print(f"The mean magnitude of the earthquakes files is {mean_magnitude}.")

    max_depth_record = earthquakes.max_depth()
    print(f"The record that has the maximum depth is {max_depth_record}.")

    min_depth_record = earthquakes.min_depth()
    print(f"The record that has the minimum depth is {min_depth_record}.")

    max_magnitude_record = earthquakes.max_magnitude()
    print(f"The record that has the maximum magnitude is {max_magnitude_record}.")

    min_magnitude_record = earthquakes.min_magnitude()
    print(f"The record that has the minimum magnitude is {min_magnitude_record}.")

    filtered_records = earthquakes.records_occurred_after_max_depth()
    for record in filtered_records:
        print(record)
