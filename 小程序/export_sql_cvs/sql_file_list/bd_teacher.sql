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
 bt.school_business_key AS schoolBusinessKey,
 bt.department_business_key AS departmentBusinessKey,
 bt.picture AS picture
FROM base_user bu
INNER JOIN bd_teacher bt ON bt.id = bu.id
INNER JOIN bd_school bs ON bs.business_key = bt.school_business_key
WHERE bu.category = 'teacher' AND bt.school_business_key = 'e14059b54350457c8726cc99970d14ec'