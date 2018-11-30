SELECT DISTINCT btt.id AS id,
 btt.business_key AS businessKey,
 btt.edu_class_business_key AS eduClassBusinessKey,
 btt.phases_key AS phasesKey,
 btt.reason AS reason,
 btt.remark AS remark,
 btt.subject_key AS subjectKey,
 btt.teacher_business_key AS teacherBusinessKey,
 btt.teaching_course_no AS teachingCourseNo,
 btt.teaching_start_date AS teachingStartDate,
 btt.teaching_end_date AS teachingEndDate,
 btt.total_hours AS totalHours,
 btt.grade_key AS gradeKey,
 btt.grade_key AS gradeBussinessKey,
 btt.create_time AS createTime,
 btt.is_delete AS isDelete,
 btt.name AS name,
 btt.school_business_key AS schoolBusinessKey,
 btt.text_book_version_business_key AS textBookVersionBusinessKey,
 btt.update_time AS updateTime,
 btt.publish_time AS publishTime
FROM bd_teacher_teaching btt
INNER JOIN bd_school bs ON bs.business_key = btt.school_business_key
INNER JOIN bd_grade bg ON bg.business_key = btt.grade_key
INNER JOIN bd_edu_class bec ON bec.business_key = btt.edu_class_business_key
WHERE btt.school_business_key = 'e14059b54350457c8726cc99970d14ec'