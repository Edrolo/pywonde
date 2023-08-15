
## Endpoints

### Implemented
Deletions
    /schools/{school_id}/deletions
Schools
    /schools
    /schools/all
    /schools/approved
    /schools/pending
    /schools/audited
    /schools/offline
    /schools/revoked
    /schools/declined
    /meta/schools/{school_id}
    /meta/schools/{school_id}/permissions
    /meta/schools/{school_id}/acl
    /schools/{school_id}
    /schools/{school_id}/request-access POST
    /schools/{school_id}/revoke-access  DELETE
Classes
    /schools/{school_id}/classes
    /schools/{school_id}/classes/{class_id}
Employees
    /schools/{school_id}/employees
    /schools/{school_id}/employees/{employee_id}
Students
    /schools/{school_id}/students
    /schools/{school_id}/students/{student_id}
Subjects
    /schools/{school_id}/subjects
    /schools/{school_id}/subjects/{subject_id}
Lessons
    /schools/{school_id}/lessons
    /schools/{school_id}/lessons/{lesson_id}


### Not yet implemented
Achievements
    /schools/{school_id}/achievements
    /schools/{school_id}/achievements/{achievement_id}   GET POST DELETE
Assessments
    /schools/{school_id}/assessment/aspects
    /schools/{school_id}/assessment/aspects/{aspect_id}
    /schools/{school_id}/assessment/results
    /schools/{school_id}/assessment/results/{result_id}
    /schools/{school_id}/assessment/resultsets
    /schools/{school_id}/assessment/resultsets/{result_set_id}
    /schools/{school_id}/assessment/templates
    /schools/{school_id}/assessment/templates/{template_id}
    /schools/{school_id}/assessment/marksheets
    /schools/{school_id}/assessment/marksheets/{mark_sheet_id}
Attendance
    /schools/{school_id}/attendance/session GET POST
    /schools/{school_id}/attendance-leavers/session
    /schools/{school_id}/attendance/lesson  GET POST
Attendance Codes
    /attendance-codes
    /schools/{school_id}/attendance-codes
Attendance Summaries
    /schools/{school_id}/attendance-summaries
    /schools/{school_id}/attendance-summaries/{summary_id}
Behaviours
    /schools/{school_id}/behaviours GET POST
    /schools/{school_id}/behaviours/{behaviour_id}  GET DELETE
Contacts
    /schools/{school_id}/contacts
    /schools/{school_id}/contacts/{contact_id}
Contact Details
    No endpoints
Doctors
    /schools/{school_id}/doctors
    /schools/{school_id}/doctors/{doctor_id}
Detentions
    /schools/{school_id}/detentions
    /schools/{school_id}/detentions/{detention_id}
Detention Attendance Codes
    /schools/{school_id}/detention-attendance-codes
Detention Attendance
    /schools/{school_id}/attendance/detention
    /schools/{school_id}/attendance/detention/{detention_attendance_id}
Detention Types
    /schools/{school_id}/detention-types
    /schools/{school_id}/detention-types/{detention__type_id}
Counts
    /schools/{school_id}/counts
Employee Absences
    /schools/{school_id}/employee-absences  GET POST
    /schools/{school_id}/employee-absences/{employee_absence}   GET PUT DELETE
Events
    /schools/{school_id}/events
    /schools/{school_id}/events/{event_id}
Extended Details
    No endpoints
Exclusions
    /schools/{school_id}/exclusions
    /schools/{school_id}/exclusions/{exclusion_id}
Groups
    /schools/{school_id}/groups
    /schools/{school_id}/groups/{group_id}
Medical Conditions
    /schools/{school_id}/medical-conditions
    /schools/{school_id}/medical-conditions/{medical_condition_id}
Medical Events
    /schools/{school_id}/medical-events
    /schools/{school_id}/medical-events/{medical_event_id}
Medical Notes
    /schools/{school_id}/medical-notes
    /schools/{school_id}/medical-notes/{medical_note_id}
Periods
    /schools/{school_id}/periods
    /schools/{school_id}/periods/{period_id}
Photos
    /schools/{school_id}/photos
    /schools/{school_id}/photos/{photo_id}
Rooms
    /schools/{school_id}/rooms
    /schools/{school_id}/rooms/{room_id}
Pre-Admission Students
    /schools/{school_id}/students-pre-admission
    /schools/{school_id}/students-pre-admission/{student_id}
Student Leavers
    /schools/{school_id}/students-leaver
    /schools/{school_id}/students-leaver/{student_id}
Student Absences
    /schools/{school_id}/attendance/absence
    /schools/{school_id}/attendance/absence/{student_absence}
Writebacks
    /writebacks/{writeback_id}
