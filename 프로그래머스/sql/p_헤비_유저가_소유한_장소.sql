# 헤비 유저가 소유한 장소
# with 이용

with temp as (
SELECT host_id, count(*) cnt from places
group by host_id having cnt >=2
)

select * from places 
where host_id in (select host_id from temp)
order by ID