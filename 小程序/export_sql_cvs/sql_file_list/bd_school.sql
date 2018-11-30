SELECT bs.id AS id,
bs.business_key AS businessKey,
bs.address AS address,
bs.code AS code,
bs.create_sch_date AS createSchDate,
bs.district_code AS districtCode,
bs.district_flag AS districtFlag,
bs.email AS email,
bs.en_name AS enName,
bs.is_delete AS isDelete,
bs.name AS name,
bs.school_qualification AS schoolQualification,
bs.create_time AS createTime,
bs.update_time AS updateTime
FROM bd_school bs
WHERE bs.business_key = 'e14059b54350457c8726cc99970d14ec'