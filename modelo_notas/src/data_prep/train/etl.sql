drop table if exists tb_abt_nota;
create table tb_abt_nota as
    select *

    from (
        select t1.*,
            t2.avg_review_score as nota_target,
            case when t1.avg_review_score > t2.avg_review_score then 1 else 0 end as flag_nota_inc

        from tb_book_sellers as t1

        left join tb_book_sellers as t2
        on t1.seller_id = t2.seller_id
        and t1.dt_ref = date( t2.dt_ref, '-1 months' )

        -- Safras para treinar o modelo
        where t1.dt_ref >= '{dt_init}'
        and t1.dt_ref <= '{dt_end}'
    )
    where nota_target is not null
;