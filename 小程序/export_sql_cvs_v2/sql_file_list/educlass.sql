SELECT bec.id AS id,
 bec.arts_and_cience_type AS artsAndCienceType,
 bec.bilingual_teaching_code AS bilingualTeachingCode,
 bec.build_datet AS buildDatet,
 bec.business_key AS businessKey,
 bec.class_honor_name AS classHonorName,
 bec.create_time AS createTime,
 bec.finish_date AS finishDate,
 bec.grade_business_key AS gradeBusinessKey,
 bec.is_delete AS isDelete,
 bec.is_minority_nationality AS isMinorityNationality,
 bec.length,
 bec.monitor_business_key AS monitorBusinessKey,
 bec.name AS name,
 bec.serial_number AS serialNumber,
 bec.teacher_business_key AS teacherBusinessKey,
 bec.type,
 bec.update_time AS updateTime,
 bec.school_business_key AS schoolBusinessKey
FROM bd_edu_class bec
INNER JOIN bd_school bs ON bs.business_key = bec.school_business_key
INNER JOIN bd_grade bg ON bg.business_key = bec.grade_business_key
WHERE bec.school_business_key = 'e14059b54350457c8726cc99970d14ec'