import csv
from supabase import create_client
import os

# Initialize Supabase client
url = "https://wxwxtdgvubhrpdhczgfj.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind4d3h0ZGd2dWJocnBkaGN6Z2ZqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE1MTUyMTgsImV4cCI6MjA1NzA5MTIxOH0.YpWVZuNIIGQ8bJi5cMgG-2KtkZKoFaKYVAtaguAdX3k"
supabase = create_client(url, key)

def process_nl_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        counter = 1
        for line in file:
            data = line.strip().split(':')
            if len(data) >= 9:
                print(f"Migrating NL record {counter}")
                record = {
                    'telefoonnummer': data[0],
                    'facebookid': data[1],
                    'voornaam': data[2],
                    'achternaam': data[3],
                    'geslacht': data[4],
                    'plaatsnaam': data[5],
                    'geboorteplaats': data[6],
                    'status': data[7],
                    'bedrijfsnaam': data[8]
                }
                supabase.table('profiles').insert(record).execute()
                counter += 1

def process_be_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        counter = 1
        reader = csv.reader(file)
        for row in reader:
            print(f"Migrating BE record {counter}")
            record = {
                'telefoonnummer': row[0],
                'facebookid': row[1],
                'voornaam': row[2],
                'achternaam': row[3],
                'geslacht': row[4],
                'plaatsnaam': row[5],
                'status': row[6],
                'bedrijfsnaam': row[7],
                'geboorteplaats': ''  # Empty for Belgian records
            }
            supabase.table('profiles').insert(record).execute()
            counter += 1

# Process files
process_nl_file('data/Netherlands 01.txt')
process_nl_file('data/Netherlands 02.txt')
process_be_file('data/Belgium.txt')