-- Write your query below
select s.seller_name from seller s where not exists (select 1 from orders where orders.seller_id = s.seller_id and
      EXTRACT(YEAR FROM orders.sale_date) = 2020) order by seller_name asc;