SELECT *,
        case when dt_ref = '{dt_ref}' then 1 else 0

FROM {table}

where dt_ref > '{dt_ref}'