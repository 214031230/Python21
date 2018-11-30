SELECT bu.id AS id,
 bu.business_key AS businessKey,
 bu.pass_word AS passWord,
 bu.create_time AS createTime,
 bu.device_number AS deviceNumber,
 bu.email AS email,
 bu.id_card AS idCard,
 bu.ji_num AS jiNum,
 bu.telphone AS telphone,
 bu.category AS category,
 bu.update_time AS updateTime,
 bu.user_code AS userCode,
 bu.birthday AS birthday,
 bu.name AS name,
 bu.phone AS phone,
 bu.sex AS sex,
 bu.nickname AS nickname,
 bu.status_type AS statusType,
 bu.is_delete AS isDelete,
 bs.school_business_key AS schoolBusinessKey,
 bs.grade_business_key AS gradeBusinessKey,
 bs.class_business_key AS classBusinessKey,
 bs.head_portrait AS headPortrait,
 bs.picture,
 bs.history_num AS historyNum
FROM base_user bu
INNER JOIN bd_student bs ON bs.id = bu.id
INNER JOIN bd_school bl ON bl.business_key = bs.school_business_key
INNER JOIN bd_grade bg ON bg.business_key = bs.grade_business_key
INNER JOIN bd_edu_class bec ON bec.business_key = bs.class_business_key
WHERE bu.category = 'student' AND bs.school_business_key = 'e14059b54350457c8726cc99970d14ec'