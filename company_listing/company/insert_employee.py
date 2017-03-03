# This is dummy/psudo code used to insert data into mysql DB


        with open('/home/dheeraj/experiments/company/employee.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 5:
                    print row
                    continue
                try:
                    company = Employee()
                    company.company_id = str(row[0])
                    company.name = str(row[1])
                    company.din = row[4]
                    company.designation = row[2]
                    company.appointment_date = datetime.strptime(row[3], "%Y-%m-%d").date() if row[3] !=  '' else None
                    company.save()
                except Exception as e:
                    print row
                    print e
