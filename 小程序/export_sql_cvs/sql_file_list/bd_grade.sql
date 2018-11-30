SELECT bg.id AS id,
 bg.base_grade_business_key AS baseGradeBusinessKey,
 bg.business_key AS businessKey,
 bg.create_time AS createTime,
 bg.finish_date AS finishDate,
 bg.grade_level AS gradeLevel,
 bg.leader_business_key AS leaderBusinessKey,
 bg.name AS name,
 bg.period_level AS periodLevel,
 bg.school_business_key AS schoolBusinessKey,
 bg.serial_number AS serialNumber,
 bg.update_time AS updateTime,
 bg.is_delete AS isDelete
FROM bd_grade bg
INNER JOIN bd_school bs ON bs.business_key = bg.school_business_key
WHERE bg.school_business_key = 'e14059b54350457c8726cc99970d14ec'