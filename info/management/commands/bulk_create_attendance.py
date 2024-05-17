from django.core.management.base import BaseCommand
from info.models import AttendanceClass, Assign, AttendanceRange
from datetime import timedelta

class Command(BaseCommand):
    help = 'Bulk create attendance records for all assignments within the attendance range'

    def handle(self, *args, **kwargs):
        try:
            attendance_range = AttendanceRange.objects.latest('start_date')
            start_date = attendance_range.start_date
            end_date = attendance_range.end_date
            assignments = Assign.objects.all()

            self.stdout.write(self.style.SUCCESS(f'Using attendance range from {start_date} to {end_date}'))
            self.stdout.write(self.style.SUCCESS(f'Found {assignments.count()} assignments'))

            days = {
                'Monday': 1,
                'Tuesday': 2,
                'Wednesday': 3,
                'Thursday': 4,
                'Friday': 5,
                'Saturday': 6,
            }

            def daterange(start_date, end_date):
                for n in range(int((end_date - start_date).days) + 1):
                    yield start_date + timedelta(n)

            created_count = 0
            for assign in assignments:
                self.stdout.write(self.style.SUCCESS(f'Processing assignment: {assign}'))
                for single_date in daterange(start_date, end_date):
                    assign_times = assign.assigntime_set.all()
                    self.stdout.write(self.style.SUCCESS(f'Date: {single_date}, Assign times: {assign_times.count()}'))
                    for assign_time in assign_times:
                        if single_date.isoweekday() == days[assign_time.day]:
                            attendance_class, created = AttendanceClass.objects.get_or_create(
                                date=single_date,
                                assign=assign
                            )
                            if created:
                                created_count += 1
            
            self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} attendance records.'))

        except AttendanceRange.DoesNotExist:
            self.stdout.write(self.style.ERROR('No AttendanceRange found. Please create one in the admin interface.'))
