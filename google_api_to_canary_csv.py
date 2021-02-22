import os
import sys


CSV_DIRECTORY = 'csv_outputs/'


def main():
    """
    to run this file:
    python google_api_to_canary_csv.py {GOOGLE_TRANSCRIPT_DIRECTORY}
    """
    input_files = sys.argv[1]
    for filename in os.listdir(input_files):
        csv_content = ''
        if filename != '.DS_Store':
            with open(input_files + filename, 'r') as transcript:
                data = transcript.read().replace('\n', '').replace('results', '\nresults')[1:]
                for line in iter(data.splitlines()):
                    arr = line.split('words ')
                    csv_content += arr[0].replace('\\', '')
                    for word in arr[1:]:
                        test = word.replace('{      start_time {', ',')
                        test = test.replace('}      end_time {', ',')
                        test = test.replace('}      word: ', ',').replace('    }', ',').replace(',  }}', ',')
                        test = test.replace('\\', ''). replace('\"', '')
                        csv_content += test + '\n'
                    csv_content += '\n'
                if not os.path.exists(CSV_DIRECTORY):
                    os.mkdir(CSV_DIRECTORY)
                output_file = open(CSV_DIRECTORY + filename + '_processed.csv', 'w')
                output_file.write(csv_content)
                output_file.close()


if __name__ == "__main__":
    main()
