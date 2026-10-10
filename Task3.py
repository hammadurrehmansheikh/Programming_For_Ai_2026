attendance = [72, 85, 90, 60, 40, 78, 88]

meeting_requirement = 0

not_meeting_requirement = 0

for attendance_value in attendance:
    if(attendance_value >= 75):
        meeting_requirement += 1
    else:
        not_meeting_requirement += 1

print("meeting_requirement : ",meeting_requirement)

print("not_meeting_requirement : ",not_meeting_requirement)